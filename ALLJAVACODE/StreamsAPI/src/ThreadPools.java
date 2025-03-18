import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

/*
 * Thread Pools => Managing Lock Threads @ same time 
 * Thread Pools => Is like how many numbers of worker in your factory
 * Run Concurently(Simultaneously)
 */

class Processor implements Runnable{
	private int id;
	public Processor(int id){
		this.id = id;
	}
	@Override
	public void run() {		
		System.out.println("Starting: " + id);
		try {
			Thread.sleep(2000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println("Completed: " + id);
	}
	
}

public class ThreadPools {
	
	
	public static void main(String[] args) {
		//Thread Pool
		ExecutorService executor = Executors.newFixedThreadPool(2);
		
		for(int i = 0; i < 5; i++){
			executor.submit(new Processor( (i+1) )); //Assign task to the Thread(Worker
		}
		
		executor.shutdown(); //Will shutdown After the task is Completed
		
		System.out.println("All Task Submitted!");
		try {
			executor.awaitTermination(1, TimeUnit.DAYS); //Wait for 1 Day then ONLY terminate
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		System.out.println("All Task Completed!");
	}//ENDof Main

}
