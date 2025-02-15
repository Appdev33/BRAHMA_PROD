import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.Random;

public class ExecutorsBasic {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ExecutorService executor = Executors.newCachedThreadPool();
		
		executor.submit(new Runnable() {

			@Override
			public void run() {
				// TODO Auto-generated method stub
				Random random = new Random();
				int duration = random.nextInt(4000);
				
				System.out.println("Starting....");
				try {
					Thread.sleep(duration);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				
				System.out.println("Finish....");
			}
		});
		executor.shutdown();
	}

}
