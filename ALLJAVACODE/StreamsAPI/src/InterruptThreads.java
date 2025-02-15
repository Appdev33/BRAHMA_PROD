import java.util.Random;

/*
 * Interrupting Threads
 */
public class InterruptThreads {

	public static void main(String[] args) throws InterruptedException {
		System.out.println("Starting...");
		
		Thread t1 = new Thread(new Runnable() {

			@Override
			public void run() {
				Random random = new Random();
				
				// 1E10 => 1 x (10 ^ 6)
				for(int i = 0; i < 1E8; i++){
					
					//Check if is being interrupted
					if ( Thread.currentThread().isInterrupted() ){
						System.out.println("Interrupted!!!");
						break;
					}
					
					/*try{
						Thread.sleep(1);
					}catch(InterruptedException e){
						System.out.println("Interrupted!!!");
						break;
					}*/
					Math.sin(random.nextDouble());
				}
			}
			
		});
		
		t1.start();
		
		Thread.sleep(500);
		//Set Flag tells that it is being interrupted
		//Does not terminate 
		t1.interrupt(); 
		
		t1.join();
		
		System.out.println("Finished...");
	}//ENDof Main()

}

