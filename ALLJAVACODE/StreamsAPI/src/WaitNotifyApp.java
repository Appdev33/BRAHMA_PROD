
public class WaitNotifyApp {
	
	public static void main(String[] args) throws InterruptedException{
		
		final WaitNotify processor = new WaitNotify();
		
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