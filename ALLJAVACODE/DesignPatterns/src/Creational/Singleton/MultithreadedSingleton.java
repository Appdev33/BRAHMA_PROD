package Creational.Singleton;

import java.io.Serializable;

public class MultithreadedSingleton implements Serializable {

    // Volatile ensures visibility and prevents instruction reordering
    private static volatile MultithreadedSingleton instance = null;

    // Private constructor to prevent instantiation from outside
    private MultithreadedSingleton() {
        // Prevents breaking singleton via reflection
        if (instance != null) {
            throw new RuntimeException("Use getInstance() method to create a singleton");
        }
    }

    // Public method to provide a global access point
    public static MultithreadedSingleton getInstance() {
        if (instance == null) { // First check (before synchronization)
            synchronized (MultithreadedSingleton.class) { // Synchronize only when instance is null
                if (instance == null) { // Second check (inside synchronized block)
                    instance = new MultithreadedSingleton();
                }
            }
        }
        return instance;
    }

    // Protects against breaking singleton via serialization
    protected Object readResolve() {
        return getInstance();
    }
}


//Access Modifiers Used & Explanation
//private static volatile MultithreadedSingleton instance;
//
//private → Prevents direct access and modification from outside the class.
//static → Ensures that there is only one shared instance across all instances of the class.
//volatile → Prevents instruction reordering and ensures that all threads see a fully initialized object.
//private MultithreadedSingleton() (Constructor)
//
//private → Restricts direct instantiation from outside the class.
//Prevents Reflection Attacks → Throws an exception if an instance already exists to prevent creating multiple instances via reflection.
//public static MultithreadedSingleton getInstance()
//
//public → Provides a global access point to obtain the singleton instance.
//static → Allows calling getInstance() without needing an object of the class.
//protected Object readResolve()
//
//protected → Ensures that only this class and its subclasses can override it.
//Prevents Breaking Singleton via Serialization → Ensures that deserialization returns the same instance instead of creating a new one.
//
//
