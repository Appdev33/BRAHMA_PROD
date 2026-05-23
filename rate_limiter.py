import time
import threading
from collections import defaultdict, deque
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod
import bisect

# ===============================
# ENTITIES AND DATA STRUCTURES
# ===============================

@dataclass
class RateLimitRule:
    """Represents a rate limiting rule configuration"""
    rule_id: str
    max_requests: int
    window_size_ms: int
    
    def __post_init__(self):
        if self.max_requests <= 0:
            raise ValueError("max_requests must be positive")
        if self.window_size_ms <= 0:
            raise ValueError("window_size_ms must be positive")

@dataclass
class Request:
    """Represents a single request with timestamp"""
    user_id: str
    request_id: str
    timestamp: int
    metadata: Dict[str, Any]
    
    def __init__(self, user_id: str, request_id: str, metadata: Dict[str, Any] = None):
        self.user_id = user_id
        self.request_id = request_id
        self.timestamp = int(time.time() * 1000)  # Current time in milliseconds
        self.metadata = metadata or {}

@dataclass
class RateLimitResult:
    """Represents the result of a rate limit check"""
    allowed: bool
    remaining_requests: int
    reset_time_ms: int
    retry_after_ms: int
    
    def __str__(self):
        return f"RateLimitResult(allowed={self.allowed}, remaining={self.remaining_requests})"

class TimeWindow:
    """Represents a time window for sliding window algorithm"""
    
    def __init__(self, start_time: int, duration: int):
        self.start_time = start_time
        self.duration = duration
        self.end_time = start_time + duration
    
    def contains(self, timestamp: int) -> bool:
        """Check if timestamp falls within this window"""
        return self.start_time <= timestamp < self.end_time
    
    def __str__(self):
        return f"TimeWindow({self.start_time}-{self.end_time})"

class SlidingWindowBucket:
    """Sliding window bucket that tracks requests in a time window"""
    
    def __init__(self):
        self.request_timestamps: List[int] = []
        self.lock = threading.RLock()
    
    def add_request(self, timestamp: int):
        """Add a request timestamp to the bucket"""
        with self.lock:
            bisect.insort(self.request_timestamps, timestamp)
    
    def get_request_count(self, window_start: int, window_end: int) -> int:
        """Get count of requests in the specified window"""
        with self.lock:
            # Clean up old entries
            self._cleanup_old_entries(window_start)
            
            # Count requests in the current window
            start_idx = bisect.bisect_left(self.request_timestamps, window_start)
            end_idx = bisect.bisect_left(self.request_timestamps, window_end)
            
            return end_idx - start_idx
    
    def _cleanup_old_entries(self, window_start: int):
        """Remove timestamps older than window_start"""
        cutoff_idx = bisect.bisect_left(self.request_timestamps, window_start)
        if cutoff_idx > 0:
            self.request_timestamps = self.request_timestamps[cutoff_idx:]
    
    def get_total_requests(self) -> int:
        """Get total number of requests in bucket"""
        with self.lock:
            return len(self.request_timestamps)

class User:
    """User entity with rate limiting information"""
    
    def __init__(self, user_id: str, user_tier: str = "standard"):
        self.user_id = user_id
        self.user_tier = user_tier
        self.rate_limit_rules: Dict[str, RateLimitRule] = {}
        self.request_bucket = SlidingWindowBucket()
        self.lock = threading.RLock()
    
    def add_rate_limit_rule(self, endpoint: str, rule: RateLimitRule):
        """Add a rate limit rule for a specific endpoint"""
        with self.lock:
            self.rate_limit_rules[endpoint] = rule
    
    def get_rate_limit_rule(self, endpoint: str) -> Optional[RateLimitRule]:
        """Get rate limit rule for a specific endpoint"""
        with self.lock:
            return self.rate_limit_rules.get(endpoint)
    
    def __str__(self):
        return f"User({self.user_id}, tier={self.user_tier})"

# ===============================
# STORAGE INTERFACES
# ===============================

