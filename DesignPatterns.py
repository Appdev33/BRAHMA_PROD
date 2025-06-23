

# **************** METACLASS ****************

# A Metaclass is the “class of a class” — it defines how classes themselves behave.
# In Python, everything is an object, including classes. Classes are instances of metaclasses.
# By default, the metaclass for all classes is type.
# Metaclasses allow you to customize class creation (e.g., modify attributes, enforce rules, register classes)

# class UpperMetaAttr(type):
	
# 	def __new__(cls, name, bases, dct):
# 		upperattrs = {k.upper() : v for k,v in dct.items() }
# 		return super().__new__(cls, name, bases, upperattrs)
		
# class Person(metaclass = UpperMetaAttr):
# 	name = 'alice'
# 	age = 20
	
	
	
# print(hasattr(Person, 'name'))  # False
# print(hasattr(Person, 'NAME'))  # True
# print(Person.NAME)              # Alice

# class InterfaceCheckMeta(type):
#     def __new__(cls, name, bases, class_dict):
#         if 'execute' not in class_dict:
#             raise TypeError(f"{name} must define 'execute'")
#         return super().__new__(cls, name, bases, class_dict)

# # Enforcing Interface (Method Check)
# class Job(metaclass=InterfaceCheckMeta):
#     # def execute(self):  # Remove this line to see the error!
#     #     print("Running job")
#     pass

#*****# **************** IMMUTABLE ****************

# Method	Mutability	Use Case
# @dataclass(frozen=True)	❌ Immutable	Preferred, readable
# Manual __setattr__	❌ Immutable	Custom logic needed
# namedtuple	❌ Immutable	Lightweight structs
# object.__setattr__ in frozen dataclass	✅ Controlled mutation	Special cases only

# class ImmutableMeta(type):
#     def __new__(cls, name, bases, dct):
#         original_setattr = dct.get('__setattr__')

#         def locked_setattr(self, key, value):
#             if hasattr(self, key):
#                 raise AttributeError(f"Cannot modify existing attribute '{key}'")
#             raise AttributeError(f"Cannot add new attribute '{key}'")

#         dct['__setattr__'] = locked_setattr
#         return super().__new__(cls, name, bases, dct)

# class ImmutableConfig(metaclass=ImmutableMeta):
#     def __init__(self, token, env):
#         object.__setattr__(self, 'token', token)
#         object.__setattr__(self, 'env', env)

# cfg = ImmutableConfig("XYZ123", "prod")

# print(cfg.token)  # OK

# cfg.token = "ABC"     # ❌ Raises AttributeError
# cfg.api = "v1"        # ❌ Also blocked: cannot add new attr

# obj.name = "Alice" in python equals
# obj.__setattr__("name", "Alice")
# "Hey, Python — instead of using the usual __setattr__, use this one that I’m defining now."
# dct['__setattr__'] = locked_setattr


### #*********************DESIGN PATTERNS*************************

#********************* SINGLETON ****************

# import threading

# class SingletonMeta(type):
#     _instances = {}
#     _lock = threading.Lock()  # class-level lock

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             with SingletonMeta._lock:
#                 if cls not in cls._instances:
#                     instance = super().__call__(*args, **kwargs)
#                     cls._instances[cls] = instance
#         return cls._instances[cls]

# class NewClass(metaclass=SingletonMeta):
#     def __init__(self, a):
#         self.a = a

#     def get_instance(self):
#         return self.a

# # Testing
# a = NewClass(10)
# b = NewClass(20)

# print(a is b)         # ✅ True — same instance
# print(a.a, b.a)       # 10 10 — because only first init worked

# *************** DECORATOR DESIGN PATTERN ****************

# What does @functools.wraps(func) do?
# When you decorate a function, it’s actually replaced by the wrapper function. 
# This can lead to the original function’s metadata being lost, like:

# Its name (__name__)
# Its docstring (__doc__)
# Its signature (for introspection or documentation tools)
# Its module path (__module__)

# import time
# import functools

# def timeit(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):  # fix here
#         start = time.perf_counter()
#         result = func(*args, **kwargs)  # fix: use result
#         end = time.perf_counter()
#         duration = end - start  # fix: proper subtraction
#         print(f"Time taken to execute {func.__name__} is {duration:.4f} seconds")
#         return result
#     return wrapper

# @timeit
# def workdone(n):
#     n = 10 ** n
#     for _ in range(n):
#         pass

# # Call with an argument
# p = workdone(6)


# **************** FACTORY DESIGN PATTERN ****************

# from abc import ABC, abstractmethod

# class Notifier(ABC):
#     @abstractmethod
#     def notify(self, message):
#         pass

# class EmailNotifier(Notifier):
#     def notify(self, message):  # added self parameter
#         print(f"Sending Email: {message}")

# class SMSNotifier(Notifier):
#     def notify(self, message):  # added self parameter
#         print(f"Sending SMS: {message}")

