import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class Processora implements Runnable{
	private CountDownLatch latch;
	
	public Processora(CountDownLatch latch){
		this.latch = latch;
	}
	@Override
	public void run() {	
		System.out.println("Started...");
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		latch.countDown(); //count = count-1
	}//ENDof RUN
	
}


public class CountDownLatches {
	
	
	public static void main(String[] args) {
		//Wait Till the latch reach 0 ==> Then only proceed 
		CountDownLatch latch = new CountDownLatch(3);
		
		ExecutorService executor = Executors.newFixedThreadPool(3);
		
		for (int i = 0; i < 3 ; i++){
			executor.submit(new Processora(latch));
		}
		
		try {
			latch.await(); //Waits until countDown() reached 0
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		System.out.println("Completed....");
	}//ENDof Main
}

