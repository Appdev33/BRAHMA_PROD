import java.util.Scanner;
/*
 * wait() tells the calling thread to give up the monitor and go to sleep until some other thread enters the same monitor and calls notify( ).
 * notify() wakes up the first thread that called wait() on the same object.
 */

public class WaitNotify {
	
	public void produce() throws InterruptedException{
		
		synchronized(this) { //On the Procesor Object
			System.out.println("Producer thread running...");
			wait(); //Only can be called inside Synchronize block 
			System.out.println("Resumed...");
		}
		
	}//EndOf Produce()
	
	public void consume() throws InterruptedException{
		Scanner scanner = new Scanner(System.in); 
		Thread.sleep(2000);
		synchronized(this) { //On the Procesor Object
			System.out.println("Waiting for return key...");
			scanner.nextLine();
			System.out.println("Return key pressed");
			notify(); //Notify the wait() object
			Thread.sleep(5000);
		}
		scanner.close();
	}//EndOf Consume()

}