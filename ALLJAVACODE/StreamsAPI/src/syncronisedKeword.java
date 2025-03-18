
public class syncronisedKeword {

		private int count = 0;
		
		public static void main(String[] args) {
			syncronisedKeword app = new syncronisedKeword();
			app.doWork();
		}//ENDof Main
		
		//
		//Use SYNCHRONIZED ///////////////
		public synchronized void increment(){
			count++;
		}
		public void doWork(){
			Thread thread1 = new Thread(new Runnable(){

				@Override
				public void run() {
					for (int i = 0; i < 10000; i++){
						increment();
					}
				}
				
			});
			
			Thread thread2 = new Thread(new Runnable(){

				@Override
				public void run() {
					for (int i = 0; i < 10000; i++){
						increment();
					}
				}
				
			});
			
			thread1.start();
			thread2.start();
			
			//Wait for the thread to Finish 
			try {
				thread1.join();
				thread2.join();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			System.out.println("Count is " + count);
		}//ENDof doWork()
	}
/*
The synchronized version of the program is slower than the single-threaded version because of the overhead associated with synchronization. Here's why:

1. Context Switching:
In a multithreaded environment, the CPU must switch between threads. Each context switch has some overhead, even if the tasks are simple.
When multiple threads are running, the CPU spends some time switching between these threads, which slows down the overall execution.

2. Locking Overhead:
The synchronized keyword causes the thread to acquire a lock before entering the increment() method and release it after exiting. 
Acquiring and releasing locks introduces additional overhead, as the JVM needs to manage these locks to ensure thread safety.

3. Sequential Execution Due to Locking:
Although there are multiple threads, they can't execute the increment() method in parallel because of the lock on the method. 
Only one thread can increment the count variable at a time, effectively making the increment() method run sequentially, 
which can negate the potential speedup from multithreading.

4. Potential for Thread Contention:
If many threads are trying to access the synchronized method, they might end up waiting for each other, leading to contention. 
This waiting time can add up, further slowing down the overall execution.

5. Cache Coherency:
When multiple threads update a shared variable, the CPU caches need to stay coherent across cores.
This requires extra work to ensure that all cores see the latest value of count, which introduces additional latency.
Comparison to Single-Threaded Execution:
In the single-threaded version (from your first example), there's no need for locks, context switching, or dealing with cache coherence issues. 
The operations run sequentially without any overhead, making it faster than the synchronized, multithreaded version.

Summary:
Multithreading can potentially speed up a program if the tasks are independent and can be executed in parallel without needing 
to synchronize access to shared resources. However, in cases like this where synchronization is required to prevent data corruption, 
the overhead introduced by synchronization can actually make the program slower than a single-threaded implementation.
*/