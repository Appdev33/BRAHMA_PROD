import time
import requests
from functools import wraps
# ---------------- RETRY DECORATOR ----------------
def retry(max_attempts=5, delay=1, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= max_attempts:
                try:
                    print(f"Attempt {attempt}...")
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Error: {e}")
                    # Last attempt → raise exception
                    if attempt == max_attempts:
                        print("Max retries reached.")
                        raise
                    print(f"Retrying in {delay} sec...\n")
                    time.sleep(delay)
                    attempt += 1
        return wrapper
    return decorator
# ---------------- REAL API FUNCTION ----------------
@retry(
    max_attempts=5,
    delay=1,
    exceptions=(
        requests.exceptions.Timeout,
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError,
    ),
)
def fetch_data(url):
    # timeout=2 seconds
    response = requests.get(url, timeout=2)
    # Raise exception for 4xx/5xx
    response.raise_for_status()
    return response.json()
# ---------------- TEST ----------------
# url = "https://jsonplaceholder.typicode.com/posts/1"
url = "https://httpstat.us/500"
data = fetch_data(url)
print("\nFinal Response:")
print(data)

################################# Circular Buffer Implementation############################
class CircularBuffer:
    """Circular iterator over a fixed-size buffer"""
    def __init__(self, data: list, max_iterations: int = None):
        self.data = data
        self.index = 0
        self.iterations = 0
        self.max_iterations = max_iterations
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.data:
            raise StopIteration
        
        if self.max_iterations and self.iterations >= self.max_iterations:
            raise StopIteration
        
        result = self.data[self.index]
        self.index = (self.index + 1) % len(self.data)
        self.iterations += 1
        return result


# Circular Buffer
circular = CircularBuffer(['A', 'B', 'C'], max_iterations=20)
for item in circular:
    print(item, end=" ")  # A B C A B C A


# *If you want each iteration to restart fresh (unlike a generator object, which is single-use), you can separate the iterator logic:

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # return a *new* iterator object each time
        return CountdownIterator(self.start)


class CountdownIterator:
    def __init__(self, current):
        self.current = current

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
# Usage:

cd = Countdown(3)
for x in cd:
    print(x)

# Works again!
for x in cd:
    print(x)


import time 

class TimerContext:
    """Context manager to measure execution time"""
    def __init__(self, name: str = "Operation"):
        self.name = name
        self.start_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        print(f"Starting {self.name}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start_time
        print(f"{self.name} took {elapsed:.4f} seconds")
        return False
    
    @property
    def elapsed(self):
        return time.time() - self.start_time


# Timer context
with TimerContext("Data Processing") as timer:
    time.sleep(0.5)
    print(f"Current elapsed: {timer.elapsed:.2f}s")
    time.sleep(0.5) 


# https://claude.ai/chat/8798c22f-8993-4965-992e-fe015b436174

# Non-data descriptor — only __get__. Instance dict takes priority.

class Greeting:
    # non-data: no __set__, instance dict wins
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self           # class access → return descriptor
        return f"Hello, {obj.name}"

class Person:
    greet = Greeting()
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.greet)            # Hello, Alice
p.__dict__["greet"] = "hi"
print(p.greet)            # hi  ← instance dict wins


# Data descriptor — has both __get__ and __set__. Overrides instance dict.

class Positive:
    # data: __set__ defined → beats instance dict
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self._name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self._name} must be > 0")
        setattr(obj, self._name, value)

class Circle:
    radius = Positive()
    def __init__(self, r): self.radius = r

c = Circle(5)
print(c.radius)           # 5
c.radius = -1             # ValueError: _radius must be > 0

# Typed descriptor — enforces type on every assignment. Reusable across fields.

