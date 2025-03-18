package Creational.Singleton;



public class Main {
    public static void main(String[] args) {
        // Get the singleton instance
        MultithreadedSingleton instance = MultithreadedSingleton.getInstance();
        MultithreadedSingleton instance2 = MultithreadedSingleton.getInstance();

        // Use the instance (Example: Print hashcode to confirm it's the same instance)
        System.out.println("Singleton Instance HashCode: " + instance.hashCode());
        System.out.println("Singleton Instance HashCode: " + instance2.hashCode());
    }
}

