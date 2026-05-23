

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


from dataclasses import dataclass

@dataclass(frozen="True")
class Immutable:
	name:str
	age:int

p = Immutable("alice",10)	
p.age =12	
		
	
class Immutable:
    def __init__(self, age, name):
        super().__setattr__('_locked', False)  # Allow setting during init
        self.name = name
        self.age = age
        super().__setattr__('_locked', True)   # Lock after init

    def __setattr__(self, key, value):
        if getattr(self, '_locked', False):
            raise AttributeError("Can't change attribute. Object is immutable.")
        super().__setattr__(key, value)

# Usage
p = Immutable(30, "Alice")
print(p.name)    # Alice
p.name = "Bob"   # ❌ Raises AttributeError


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


class Singleton:
    _instance = None  # This is a class-level variable to store the one-and-only instance.

    def __new__(cls):  # This method controls how the object is created.
        if cls._instance is None:  # If no instance has been created yet...
            cls._instance = super(Singleton, cls).__new__(cls)  # Create and save it
        return cls._instance  # Return the same instance every time

a = Singleton()
b = Singleton()
print(a is b)


import threading

class NewClass:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, a):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    # Initialize attributes here, inside __new__
                    cls._instance.a = a
        return cls._instance

    def get_value(self):
        return self.a

# Usage
obj1 = NewClass(10)
obj2 = NewClass(20)

print(obj1 is obj2)           # True
print(obj1.get_value())       # 10
print(obj2.get_value())       # 10

# cls._instance = super().__new__(cls)
# super() refers to the parent class of NewClass, which is object by default.
# object.__new__(cls) actually allocates memory for a new instance of cls.


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


from abc import ABC, abstractmethod

# Abstract base class
class Notifier(ABC):
    @abstractmethod
    def notify(self, message):
        pass


# Concrete implementation
class EmailNotifier(Notifier):
    def notify(self, message):
        print(f"This is message from Email: {message}")


# Factory class
class NotifierFactory:
    @staticmethod
    def get_notifier(channel):
        channels = {
            "email": EmailNotifier
        }

        notifier_cls = channels.get(channel)

        if notifier_cls is None:
            raise ValueError("Unidentified Notifier")

        return notifier_cls()


# Client code
def send_alert(channel, message):
    notifier = NotifierFactory.get_notifier(channel)
    notifier.notify(message)


# Usage
send_alert("email", "Checking this")

# 🏭 What is the Factory Design Pattern? (Layman Explanation)
# Imagine you go to a restaurant 🍔🍕.
# You don’t go into the kitchen and cook yourself.
# You just say:
# “I want a burger.”

# The kitchen (factory) decides:
# which ingredients to use
# how to cook it
# who prepares it

# You don’t care how it’s made — you only care that you get a burger.
# 👉 That’s exactly what the Factory Pattern does.

# 🧠 In One Line (Layman)
# Factory Pattern = “Tell me WHAT you want, not HOW to create it.”

# 💻 Without Factory (Problem)
def send_alert(channel, message):
    if channel == "email":
        notifier = EmailNotifier()
    elif channel == "sms":
        notifier = SMSNotifier()
    elif channel == "push":
        notifier = PushNotifier()
    else:
        raise ValueError("Invalid channel")
    notifier.notify(message)

# ❌ Problems

# Too many if/elif
# Every new notifier → modify this function
# Code becomes hard to maintain
# Breaks Open/Closed Principle

from abc import ABC, abstractmethod


# ===================== BASE INTERFACE =====================
class Notifier(ABC):
    @abstractmethod
    def notify(self, message):
        pass


# ===================== EXISTING NOTIFIER =====================
class EmailNotifier(Notifier):
    def notify(self, message):
        print(f"📧 Email: {message}")  
        # EXISTING CODE → NO CHANGE REQUIRED


# ===================== NEW NOTIFIER ADDED =====================
class SMSNotifier(Notifier):
    def notify(self, message):
        print(f"📱 SMS: {message}")  
        # ✅ NEW FEATURE ADDED WITHOUT TOUCHING CLIENT CODE


# ===================== FACTORY =====================
class NotifierFactory:
    @staticmethod
    def get_notifier(channel):
        channels = {
            "email": EmailNotifier,    # EXISTING MAPPING
            "sms": SMSNotifier,        # ✅ NEW ELEMENT ADDED HERE
        }

        notifier_cls = channels.get(channel)

        if not notifier_cls:
            raise ValueError("Unknown Notifier Type")

        return notifier_cls()
        # ✅ OBJECT CREATION CENTRALIZED


# ===================== CLIENT CODE =====================
def send_alert(channel, message):
    notifier = NotifierFactory.get_notifier(channel)
    notifier.notify(message)
    # ✅ CLIENT CODE NEVER CHANGES


# ===================== USAGE =====================
send_alert("email", "Server is running")
send_alert("sms", "Server CPU high")   # ✅ NEW FUNCTIONALITY WORKS



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



def no_divide_by_zero(func):
    def wrapper(*args, **kwargs):
        if len(args) > 1 and args[1] == 0:
            raise ZeroDivisionError("Division by zero!")
        return func(*args, **kwargs)
    return wrapper


@no_divide_by_zero
def divide(a, b):
    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Raises ZeroDivisionError