class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = name
        self.private = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None: return self
        return getattr(obj, self.private, None)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name}: expected {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        setattr(obj, self.private, value)

class Employee:
    name = Typed(str)
    age  = Typed(int)
    def __init__(self, name, age):
        self.name, self.age = name, age

e = Employee("Bob", 30)
e.age = "old"              # TypeError: age: expected int, got str

# Cached (lazy) property — computes once on first access, stores in instance dict.

class CachedProperty:
    # non-data → instance dict write sticks after first call
    def __init__(self, func):
        self.func = func
        self.__doc__ = func.__doc__

    def __set_name__(self, owner, name):
        self.attrname = name

    def __get__(self, obj, objtype=None):
        if obj is None: return self
        val = self.func(obj)
        obj.__dict__[self.attrname] = val  # cache in instance
        return val

class DataSet:
    def __init__(self, data):
        self.data = data

    @CachedProperty
    def stats(self):
        print("computing...")    # runs only once
        return sum(self.data) / len(self.data)

ds = DataSet([1,2,3,4])
print(ds.stats)   # computing... → 2.5
print(ds.stats)   # 2.5  (cached, no recompute)

# ReadOnly descriptor — raises on assignment. Uses __delete__ too for full data descriptor.
class ReadOnly:
    def __set_name__(self, owner, name):
        self.name = name
        self.private = "_ro_" + name

    def __get__(self, obj, objtype=None):
        if obj is None: return self
        return getattr(obj, self.private)

    def __set__(self, obj, value):
        if hasattr(obj, self.private):
            raise AttributeError(f"{self.name} is read-only")
        setattr(obj, self.private, value)  # allow __init__

    def __delete__(self, obj):
        raise AttributeError(f"{self.name} cannot be deleted")

class Config:
    version = ReadOnly()
    def __init__(self, v): self.version = v

cfg = Config("1.0")
print(cfg.version)        # 1.0
cfg.version = "2.0"      # AttributeError: version is read-only


# custom exception hierarchy
# Build a typed exception tree. Catch broad or narrow — callers choose.

class AppError(Exception):
    """Base for all app errors."""
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

    def __str__(self):
        return f"[{self.code}] {super().__str__()}" if self.code else super().__str__()


class ValidationError(AppError):
    def __init__(self, field, message):
        super().__init__(message, code="VALIDATION")
        self.field = field

    def __str__(self):
        return f"[VALIDATION] '{self.field}': {self.args[0]}"


class NotFoundError(AppError):
    def __init__(self, resource, id_):
        super().__init__(f"{resource} with id={id_} not found", code="NOT_FOUND")
        self.resource = resource
        self.id = id_


class DatabaseError(AppError): ...
class AuthError(AppError): ...


# --- usage ---
try:
    raise ValidationError("email", "must contain @")
except ValidationError as e:
    print(e)               # [VALIDATION] 'email': must contain @
    print(e.field)         # email
except AppError as e:
    print("generic app error:", e)


# all try/except patterns
# Every clause form: multi-except, tuple catch, else, finally, bare re-raise.

import sys

def parse_config(path):
    try:
        f = open(path)                       # may raise
        data = f.read()

    except FileNotFoundError:
        print("file missing")               # specific

    except (PermissionError, OSError) as e:
        print("OS problem:", e)             # tuple catch

    except Exception as e:
        print("unexpected:", type(e).__name__, e)
        raise                               # bare re-raise keeps traceback

    else:
        # runs ONLY if no exception was raised
        print("read ok:", len(data), "bytes")
        return data

    finally:
        # ALWAYS runs — even after return or raise
        print("cleanup done")


# catching everything (rarely correct — last resort only)
try:
    risky()
except BaseException as e:
    # catches KeyboardInterrupt, SystemExit too
    print("caught:", e)
    raise


# suppress specific errors inline
from contextlib import suppress
with suppress(FileNotFoundError):
    open("missing.txt")     # silently ignored


# exception chaining
# raise X from Y preserves root cause. raise X from None hides it intentionally.

class ServiceError(Exception): ...

def fetch_user(uid):
    try:
        result = db_query(f"SELECT * FROM users WHERE id={uid}")
    except ConnectionError as e:
        # explicit chain: __cause__ set, traceback shows both
        raise ServiceError("user lookup failed") from e

def get_score(uid):
    try:
        return scores[uid]
    except KeyError:
        # suppress chain: cleaner public API, hides KeyError
        raise NotFoundError("score", uid) from None


# inspect chain programmatically
try:
    fetch_user(42)
except ServiceError as e:
    print("cause:", e.__cause__)      # original ConnectionError
    print("context:", e.__context__)  # implicit context (if any)
    print("suppressed:", e.__suppress_context__)


# context manager
# Handle errors in __exit__ — return True to suppress, False to re-raise.

class ManagedOperation:
    def __init__(self, name, swallow=(None,)):
        self.name = name
        self.swallow = swallow   # exception types to suppress

    def __enter__(self):
        print(f"→ starting {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"✓ {self.name} ok")
            return False

        if issubclass(exc_type, self.swallow):
            print(f"⚠ {self.name} swallowed: {exc_val}")
            return True        # suppress exception

        print(f"✗ {self.name} failed: {exc_val}")
        return False           # re-raise


# --- usage ---
with ManagedOperation("db-write", swallow=(TimeoutError,)):
    raise TimeoutError("slow")    # swallowed ✓

with ManagedOperation("parse"):
    raise ValueError("bad input") # re-raised ✗


# same thing with @contextmanager
from contextlib import contextmanager

@contextmanager
def safe_open(path):
    try:
        f = open(path)
        yield f
    except FileNotFoundError:
        yield None
    finally:
        try: f.close()
        except: ...


# decorator handler
# Wrap functions with retry logic and error translation — zero boilerplate at call site.

import functools, time

def retry(times=3, delay=1.0, on=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except on as e:
                    last_exc = e
                    print(f"attempt {attempt}/{times} failed: {e}")
                    if attempt < times:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator


def catch(**mapping):
    # translate one exception type to another
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except tuple(mapping) as e:
                new_exc = mapping[type(e)]
                raise new_exc(str(e)) from e
        return wrapper
    return decorator


# --- usage ---
@retry(times=3, delay=0.5, on=(ConnectionError,))
@catch(**{KeyError: NotFoundError, ValueError: ValidationError})
def fetch_data(url):
    ...                     # retries 3×, translates exceptions


# global hook
# sys.excepthook catches any unhandled exception at process level — last line of defence.

import sys, traceback, logging

logger = logging.getLogger("app")

def global_exception_handler(exc_type, exc_value, exc_tb):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_tb)
        return                  # let Ctrl+C behave normally

    logger.critical(
        "Unhandled exception",
        exc_info=(exc_type, exc_value, exc_tb)
    )
    # optionally: send to Sentry, PagerDuty, etc.

sys.excepthook = global_exception_handler


# for threads — separate hook needed
import threading

def thread_exception_handler(args):
    logger.critical(
        f"Unhandled in thread {args.thread.name}",
        exc_info=(args.exc_type, args.exc_value, args.exc_traceback)
    )

threading.excepthook = thread_exception_handler


# for asyncio tasks
import asyncio

def async_exception_handler(loop, context):
    exc = context.get("exception")
    logger.critical(f"Asyncio error: {context['message']}", exc_info=exc)

loop = asyncio.get_event_loop()
loop.set_exception_handler(async_exception_handler)


# logging integration
# Log errors with full tracebacks, structured context, and severity levels.

import logging, sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("myapp")


def process(record):
    try:
        validate(record)
        save(record)
    except ValidationError as e:
        logger.warning("Validation failed", extra={"record_id": record.id})
        raise
    except DatabaseError:
        logger.error("DB error", exc_info=True)   # full traceback
        raise
    except Exception:
        logger.exception("Unexpected error")       # shorthand for exc_info=True
        raise


# structured logging with extra context
try:
    result = risky_call()
except Exception as e:
    logger.error(
        "Call failed",
        exc_info=True,
        extra={
            "user_id": 42,
            "error_code": getattr(e, "code", None),
            "retryable": isinstance(e, TimeoutError)
        }
    )


# ExceptionGroup (3.11+)
# Raise and handle multiple simultaneous errors — essential for concurrent/async code.

# Python 3.11+ — raise several errors at once
def validate_all(data: dict) -> None:
    errors = []
    if not data.get("name"):
        errors.append(ValidationError("name", "required"))
    if not data.get("email"):
        errors.append(ValidationError("email", "required"))
    if errors:
        raise ExceptionGroup("validation failed", errors)


# except* — matches EACH exception in the group by type
try:
    validate_all({})
except* ValidationError as eg:
    for e in eg.exceptions:
        print(f"  field={e.field}: {e}")
except* DatabaseError as eg:
    print("db errors:", eg.exceptions)


# asyncio.TaskGroup — auto-collects task exceptions
import asyncio

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(fetch("a"))
            tg.create_task(fetch("b"))   # both run; both errors collected
    except* ConnectionError as eg:
        print("failed tasks:", len(eg.exceptions))
