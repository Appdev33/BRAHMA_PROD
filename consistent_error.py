"""
============================================================
  PYTHON ERROR & EXCEPTION HANDLING — INTERVIEW PRACTICE
============================================================
  Topics Covered:
  1.  Custom Exception Hierarchy
  2.  Standard Error Response Schema
  3.  Framework-style Central Error Handlers (FastAPI & Flask)
  4.  Wrapping External API Calls
  5.  Context Managers as Error Boundaries
  6.  Structured Logging
  7.  Retry Logic with Exponential Backoff
  8.  Exception Chaining  (raise ... from ...)
  9.  finally / else blocks
  10. Practical: Simulated API Request Pipeline (run it!)
============================================================
"""

import logging
import time
import uuid
import random
from contextlib import contextmanager
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from functools import wraps


# ─────────────────────────────────────────────
# SECTION 1 — CUSTOM EXCEPTION HIERARCHY
# ─────────────────────────────────────────────
"""
WHY: Catch specific errors cleanly; never use bare `except Exception`
in production unless it's the last-resort global handler.
"""

class AppError(Exception):
    """Base class — all app errors inherit from this."""
    def __init__(self, message: str, code: str, status_code: int = 500, details: dict = None):
        self.message = message
        self.code = code            # machine-readable slug  e.g. "USER_NOT_FOUND"
        self.status_code = status_code
        self.details = details or {}
        super().__init__(message)

    def __repr__(self):
        return f"{self.__class__.__name__}(code={self.code!r}, status={self.status_code})"


# ── 4xx Client Errors ──────────────────────────────────────
class NotFoundError(AppError):
    def __init__(self, resource: str, resource_id: str):
        super().__init__(
            message=f"{resource} '{resource_id}' not found",
            code="NOT_FOUND",
            status_code=404,
        )

class ValidationError(AppError):
    def __init__(self, fields: dict):
        super().__init__(
            message="Validation failed",
            code="VALIDATION_ERROR",
            status_code=422,
            details={"fields": fields},
        )

class AuthError(AppError):
    def __init__(self, reason: str = "Unauthorized"):
        super().__init__(reason, "AUTH_ERROR", 401)

class ForbiddenError(AppError):
    def __init__(self, action: str = "perform this action"):
        super().__init__(f"Not allowed to {action}", "FORBIDDEN", 403)

class RateLimitError(AppError):
    def __init__(self, retry_after: int = 60):
        super().__init__(
            "Too many requests — slow down",
            "RATE_LIMITED",
            429,
            {"retry_after": retry_after},
        )

class ConflictError(AppError):
    def __init__(self, resource: str):
        super().__init__(f"{resource} already exists", "CONFLICT", 409)


# ── 5xx Server / External Errors ──────────────────────────
class ExternalAPIError(AppError):
    """Wraps errors from third-party services."""
    pass

class DatabaseError(AppError):
    def __init__(self, detail: str = "Database operation failed"):
        super().__init__(detail, "DB_ERROR", 503)

class ServiceUnavailableError(AppError):
    def __init__(self, service: str):
        super().__init__(f"{service} is unavailable", "SERVICE_UNAVAILABLE", 503)

class TimeoutError(AppError):
    def __init__(self, service: str):
        super().__init__(f"{service} timed out", "TIMEOUT", 504)


# ─────────────────────────────────────────────
# SECTION 2 — STANDARD ERROR RESPONSE SCHEMA
# ─────────────────────────────────────────────
"""
WHY: Every endpoint returns the SAME shape so consumers parse one format.
Interview tip: "consistency in API contracts reduces client-side complexity."
"""

@dataclass
class ErrorEnvelope:
    error: dict
    request_id: str = field(default_factory=lambda: f"req_{uuid.uuid4().hex[:8]}")
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return asdict(self)


def build_error_response(exc: AppError, request_id: str = None) -> dict:
    envelope = ErrorEnvelope(
        error={
            "code": exc.code,
            "message": exc.message,
            "status": exc.status_code,
            "details": exc.details,
        },
        request_id=request_id or f"req_{uuid.uuid4().hex[:8]}",
    )
    return envelope.to_dict()

# Sample output:
# {
#   "error": {
#     "code": "VALIDATION_ERROR",
#     "message": "Validation failed",
#     "status": 422,
#     "details": {"fields": {"email": "Invalid format"}}
#   },
#   "request_id": "req_a1b2c3d4",
#   "timestamp": "2025-04-15T10:00:00+00:00"
# }


# ─────────────────────────────────────────────
# SECTION 3 — CENTRAL ERROR HANDLERS
# (Framework-style — no Flask/FastAPI needed)
# ─────────────────────────────────────────────
"""
WHY: One place handles all errors — routes just raise, never build responses.
"""

logger = logging.getLogger("api")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
)


