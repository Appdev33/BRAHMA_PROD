import threading
import pickle

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

