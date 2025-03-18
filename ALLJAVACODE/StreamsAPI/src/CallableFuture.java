import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.Random;

public class CallableFuture {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		ExecutorService executor = Executors.newCachedThreadPool();
		
		//Callable & Future
				Future<Integer> future = executor.submit(new Callable<Integer>() {

					@Override
					public Integer call() throws Exception {
						Random random = new Random();
						int duration = random.nextInt(4000);
						
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
					System.out.println("Result: " + future.get());
				} catch (InterruptedException e) {
					e.printStackTrace();
				} catch (ExecutionException e) {
					e.printStackTrace();
				}
			}//ENDof Main()

}

/*
 * 
 Callable and Runnable are two interfaces in Java used for representing tasks that can be executed concurrently by threads. They are often used in multithreading and concurrent programming to run code asynchronously.

Runnable
Runnable is a functional interface with a single method, run().
It is designed to be implemented by any class whose instances are intended to be executed by a thread.
The run() method does not return any result and cannot throw checked exceptions.
Key Points:
No return value: run() method has a void return type.
Cannot throw checked exceptions.
Introduced in Java 1.0.
Example:
java
Copy code
class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Runnable is running.");
    }
}

// Usage
Thread thread = new Thread(new MyRunnable());
thread.start();
Callable
Callable is a generic interface with a single method, call().
It is similar to Runnable but is designed to return a result and can throw a checked exception.
The call() method returns a result of a type specified by a generic parameter.
Key Points:
Returns a value: call() method returns a value of type T.
Can throw checked exceptions.
Introduced in Java 5 as part of the java.util.concurrent package.
Example:
java
Copy code
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

class MyCallable implements Callable<String> {
    @Override
    public String call() throws Exception {
        return "Callable result";
    }
}

// Usage
ExecutorService executorService = Executors.newSingleThreadExecutor();
Future<String> future = executorService.submit(new MyCallable());
try {
    String result = future.get();  // Blocking call to get the result
    System.out.println(result);
} catch (InterruptedException | ExecutionException e) {
    e.printStackTrace();
}
executorService.shutdown();
Key Differences Between Runnable and Callable:
Feature	Runnable	Callable
Return Type	void	Generic type T
Exception Handling	Cannot throw checked exceptions	Can throw checked exceptions
Method to Implement	run()	call()
Package	java.lang	java.util.concurrent
Result Retrieval	No direct result	Can retrieve the result using Future.get()
Usage Scenarios
Runnable: Use when you don't need to return a result or handle checked exceptions. It is simple and lightweight.
Callable: Use when you need to return a result after the task completes or if you want to handle checked exceptions.
Would you like to see more examples or have any specific questions about these interfaces?





 */