def handle_request(handler_fn, request: dict):
    """
    Simulates the middleware layer of a web framework.
    Wraps any route handler so errors are caught centrally.
    """
    request_id = request.get("id", f"req_{uuid.uuid4().hex[:8]}")
    try:
        result = handler_fn(request)
        return {"status": "ok", "data": result, "request_id": request_id}

    except AppError as exc:
        logger.warning(
            "App error: %s",
            exc.code,
            extra={"request_id": request_id, "status_code": exc.status_code},
        )
        return build_error_response(exc, request_id)

    except Exception as exc:
        # Last-resort — never leak internals
        logger.exception("Unhandled exception", exc_info=exc, extra={"request_id": request_id})
        generic = AppError("An unexpected error occurred", "INTERNAL_ERROR", 500)
        return build_error_response(generic, request_id)


# ─────────────────────────────────────────────
# SECTION 4 — WRAPPING EXTERNAL API CALLS
# ─────────────────────────────────────────────
"""
WHY: Third-party errors must be translated into YOUR hierarchy.
Never let raw httpx/requests exceptions bubble to the client.
Interview tip: "own your error surface — consumers shouldn't know
                which third-party service failed."
"""

class FakeHTTPError(Exception):
    """Stand-in for httpx.HTTPStatusError in this demo."""
    def __init__(self, status_code: int):
        self.status_code = status_code

class FakeTimeoutError(Exception):
    """Stand-in for httpx.TimeoutException."""
    pass


def call_payment_api(payload: dict) -> dict:
    """
    Simulates calling an external payment service.
    Real code: replace FakeHTTPError with httpx / requests exceptions.
    """
    # Simulate different failure modes
    scenario = payload.get("_simulate", "success")

    try:
        if scenario == "timeout":
            raise FakeTimeoutError()
        elif scenario == "declined":
            raise FakeHTTPError(402)
        elif scenario == "rate_limit":
            raise FakeHTTPError(429)
        elif scenario == "server_error":
            raise FakeHTTPError(500)
        return {"transaction_id": "txn_abc123", "status": "charged"}

    except FakeTimeoutError:
        raise TimeoutError("Payment service")          # translate → our type

    except FakeHTTPError as e:
        if e.status_code == 402:
            raise ExternalAPIError("Card was declined", "CARD_DECLINED", 402)
        elif e.status_code == 429:
            raise RateLimitError(retry_after=30)
        else:
            raise ExternalAPIError("Payment service error", "PAYMENT_ERROR", 502)


# ─────────────────────────────────────────────
# SECTION 5 — CONTEXT MANAGERS AS ERROR BOUNDARIES
# ─────────────────────────────────────────────
"""
WHY: Reusable, composable error translation without try/except
     scattered across every function.
"""

class FakeIntegrityError(Exception): pass
class FakeOperationalError(Exception): pass


@contextmanager
def db_error_boundary():
    """Translates raw DB driver exceptions into AppErrors."""
    try:
        yield
    except FakeIntegrityError as e:
        raise ValidationError({"db": "Constraint violation"}) from e   # chaining!
    except FakeOperationalError as e:
        raise DatabaseError("Database connection lost") from e
    except AppError:
        raise   # let already-translated errors pass through


@contextmanager
def external_service_boundary(service_name: str):
    """Generic boundary for any third-party call."""
    try:
        yield
    except (AppError, ExternalAPIError):
        raise
    except Exception as e:
        raise ServiceUnavailableError(service_name) from e


# EXCEPTION CHAINING — interview must-know
# ─────────────────────────────────────────
# raise NewError("msg") from original_error
#   → sets __cause__; "The above exception was the direct cause of..."
#
# raise NewError("msg")   (no 'from')
#   → sets __context__; "During handling of the above exception..."
#
# raise NewError("msg") from None
#   → suppresses original; clean user-facing message
#
# Access chain:   try: ... except AppError as e: print(e.__cause__)


# ─────────────────────────────────────────────
# SECTION 6 — STRUCTURED LOGGING
# ─────────────────────────────────────────────
"""
WHY: Structured logs are queryable in tools like Datadog / Loki.
     exc_info=True preserves full traceback without leaking it to the user.
"""

def log_error(exc: Exception, request_id: str = None, user_id: str = None):
    extra = {
        "request_id": request_id,
        "user_id": user_id,
        "error_code": getattr(exc, "code", "UNKNOWN"),
        "status_code": getattr(exc, "status_code", 500),
        "details": getattr(exc, "details", {}),
    }
    if isinstance(exc, AppError) and exc.status_code < 500:
        logger.warning("Client error: %s", exc.message, extra=extra)
    else:
        logger.error("Server error: %s", exc, extra=extra, exc_info=True)


# ─────────────────────────────────────────────
# SECTION 7 — RETRY WITH EXPONENTIAL BACKOFF
# ─────────────────────────────────────────────
"""
WHY: Transient failures (timeouts, rate limits) shouldn't hard-fail.
Interview tip: "always add jitter to prevent thundering herd."
"""

