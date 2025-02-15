import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.Random;
import java.io.IOException;


public class CallableException {

	public static void main(String[] args) {
		ExecutorService executor = Executors.newCachedThreadPool();
		
		//Callable & Future
		Future<Integer> future = executor.submit(new Callable<Integer>() {

			@Override
			public Integer call() throws Exception {
				Random random = new Random();
				int duration = random.nextInt(4000);
				
				if (duration > 2000){
					throw new IOException("Sleeping for too long");
				}
				System.out.println("Starting....");
				try {
					Thread.sleep(duration);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				
				System.out.println("Finish....");
				
				return duration;
			}
			
		});
		
		executor.shutdown();
		try {
			//Future.get()
			//Throws CancellationException
			//Throws InterruptedException 
			//Throws ExecutionException 
			System.out.println("Result: " + future.get()); 
		} catch (InterruptedException e) {
			e.printStackTrace();
		} catch (ExecutionException e) {
			//IOException ex = (IOException) e.getCause();
			//System.out.println(ex.getMessage());   // "Sleeping for too long"
			System.out.println(e.getMessage());;
		}
	}//ENDof Main()

}
