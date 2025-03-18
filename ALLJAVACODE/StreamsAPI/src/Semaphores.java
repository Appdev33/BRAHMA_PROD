import java.util.concurrent.Semaphore;

public class Semaphores {
    private static Semaphores instance = new Semaphores();
    private int connections = 0;
    // Semaphore
    private Semaphore semaphore = new Semaphore(10);

    private Semaphores() {

    }

    public static Semaphores getInstance() {
        return instance;
    }

    public void connect() {
        try {
            semaphore.acquire(); // -1
            doConnect();
        } catch (InterruptedException e1) {
            e1.printStackTrace();
        } finally {
            semaphore.release(); // +1
        }
    }

    public void doConnect() {
        synchronized (this) {
            connections++;
            System.out.println("Current Connections: " + connections);
        }

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        synchronized (this) {
            connections--;
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Semaphores semaphores = Semaphores.getInstance();

        // Simulate multiple connections
        for (int i = 0; i < 5; i++) {
            new Thread(() -> {
                semaphores.connect();
            }).start();
        }

        // Ensure the main thread doesn't exit before other threads complete
        Thread.sleep(10000);
        System.out.println("Finished Main");
    }
}

/*



//public static void main(String[] args) throws InterruptedException {
//	
//	Semaphores obj = new Semaphores();
//	Semaphores.Connection instance = obj.new Connection();
//	ExecutorService executor = Executors.newCachedThreadPool();
//
//	for (int i = 0; i < 200; i++) {
//		// submit => Create a new thread auto
//		executor.submit(new Runnable() {
//
//			@Override
//			public void run() {
//				Connection.getConnection().connect(); //Invoke
//			}
//
//		});
//	}//ENDof For loop
//	
//	executor.shutdown();
//	executor.awaitTermination(1, TimeUnit.DAYS); //Wait for 1 day then ONLY terminate
//}// ENDof Main





/*
Semaphores and locks are both synchronization mechanisms used in concurrent programming to control access to shared resources. 
However, they have some key differences in terms of their usage and functionality:

Mutual Exclusion:

Locks: Primarily used for mutual exclusion. Only one thread can acquire the lock at a time, ensuring that critical sections of code are executed by a single thread.
Semaphores: Can be used for mutual exclusion (binary semaphore with value 1 acts like a lock), but they are more versatile and
can also be used to control access to a resource by multiple threads simultaneously.
Number of Permits:

Locks: Generally allow only one thread to acquire the lock at a time.
Semaphores: Can be configured to allow multiple threads to acquire permits. A semaphore with a count greater than 1 allows that number 
of threads to enter the critical section simultaneously.
Acquiring and Releasing:

Locks: Typically acquired and released explicitly using lock() and unlock() methods.
Semaphores: Acquired using acquire() and released using release() methods. A semaphore with multiple permits can be acquired and released incrementally.
Functionality:

Locks: Focus on providing mutual exclusion and often come with built-in support for features like reentrant locking, interruptible locking, 
and fairness policies (e.g., ReentrantLock in Java).
Semaphores: Provide a more general signaling mechanism. Besides mutual exclusion, semaphores can be used for signaling between threads, 
counting available resources, and implementing other synchronization patterns.
Permit Counting:

Locks: Do not inherently provide a counting mechanism.
Semaphores: Have an associated count (number of available permits), which allows for more complex synchronization scenarios.
Blocking Behavior:

Locks: Usually block until the lock is acquired. Some lock implementations may provide options for timed waits and interruptible locks.
Semaphores: Provide flexibility in terms of blocking behavior. The acquire() method can block until a permit is available, block for a specified time, 
or proceed without blocking if a permit is immediately available.
Use Cases:

Locks: Commonly used when only one thread should access a critical section at a time, such as protecting shared data structures.
Semaphores: Useful for scenarios where multiple threads can access a shared resource simultaneously or when counting resources is necessary 
(e.g., limiting the number of concurrent database connections).
In summary, while locks are specialized for mutual exclusion, semaphores offer more flexibility and can be applied to a broader range of synchronization problems,
including situations where multiple threads need concurrent access to a shared resource. The choice between them depends on the specific requirements of the concurrent task at hand.

*/


/*The code demonstrates how a Semaphore can be used to control access to a shared resource (in this case, the connection logic inside doConnect). 
* The semaphore limits the number of concurrent connections to 10, ensuring that no more than 10 threads can execute the critical section simultaneously.
*  The synchronization blocks and semaphore management help prevent race conditions and ensure proper coordination among the threads.
*/