
import java.util.*;

public class synchronisedBlocks {
	
	public class WorkerNonSync {

		private Random random = new Random();
		private List<Integer> list1 = new ArrayList<Integer>();
		private List<Integer> list2 = new ArrayList<Integer>();
		
		
		public void stageOne() {
			try {
				Thread.sleep(1);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			list1.add(random.nextInt(100));
		}

		public void stageTwo() {
			try {
				Thread.sleep(1);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			list2.add(random.nextInt(100));
		}
		
		public void process(){
			for(int i = 0; i < 1000; i++){
				stageOne();
				stageTwo();
			}
		}
	}
	
	
	public class WorkerSync {

		private Random random = new Random();
		private List<Integer> list3 = new ArrayList<Integer>();
		private List<Integer> list4 = new ArrayList<Integer>();
		
		//Synchronized => Enquire the monitor log => Slow process 
		public synchronized void stageOne() {
			try {
				Thread.sleep(1);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			list3.add(random.nextInt(100));
		}

		public synchronized void stageTwo() {
			try {
				Thread.sleep(1);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			list4.add(random.nextInt(100));
		}
		
		public void process(){
			for(int i = 0; i < 1000; i++){
				stageOne();
				stageTwo();
			}
		}
	}
	

	public class WorkerLock {
	
		private Random random = new Random();
		private Object lock1 = new Object();
		private Object lock2 = new Object();
		private List<Integer> list5 = new ArrayList<Integer>();
		private List<Integer> list6 = new ArrayList<Integer>();
		
		/*
		 * Multiple Locks: Use of Synchronized Code Blocks
		 * Run Concurently(Simultaneously)
		 */
		
		//Synchronized => Enquire the monitor log => Slow process 
		//Having Multiple Threads will slow down 
		// So.... use this method to ... make the process a little faster
		public void stageOne() {
			//Only 1 Thread @ a time -> Faster process
			synchronized(lock1){
				try {
					Thread.sleep(1);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				list5.add(random.nextInt(100));
			}
		}

		public synchronized void stageTwo() {
			//Only 1 Thread @ a time -> Faster process
			synchronized(lock2){
				try {
					Thread.sleep(1);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				list6.add(random.nextInt(100));
			}
		}
		
		public void process(){
			for(int i = 0; i < 1000; i++){
				stageOne();
				stageTwo();
			}
		}
	}
	
	
	public static void main(String[] args) {
		
		synchronisedBlocks ob = new synchronisedBlocks();
		synchronisedBlocks.WorkerNonSync obj = ob.new WorkerNonSync();
		System.out.println("Starting ....");
		long start = System.currentTimeMillis();
		obj.process();
		long end = System.currentTimeMillis();
		
		System.out.println("Time take: " + (end-start) + " ms");
		System.out.println("List 1 Length: " + obj.list1.size() +
				"; List 2 Length: " + obj.list2.size());
		
		synchronisedBlocks.WorkerSync obj2 = ob.new WorkerSync();
		
		System.out.println("***************************");
		
		start = System.currentTimeMillis();
		
		Thread t1 = new Thread(new Runnable() {
			@Override
			public void run() {
				obj2.process();
			}
		});
		
		Thread t2 = new Thread(()->obj2.process() );
		
		t1.start();
		t2.start();
		
		try {
			t1.join();
			t2.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		end = System.currentTimeMillis();
		System.out.println("Time take: " + (end-start) + " ms");
		System.out.println("List 1 Length: " + obj2.list3.size() +
				"; List 2 Length: " + obj2.list4.size());
		
		
		System.out.println("***************************");

		synchronisedBlocks.WorkerLock obj3 = ob.new WorkerLock();
		start = System.currentTimeMillis();
		
		Thread t5 = new Thread(new Runnable() {
			@Override
			public void run() {
				obj3.process();
			}
		});
		
		Thread t6 = new Thread(()->obj3.process() );
		
		t5.start();
		t6.start();
		
		try {
			t5.join();
			t6.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		end = System.currentTimeMillis();
		System.out.println("Time take: " + (end-start) + " ms");
		System.out.println("List 1 Length: " + obj3.list5.size() +
				"; List 2 Length: " + obj3.list5.size());
		
	}
}
//# *******NOTES************
/*
The primary reason the second implementation using locks (WorkerLock) may appear faster is due to the use of multiple locks (lock1 and lock2) 
for the two stages (stageOne and stageTwo). This allows these stages to be executed concurrently by different threads, potentially improving overall
performance compared to the synchronized methods in the WorkerSync class.

In the first implementation (WorkerSync), both stageOne and stageTwo are declared as synchronized methods, which means only one thread can 
execute these methods at a time. This ensures thread safety but may result in slower performance, especially when multiple threads are contending 
for the monitor lock.

In the second implementation (WorkerLock), by using separate locks for the two stages, multiple threads can execute these stages concurrently.
 This can lead to better utilization of CPU resources and potentially improved performance, especially in scenarios where the two stages do not s
 hare critical resources that require exclusive access.

However, it's important to note that the actual performance benefits of using multiple locks depend on the nature of the workload, the number of 
available CPU cores, and other factors. In some cases, the overhead of managing multiple locks might offset the potential concurrency gains. 
It's always recommended to measure and profile the performance of different implementations under realistic conditions to make informed decisions 
about synchronization strategies.


When using the synchronized keyword in Java, the behavior depends on whether you synchronize the entire method or use synchronized blocks with different locks.

1. Synchronized Methods:
If you declare a method as synchronized, it locks the entire object (this in the case of an instance method or the class object in the case of a static method) when any thread enters the method.
This means that while one thread is executing a synchronized method, no other thread can execute any other synchronized method on the same object.
This can lead to a situation where the object is effectively locked, preventing other threads from executing even unrelated synchronized methods.
Example:

java
Copy code
public synchronized void methodA() {
    // Thread 1 is here, holding the lock on the entire object
}

public synchronized void methodB() {
    // Thread 2 cannot enter this method until Thread 1 releases the lock on the object
}
In this case, both methodA() and methodB() are synchronized on the same object lock, so only one thread can execute either method at a time.

2. Synchronized Blocks with Different Locks:
In contrast, if you use synchronized blocks with different locks (like lock1 and lock2 in your example), each block can be locked independently. This allows multiple threads to execute different synchronized blocks simultaneously, as long as they are using different locks.
This approach does not block the entire object, allowing greater concurrency.
Example:

java
Copy code
private Object lock1 = new Object();
private Object lock2 = new Object();

public void methodA() {
    synchronized(lock1) {
        // Thread 1 can hold lock1 and execute this block
    }
}

public void methodB() {
    synchronized(lock2) {
        // Meanwhile, Thread 2 can hold lock2 and execute this block concurrently
    }
}
In this example, methodA() and methodB() can be executed concurrently by different threads because they synchronize on different locks (lock1 and lock2). This avoids the problem of locking the entire object.

Why Synchronized Blocks Are Faster:
Less Contention: By using synchronized blocks with different locks, you reduce contention between threads.
 Only the specific critical sections are locked, not the entire method or object, allowing other threads to proceed with different tasks concurrently.

More Granular Control: Synchronized blocks allow you to precisely control which parts of the code are locked,
 minimizing the time that locks are held and improving overall performance.

Summary:
If you synchronize the entire method or use a single lock for multiple methods, the entire object is locked for other threads, 
which can cause significant delays. However, by using synchronized blocks with different locks, you can allow different parts of the code to 
run concurrently, making the application more efficient and reducing the time taken by the operations.







*/
