
//https://gist.github.com/yclim95/821d7059767dfc098eaa6698490bb1a0
	
public class Practice {

private int count = 0;
	
	public static void main(String[] args) {
		Practice app = new Practice();
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