class RateLimiterStorage(ABC):
    """Abstract storage interface for rate limiter"""
    
    @abstractmethod
    def get_user(self, user_id: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def create_user(self, user_id: str, user_tier: str = "standard") -> User:
        pass
    
    @abstractmethod
    def increment_request_count(self, user_id: str, timestamp: int):
        pass
    
    @abstractmethod
    def get_request_count(self, user_id: str, window_start: int, window_end: int) -> int:
        pass

class InMemoryStorage(RateLimiterStorage):
    """In-memory storage implementation"""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.lock = threading.RLock()
    
    def get_user(self, user_id: str) -> Optional[User]:
        with self.lock:
            return self.users.get(user_id)
    
    def create_user(self, user_id: str, user_tier: str = "standard") -> User:
        with self.lock:
            if user_id in self.users:
                return self.users[user_id]
            
            user = User(user_id, user_tier)
            self.users[user_id] = user
            return user
    
    def increment_request_count(self, user_id: str, timestamp: int):
        with self.lock:
            user = self.get_user(user_id)
            if user:
                user.request_bucket.add_request(timestamp)
    
    def get_request_count(self, user_id: str, window_start: int, window_end: int) -> int:
        with self.lock:
            user = self.get_user(user_id)
            if user:
                return user.request_bucket.get_request_count(window_start, window_end)
            return 0

# ===============================
# RATE LIMITING STRATEGIES
# ===============================

class RateLimitStrategy(ABC):
    """Abstract rate limiting strategy"""
    
    @abstractmethod
    def is_allowed(self, user: User, rule: RateLimitRule, current_time: int) -> RateLimitResult:
        pass

class SlidingWindowStrategy(RateLimitStrategy):
    """Sliding window rate limiting strategy"""
    
    def __init__(self, storage: RateLimiterStorage):
        self.storage = storage
    
    def is_allowed(self, user: User, rule: RateLimitRule, current_time: int) -> RateLimitResult:
        window_start = current_time - rule.window_size_ms
        window_end = current_time
        
        # Get current request count in the window
        current_count = self.storage.get_request_count(
            user.user_id, window_start, window_end
        )
        
        # Check if request is allowed
        allowed = current_count < rule.max_requests
        remaining = max(0, rule.max_requests - current_count - (1 if allowed else 0))
        
        # Calculate reset time (end of current window)
        reset_time = current_time + rule.window_size_ms
        
        # Calculate retry after time
        retry_after = 0 if allowed else rule.window_size_ms
        
        return RateLimitResult(
            allowed=allowed,
            remaining_requests=remaining,
            reset_time_ms=reset_time,
            retry_after_ms=retry_after
        )

# ===============================
# MAIN RATE LIMITER CLASS
# ===============================

class SlidingWindowRateLimiter:
    """Main sliding window rate limiter class"""
    
    def __init__(self, storage: RateLimiterStorage = None, 
                 strategy: RateLimitStrategy = None):
        self.storage = storage or InMemoryStorage()
        self.strategy = strategy or SlidingWindowStrategy(self.storage)
        self.default_rules: Dict[str, RateLimitRule] = {}
        self.lock = threading.RLock()
    
    def add_default_rule(self, endpoint: str, rule: RateLimitRule):
        """Add a default rate limit rule for an endpoint"""
        with self.lock:
            self.default_rules[endpoint] = rule
    
    def create_user(self, user_id: str, user_tier: str = "standard") -> User:
        """Create a new user with default rules"""
        user = self.storage.create_user(user_id, user_tier)
        
        # Apply default rules
        with self.lock:
            for endpoint, rule in self.default_rules.items():
                user.add_rate_limit_rule(endpoint, rule)
        
        return user
    
    def is_allowed(self, user_id: str, endpoint: str = "default") -> RateLimitResult:
        """Check if a request is allowed for the user"""
        current_time = int(time.time() * 1000)
        
        # Get or create user
        user = self.storage.get_user(user_id)
        if not user:
            user = self.create_user(user_id)
        
        # Get rate limit rule
        rule = user.get_rate_limit_rule(endpoint)
        if not rule:
            # If no rule exists, allow the request
            return RateLimitResult(
                allowed=True,
                remaining_requests=float('inf'),
                reset_time_ms=current_time,
                retry_after_ms=0
            )
        
        # Check if request is allowed
        result = self.strategy.is_allowed(user, rule, current_time)
        
        # If allowed, increment the request count
        if result.allowed:
            self.storage.increment_request_count(user_id, current_time)
        
        return result
    
    def process_request(self, request: Request, endpoint: str = "default") -> RateLimitResult:
        """Process a request and return rate limit result"""
        return self.is_allowed(request.user_id, endpoint)

# ===============================
# EXAMPLE USAGE AND TESTING
# ===============================

def example_usage():
    """Example usage of the sliding window rate limiter"""
    
    # Create rate limiter
    rate_limiter = SlidingWindowRateLimiter()
    
    # Add default rules
    api_rule = RateLimitRule("api_limit", max_requests=10, window_size_ms=60000)  # 10 requests per minute
    rate_limiter.add_default_rule("api", api_rule)
    
    # Create users
    user1 = rate_limiter.create_user("user1", "premium")
    user2 = rate_limiter.create_user("user2", "standard")
    
    # Test rate limiting
    print("Testing rate limiter...")
    
    # Make requests for user1
    for i in range(12):
        result = rate_limiter.is_allowed("user1", "api")
        print(f"Request {i+1} for user1: {result}")
        
        if i == 5:  # Sleep a bit to show time-based behavior
            time.sleep(0.1)
    
    print("\nTesting user2...")
    
    # Make requests for user2
    for i in range(5):
        result = rate_limiter.is_allowed("user2", "api")
        print(f"Request {i+1} for user2: {result}")

if __name__ == "__main__":
    example_usage()