def retry(
    max_attempts: int = 3,
    backoff_base: float = 0.5,
    retriable: tuple = (TimeoutError, RateLimitError, ServiceUnavailableError),
):
    """Decorator: retry on transient errors with exponential backoff + jitter."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return fn(*args, **kwargs)
                except retriable as e:
                    last_exc = e
                    wait = backoff_base * (2 ** (attempt - 1)) + random.uniform(0, 0.3)
                    logger.warning(
                        "Attempt %d/%d failed (%s). Retrying in %.2fs…",
                        attempt, max_attempts, e.code, wait,
                    )
                    if attempt < max_attempts:
                        time.sleep(wait)
            raise last_exc  # re-raise after exhausting retries
        return wrapper
    return decorator


@retry(max_attempts=3, backoff_base=0.1)  # fast for demo
def fetch_user_data(user_id: str) -> dict:
    """Simulates a flaky external call."""
    if random.random() < 0.5:   # 50% chance of transient failure
        raise TimeoutError("UserService")
    return {"id": user_id, "name": "Alice", "email": "alice@example.com"}


# ─────────────────────────────────────────────
# SECTION 8 — finally / else  (interview classic)
# ─────────────────────────────────────────────
"""
RULES:
  try   → code that might raise
  except→ handle specific errors
  else  → runs ONLY if no exception was raised  ← often forgotten!
  finally→ ALWAYS runs (cleanup: close files, release locks, DB sessions)
"""

def read_config(path: str) -> dict:
    file = None
    try:
        file = open(path, "r")          # might raise FileNotFoundError
        data = file.read()              # might raise IOError
    except FileNotFoundError:
        logger.error("Config file not found: %s", path)
        return {}
    except IOError as e:
        raise AppError(f"Failed to read config: {e}", "CONFIG_READ_ERROR") from e
    else:
        # Only runs if open() AND read() succeeded
        logger.info("Config loaded successfully (%d bytes)", len(data))
        return {"raw": data}
    finally:
        # Always runs — even if we return inside try/except
        if file:
            file.close()
            logger.debug("Config file handle closed")


# ─────────────────────────────────────────────
# SECTION 9 — A COMPLETE SIMULATED PIPELINE
# Run this file directly: python error_handling_interview.py
# ─────────────────────────────────────────────

def create_user_route(request: dict) -> dict:
    """Fake route handler — validates input, hits DB, charges payment."""
    body = request.get("body", {})

    # --- Validation ---
    errors = {}
    if not body.get("email"):
        errors["email"] = "Required"
    if not body.get("name"):
        errors["name"] = "Required"
    if errors:
        raise ValidationError(errors)

    # --- DB write (via error boundary) ---
    with db_error_boundary():
        if body.get("email") == "dupe@example.com":
            raise FakeIntegrityError("unique constraint")
        user = {"id": f"usr_{uuid.uuid4().hex[:6]}", **body}

    # --- External payment (translated errors) ---
    with external_service_boundary("PaymentGateway"):
        charge = call_payment_api({"amount": 9.99, "_simulate": body.get("_payment", "success")})

    return {"user": user, "charge": charge}


def run_demo():
    print("\n" + "═" * 60)
    print("  DEMO — Simulated API Error Handling Pipeline")
    print("═" * 60)

    scenarios = [
        # (label, request_body)
        ("✅ Happy path",          {"name": "Alice", "email": "alice@example.com"}),
        ("❌ Validation error",    {"name": "", "email": ""}),
        ("❌ Duplicate email",     {"name": "Bob", "email": "dupe@example.com"}),
        ("❌ Payment declined",    {"name": "Eve", "email": "eve@example.com", "_payment": "declined"}),
        ("❌ Payment timeout",     {"name": "Dan", "email": "dan@example.com", "_payment": "timeout"}),
        ("❌ Rate limited",        {"name": "Zoe", "email": "zoe@example.com", "_payment": "rate_limit"}),
    ]

    for label, body in scenarios:
        print(f"\n{'─'*55}")
        print(f"  {label}")
        print(f"{'─'*55}")
        req = {"id": f"req_{uuid.uuid4().hex[:6]}", "body": body}
        response = handle_request(create_user_route, req)
        import json
        print(json.dumps(response, indent=2))

    # Retry demo
    print(f"\n{'─'*55}")
    print("  🔁 Retry with backoff (fetch_user_data — 50% flakiness)")
    print(f"{'─'*55}")
    try:
        user = fetch_user_data("usr_42")
        print(f"  Result: {user}")
    except TimeoutError as e:
        print(f"  All retries exhausted — final error: {e!r}")

    print("\n" + "═" * 60 + "\n")


if __name__ == "__main__":
    run_demo()