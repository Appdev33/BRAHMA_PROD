import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.Random;
import java.util.Scanner;

public class ProducerConsumer {
	
	//Add/Remvoe item 
	private static BlockingQueue<Integer> queue = new ArrayBlockingQueue<Integer>(10);
	
	public static void main(String[] args) {
		Thread t1 = new Thread(new Runnable(){

			@Override
			public void run() {	
				try {
					producer();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		});
		
		Thread t2 = new Thread(new Runnable(){

			@Override
			public void run() {	
				try {
					consumer();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
			
		});
		
		//Start it 
		t1.start();
		t2.start();
		
		try {
			t1.join();
			t2.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}//ENDof Main
	
	private static void producer() throws InterruptedException{
		Random random = new Random();
		
		while(true){
			queue.put(random.nextInt(100)); //Range from 0-99
		}
	}//ENDof Producer()
	
	private static void consumer() throws InterruptedException{
		Random random = new Random();
		while(true){
			Thread.sleep(100);
			if (random.nextInt(10) == 0){
				Integer value = queue.take(); //Retrieve and remove the head value
				System.out.println("Taken value: " + value +
						"; Queue Size: " + queue.size());
			}
		}
	}//ENDof Consumer()
	
	/*
	 * wait() tells the calling thread to give up the monitor and go to sleep until some other thread enters the same monitor and calls notify( ).
	 * notify() wakes up the first thread that called wait() on the same object.
	 */
}