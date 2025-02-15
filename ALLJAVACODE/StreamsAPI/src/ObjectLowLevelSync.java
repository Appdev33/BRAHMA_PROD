

import java.util.LinkedList;
import java.util.Random;


/*
 * Low Level Synchronization (Example) 
 * Run Concurently(Simultaneously)
 */

public class ObjectLowLevelSync {
	
	
	
	public class Processor {
		private LinkedList <Integer> list = new LinkedList<Integer>();
		private final int LIMIT = 10;
		private Object lock = new Object(); //LockOn 
		
		public void produce() throws InterruptedException{
			int value = 0;
			
			while(true){ //Infinite Loop
				synchronized(lock){
					while(list.size() == LIMIT){
						//wait until the current thread invoke notify()
						System.out.println("Reached LIMIT");
						lock.wait();  //No1
					}
					list.add(value++);
					System.out.println("Adding"+value);
					lock.notify(); // Will wake up the consume() @ No2
				}
			}
			
		}//Endof Produce()
		
		public void consume() throws InterruptedException{
			Random random = new Random();
			
			while(true){
				synchronized(lock){
					
					while(list.size() == 0){
						lock.wait(); //No2
						System.out.println("List Size"+list.size());
					}
					System.out.print("List size: " + list.size());
					
					int value = 0;
//					for(int i=0;i<10; i++) {
					value = list.removeFirst();
					System.out.println(";Consume value: " + value);
//					}
					lock.notify(); // Will wake up thread @ No1
					
				}//EndOf Synchronized()
				
				Thread.sleep(random.nextInt(1000)); //0-999
			}//Endof While
			
		}//Endof Consume()
	}
	
	
	
	
	public static void main(String[] args) throws InterruptedException {
		
		ObjectLowLevelSync obj = new ObjectLowLevelSync();
		ObjectLowLevelSync.Processor processor = obj.new Processor();
//		final Processor processor = new Processor();
		Thread t1 = new Thread(new Runnable(){

			@Override
			public void run() {
				try {
					processor.produce();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
			
		});
		
		Thread t2 = new Thread(new Runnable(){

			@Override
			public void run() {
				try {
					processor.consume();
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
	}//ENDof Main
	
}

/*
Producer (produce method):

The produce method runs in an infinite loop, continually producing items.
It enters a synchronized block using the lock object to ensure exclusive access.
Inside the synchronized block, it checks if the buffer (list) is at its maximum capacity (LIMIT). If so, it waits (lock.wait()), releasing the lock and allowing 
the consumer to consume items until there is space.
Once there is space in the buffer, it adds a new item to the list, increments the value, and notifies any waiting threads (specifically the consumer) that there 
is an item to consume (lock.notify()).
Consumer (consume method):

The consume method also runs in an infinite loop, continually consuming items.
It enters a synchronized block using the lock object.
Inside the synchronized block, it checks if the buffer is empty. If so, it waits (lock.wait()), releasing the lock and allowing the producer to produce items until 
there is something to consume.
Once there is an item in the buffer, it prints the size of the list, removes the first item, prints its value, and notifies any waiting threads (specifically the producer) 
that there is space in the buffer (lock.notify()).
After processing an item, the consumer introduces a random delay using Thread.sleep(random.nextInt(1000)) to simulate variable processing time.
*/

