

import java.util.Scanner;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/*
 * Re-entrants Locks
 * Run Concurently(Simultaneously)
 */

public class ReEntrantLocks {
	
	public class Runner {
		private int count = 0;
		private Lock lock = new ReentrantLock(); //Alternative to Synchronized
		private Condition condition = lock.newCondition();
		
		private void increment(){
			for (int i = 0; i < 1000; i++){
				count++;
			}
		}
		
		public void firstThread() throws InterruptedException{
			lock.lock();
			
			System.out.println("Waiting...");
			condition.await();  //Wait until signal() is invoked (No1)
			
			System.out.println("Woken Up!");
			try {
				increment(); //Use try-catch => prevent Exception 
			} catch (Exception e) {
				e.printStackTrace();
			}finally{
				lock.unlock();
			}
			
		}
		
		public void secondThread() throws InterruptedException{
			Thread.sleep(1000);
			lock.lock();
			
			System.out.println("Press The return key!");
			new Scanner(System.in).nextLine();
			System.out.println("Got return key!");
			
			condition.signal(); //No1
			try {
				increment(); //Use try-catch => prevent Exception 
			} catch (Exception e) {
				e.printStackTrace();
			}finally{
				lock.unlock();
			}
		}
		
		public void finished(){
			System.out.println("Count: " + count);
		}
	}
	
	
	public static void main(String[] args) throws InterruptedException {
		ReEntrantLocks obj = new ReEntrantLocks();
		final ReEntrantLocks.Runner runner = obj.new Runner();
		Thread t1 = new Thread(new Runnable(){

			@Override
			public void run() {
				try {
					runner.firstThread();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
			
		});
		
		Thread t2 = new Thread(new Runnable(){

			@Override
			public void run() {
				try {
					runner.secondThread();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
			
		});
		
		//Start
		t1.start();
		t2.start();
		
		t1.join();
		t2.join();
		
		runner.finished();
	}//ENDof Main
	
}


/*
This Java code demonstrates the use of the Lock and Condition interfaces to implement a simple synchronization mechanism between two threads. 
The Lock interface provides an alternative to the traditional synchronized keyword for controlling access to critical sections, and the Condition 
interface allows threads to await and signal each other.

Here's a breakdown of the code:

Instance Variables:

count: An integer variable that will be incremented by both threads.
lock: An instance of ReentrantLock (a type of Lock) used for synchronization.
condition: An instance of Condition associated with the lock.

Method increment:
A private method that increments the count variable in a loop. This method will be called by both threads.

Method firstThread:
Acquires the lock using lock.lock().
Prints "Waiting..." and then calls condition.await(). This releases the lock and puts the thread in a waiting state until another 
thread signals it using condition.signal().
When the thread is awakened (signaled), it prints "Woken Up!", increments the count, and releases the lock using lock.unlock() in a 
finally block to ensure proper cleanup.
Method secondThread:

Sleeps for 1000 milliseconds to simulate some processing.
Acquires the lock using lock.lock().
Prints a message, waits for the user to press the return key, and then prints "Got return key!"
Calls condition.signal() to signal the waiting thread (the one in firstThread) to wake up.
Increments the count and releases the lock using lock.unlock() in a finally block.
Method finished:

Prints the final value of the count variable.
In summary, this code demonstrates inter-thread communication using a Lock and Condition. The firstThread method waits for a signal 
from secondThread before proceeding, and the secondThread method signals the waiting thread after a certain condition is met. The use of
 ReentrantLock provides a more flexible and explicit way of managing synchronization compared to the traditional synchronized keyword.
*/




/*
The provided code is an example of inter-thread communication using the wait() and notify() mechanism with a basic synchronization approach using
 the synchronized keyword. In contrast, the ReentrantLock and Condition approach provides a more explicit and flexible way of achieving the same result.
  Here are the key differences:

Using synchronized and wait()/notify():
Locking Mechanism:

synchronized: The synchronized keyword is used for locking. It automatically acquires and releases the lock associated with the specified object.
ReentrantLock: The ReentrantLock is an explicit lock provided by the java.util.concurrent.locks package. You manually acquire and release the lock using 
the lock() and unlock() methods.
Waiting and Signaling:

synchronized: The wait() and notify() methods are used for waiting and signaling. Threads must be in a synchronized block to call these methods.
ReentrantLock and Condition: The await() and signal() methods are used for waiting and signaling in conjunction with a Condition object. This provides
 more control and expressiveness compared to wait() and notify().
Flexibility:

synchronized: Simpler and easier to use but less flexible. Limited features compared to ReentrantLock.
ReentrantLock: Offers more advanced features, such as interruptible locking, timed lock acquisition, and the ability to have multiple conditions associated with a single lock.
Explicitness:

synchronized: Implicit locking mechanism, which can be convenient but less explicit.
ReentrantLock: Requires explicit calls to lock() and unlock(), making the code more explicit and allowing finer control over locking.


In summary, the ReentrantLock and Condition approach provides more explicit control over locking, more advanced features, and a clearer separation of concerns. 
It can be especially beneficial in complex scenarios where fine-grained control over thread synchronization is required. However, for simpler use cases, 
the synchronized keyword with wait() and notify() might be sufficient and more straightforward.

*/