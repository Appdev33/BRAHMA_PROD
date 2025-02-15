
public class stopThreadWithVolatile {

	public static void main(String[] args) {
        MyRunnable myRunnable = new MyRunnable();
        Thread thread = new Thread(myRunnable);

        // Start the thread
        thread.start();

        // Allow the thread to run for some time
        try {
            Thread.sleep(5000);
            System.out.println("Stoppinf thread in 5");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Stop the thread
        myRunnable.stopThread();

        // Optionally, wait for the thread to finish
        try {
            thread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Main thread exiting.");
    }
}

class MyRunnable implements Runnable {
    private volatile boolean keepRunning = true;

    @Override
    public void run() {
        while (keepRunning) {
            // Your task logic here

            try {
                // Add a sleep or some other mechanism to avoid busy-waiting
                Thread.sleep(2000);
                System.out.println("Avoid busy waiting");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                // Handle interruption if needed
            }
        }

        System.out.println("MyRunnable thread exiting.");
    }

    public void stopThread() {
        keepRunning = false;
    }

}
