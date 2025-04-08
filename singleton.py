import threading

class SingletonMeta(type):
    """ A thread-safe implementation of Singleton using metaclass. """

    _instances = {}  # Dictionary to store instances of classes

    _lock = threading.Lock()  # Ensures thread safety during instance creation

    def __call__(cls, *args, **kwargs):
        """ Controls instance creation. Ensures only one instance exists. """
        if cls not in cls._instances:
            with cls._lock:  # Ensures only one thread creates the instance
                if cls not in cls._instances:  # Double-checked locking
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class MultithreadedSingleton(metaclass=SingletonMeta):
    """ Singleton class using the SingletonMeta metaclass. """

    def __init__(self):
        """ Prevents reflection-based instantiation. """
        if hasattr(self, "_initialized"):
            raise RuntimeError("Use getInstance() method to create a singleton")
        self._initialized = True  # Marks that initialization is complete

    def __str__(self):
        return f"Singleton Instance ID: {id(self)}"

    def __reduce__(self):
        """ Prevents singleton breakage via serialization (pickle). """
        return self.__class__, ()

# Explanation of Each Component in Python
# 1. SingletonMeta (metaclass)
# Why Metaclass? Python doesn't have static methods like Java for singleton handling, so a metaclass ensures only one instance exists.
# _instances Dictionary: Stores instances of all singleton classes, ensuring only one instance is created per class.
# Thread-Safety (_lock): Uses threading.Lock() to ensure only one thread initializes the instance at a time.
# 2. __call__()
# Controls instance creation: When MultithreadedSingleton() is called, __call__() is executed instead of __init__().
# Double-Checked Locking: Ensures that even with multiple threads, only one instance is created.
# 3. MultithreadedSingleton (Singleton Class)
# Uses SingletonMeta metaclass: Ensures singleton properties.
# if hasattr(self, "_initialized"):
# Prevents reflection-based attacks where an object is re-created via direct instantiation.
# self._initialized = True
# Used to track if the instance is already initialized.
# 4. __reduce__()
# Protects Against Serialization (pickle)
# Ensures that deserializing (pickle.load) returns the same singleton instance instead of creating a new object.
