

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


### DESIGN PATTERNS*************************

#********************* SINGLETON ****************