# class WebexNotifier(Notifier):
#     def notify(self, message):  # added self parameter
#         print(f"Sending Webex: {message}")

# class NotifierFactory:
#     @staticmethod
#     def get_notifier(channel):
#         channels = {
#             "email": EmailNotifier,
#             "sms": SMSNotifier,
#             "webex": WebexNotifier
#         }
#         notifier_cls = channels.get(channel.lower())
#         if notifier_cls is None:
#             raise ValueError(f"Notification channel '{channel}' not supported")
#         return notifier_cls()

# # Usage example
# def send_alert(channel: str, message: str):
#     notifier = NotifierFactory.get_notifier(channel)
#     notifier.notify(message)

# # Sending notifications
# send_alert("email", "Migration job completed!")
# send_alert("sms", "Device migration started.")  # Will raise ValueError


# Simple Illustration

# # factory.py
# def create_a():
#     from module_a import ClassA
#     return ClassA()

# def create_b():
#     from module_b import ClassB
#     return ClassB()

# # module_a.py
# from factory import create_b

# class ClassA:
#     def __init__(self):
#         self.b = create_b()  # delayed import via factory

#     def do_something(self):
#         print("A uses B")
#         self.b.do_something()

# # module_b.py
# from factory import create_a

# class ClassB:
#     def __init__(self):
#         self.a = create_a()  # delayed import via factory

#     def do_something(self):
#         print("B uses A")
#         self.a.do_something()


# ****** DIFFERENCE BETWEEN FACTORY AND STRATEGY PATTERNS ******
# Absolutely! Here's a simple, layman-friendly way to understand the difference between
# Factory and Strategy patterns:

# Imagine you’re at a coffee shop:
# Factory Pattern — The Barista Who Makes Your Drink
# You tell the barista: "I want a coffee, or maybe a tea."

# The barista makes the drink for you based on your choice.
# You don’t care how the barista makes it; you just get the final drink.
# Factory = The barista who creates the right drink (object) for you.
# Strategy Pattern — The Way You Drink Your Coffee
# You already have your coffee.

# Now, you want to decide how to drink it: sip slowly, add sugar, or maybe drink it iced.
# You can change the way you drink anytime without changing the coffee itself.
# Strategy = Different ways of drinking your coffee (behaviors) you can swap anytime.

# So...
# Factory is about making the right thing (object).
# Strategy is about choosing how to do something (behavior) with that thing.

# Example recap:
# Factory: "Give me a notifier — email, SMS, or Webex." → It creates the notifier for you.
# Strategy: "Given a notifier, how do you send messages?" → You can change the sending behavior dynamically.



#BELOW 5 ORDERED BY RELEVANCE TO PYTHON
# **************** STRATEGY DESIGN PATTERN ****************

# from abc import ABC, abstractmethod

# class LoggingStrategy(ABC):
#     @abstractmethod
#     def log(self, message):
#         pass

# class FileLoggingStrategy(LoggingStrategy):
#     def __init__(self, filename=None):
#         self.filename = filename

#     def log(self, message):
#         # For demonstration, just print with filename
#         print(f"File Logging strategy [{self.filename}]: {message}")

# class ConsoleLoggingStrategy(LoggingStrategy):
#     def log(self, message):
#         print(f"Console Logging strategy: {message}")

# class RemoteLoggingStrategy(LoggingStrategy):
#     def log(self, message):
#         print(f"Remote Logging strategy: {message}")

# class Logger:

#     def __init__(self, strategy: LoggingStrategy):
#         self._strategy = strategy

#     def set_strategy(self, strategy: LoggingStrategy):
#         self._strategy = strategy

#     def log(self, message: str):
#         self._strategy.log(message)

# # Usage Example
# if __name__ == "__main__":
#     logger = Logger(ConsoleLoggingStrategy())
#     logger.log("Starting migration job for Device_001")

#     logger.set_strategy(FileLoggingStrategy("bmt_migration.log"))
#     logger.log("Migration progress: 50% completed")

#     logger.set_strategy(RemoteLoggingStrategy())
#     logger.log("Migration job completed successfully")




# **************** ADAPTOR DESIGN PATTERN ****************
# **************** OBSERVER DESIGN PATTERN ****************
# **************** COMMAND DESIGN PATTERN ****************
# **************** BUILDER DESIGN PATTERN ****************




# **************** REPOSITORY PATTERN ****************
# [Service Layer]
#      |
# [Repository Interface]
#      |
# [Repository Implementation]
#      |
# [ORM / SQL / API]

# Great question: Python doesn’t enforce the Repository Pattern, 
# but you absolutely can and often should use it, especially in large-scale 
# applications like your BMT system or any layered, enterprise-grade architecture.

# Without repository:

# # tightly coupled logic
# user = db.query(User).filter(User.id == id).first()
# With repository:

# # clean separation
# user = user_repository.get_by_id(id)

# Now:
# You can mock user_repository in tests
# Swap PostgresUserRepository with RedisUserRepository easily
# Keep services focused only on business logic

