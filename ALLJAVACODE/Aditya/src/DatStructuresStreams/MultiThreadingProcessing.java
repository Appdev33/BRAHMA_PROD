package DatStructuresStreams;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Callable;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.Future;
import java.util.concurrent.RecursiveTask;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;
import java.util.stream.IntStream;

class AlphabetRunner implements Runnable{

	@Override
	public void run() {
		// TODO Auto-generated method stub
		IntStream.rangeClosed('A','D')
		.mapToObj(c->(char)c)
		.forEach(i->{
			System.out.println(i);
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
				Thread.currentThread().interrupt();
                System.out.println("Number thread interrupted");
			}	
		});
		
	}
}

class NumberRunner implements Runnable{

	@Override
	public void run() {
		// TODO Auto-generated method stub
		IntStream.rangeClosed(1,3).
		forEach(i->{
			System.out.println(i);
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
				Thread.currentThread().interrupt();
                System.out.println("Number thread interrupted");
			}	
		});
	}
}


// Thread Syncronisation using keyword

class Counter {
	
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}


class CounterTask implements Runnable {
    private final Counter counter;

    public CounterTask(Counter counter) {
        this.counter = counter;
    }

    @Override
    public void run() {
        String threadName = Thread.currentThread().getName();
        for (int i = 0; i < 100; i++) {
            counter.increment();
            // Print thread name and current count
            System.out.println("Thread " + threadName + " incremented count to: " + counter.getCount());
        }
    }
}

// ################# Using Executor Service #################

class Task implements Runnable {
    private final int taskId;

    public Task(int taskId) {
        this.taskId = taskId;
    }

    @Override
    public void run() {
        System.out.println("Executing Task " + taskId);
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

// #################Using Callable Service #################
class calableTask implements Callable<Integer>{
	
	private final List<Integer> numbers;
	
	public calableTask(List<Integer> numbers) {
		this.numbers = numbers;
	}
	
	@Override
	public Integer call() throws Exception {
		Thread.sleep(1000);
		return numbers.stream().reduce((a,b)->a>b?b:a).get();
	}
}

//#################Parallel Processing ForkJoin Pool #################

class SumTask extends RecursiveTask<Integer> {
    private final int[] array;
    private final int start, end;

    public SumTask(int[] array, int start, int end) {
        this.array = array;
        this.start = start;
        this.end = end;
    }

    protected Integer compute() {
        if (end - start <= 2) {
            int sum = 0;
            for (int i = start; i < end; i++) sum += array[i];
            return sum;
        }
        int mid = (start + end) / 2;
        SumTask leftTask = new SumTask(array, start, mid);
        SumTask rightTask = new SumTask(array, mid, end);
        leftTask.fork();
        return rightTask.compute() + leftTask.join();
    }
}

//#################Parallel Processing ForkJoin Pool #################

class AsyncTask implements Runnable {
    private final int taskId;

    public AsyncTask(int taskId) {
        this.taskId = taskId;
    }

    @Override
    public void run() {
        System.out.println("Executing Task " + taskId + " in: " + Thread.currentThread().getName());
        try {
            Thread.sleep(1000); // Simulate some work
        } catch (InterruptedException e) {
            System.err.println("Task " + taskId + " was interrupted.");
        }
        System.out.println("Task " + taskId + " completed.");
    }
}


 class ForkJoinSum extends RecursiveTask<Long> {

    private static final int THRESHOLD = 10; // Threshold for splitting tasks
    private final int[] numbers;
    private final int start;
    private final int end;

    // Constructor
    public ForkJoinSum(int[] numbers, int start, int end) {
        this.numbers = numbers;
        this.start = start;
        this.end = end;
    }

    @Override
    protected Long compute() {
        int length = end - start;
        
        if (length <= THRESHOLD) {
            // Compute directly if task is small enough
            return computeDirectly();
        }

        // Split task
        int middle = start + (length / 2);
        ForkJoinSum leftTask = new ForkJoinSum(numbers, start, middle);
        ForkJoinSum rightTask = new ForkJoinSum(numbers, middle, end);

        // Fork subtasks
        leftTask.fork();
        long rightResult = rightTask.compute();
        long leftResult = leftTask.join();

        // Combine results
        return leftResult + rightResult;
    }

    private long computeDirectly() {
        long sum = 0;
        for (int i = start; i < end; i++) {
            sum += numbers[i];
        }
        return sum;
    }
}

// System.out.println("################# Multithreading with Java Streams (Parallel Streams)  ###########################");
 
 class Producer implements Runnable {
	    private BlockingQueue<Integer> queue;

	    public Producer(BlockingQueue<Integer> queue) {
	        this.queue = queue;
	    }

	    public void run() {
	        try {
	            for (int i = 0; i < 5; i++) {
	                queue.put(i);
	                System.out.println("Produced: " + i);
	                Thread.sleep(1000);
	            }
	        } catch (InterruptedException e) {
	            Thread.currentThread().interrupt();
	        }
	    }
	}

	class Consumer implements Runnable {
	    private BlockingQueue<Integer> queue;

	    public Consumer(BlockingQueue<Integer> queue) {
	        this.queue = queue;
	    }

	    public void run() {
	        try {
	            while (true) {
	                Integer item = queue.take();
	                System.out.println("Consumed: " + item);
	                Thread.sleep(1500);
	            }
	        } catch (InterruptedException e) {
	            Thread.currentThread().interrupt();
	        }
	    }
	}

 
 
// System.out.println("################# Thread Syncronisation using keyword  ###########################");
 
 
 

public class MultiThreadingProcessing {

	public static void main(String[] args) throws InterruptedException, ExecutionException {
		// TODO Auto-generated method stub
		Thread th1 = new Thread(new NumberRunner()); 
		Thread th2 = new Thread(new AlphabetRunner());
		
		th1.start();
		th2.start();
		
		try {
			th1.join();
			th2.join();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		System.out.println("Practicing thread for multithreading....");
		
		
		System.out.println("################# Thread Syncronisation using keyword  ###########################");
		Counter counter = new Counter();
		Thread[] threads = java.util.stream.Stream
	            .of(new Thread(new CounterTask(counter), "Thread-1"),
	                 new Thread(new CounterTask(counter), "Thread-2"))
	            .peek(Thread::start) // Start each thread
	            .toArray(Thread[]::new);

	        // Join threads to ensure completion
	        for (Thread thread : threads) {
	            try {
					thread.join();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	        }

	        System.out.println("Final count: " + counter.getCount());
	        
	     // Using Executor Service
	        System.out.println("#################Using Executor Service###########################");
	        ExecutorService executor = Executors.newFixedThreadPool(3);
	        ExecutorService executor2 = Executors.newFixedThreadPool(3);
	        
	        for(int i=1; i<=5; i++) {
	        	final int taskId = i;
	        	
	        	executor.submit(()->{
	        		System.out.println(Thread.currentThread());
	        		try {
						Thread.sleep(1000);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}finally {
						executor.shutdown();
					}
	        	});
	        }
	        
	        for (int i = 1; i <= 5; i++) {
	            Task task = new Task(i); // Create a new Task instance for each task
	            executor.submit(task);
	        }
	        
	        List<Integer> al = Arrays.asList(4,5,7,9,11,34);
	        
	        // Using Callable Service
	        Callable<Integer> task1 = new calableTask(al);
	        
	        Future<Integer> future = executor2.submit(task1);
	        
	        try {
	            // Wait for future to complete and store the result
	            Integer result = future.get();  // This blocks until the task is completed
	            System.out.println("Result from Callable task: " + result);
	        } catch (InterruptedException | ExecutionException e) {
	            e.printStackTrace();
	        } finally {
	            // Shutdown the ExecutorService after completion
	            executor.shutdown();
	        }
	        

	        
	      //#################Parallel Processing ForkJoin Pool #################
//	        Using ForkJoinPool for divide-and-conquer algorithms.
	        
	        ForkJoinPool pool = new ForkJoinPool();
	        int[] array = {1, 2, 3, 4, 5, 6};
	        SumTask task = new SumTask(array, 0, array.length);
	        System.out.println("Sum: " + pool.invoke(task));
	        
//	        ###################  CompletableFuture for Asynchronous Tasks ################	        
//	        Handling async tasks with CompletableFuture.
	     // Create and run multiple tasks asynchronously
	        
	        System.out.println("############################## CompletableFuture for Asynchronous Tasks ");
	        
	        CompletableFuture<Void> task11 = CompletableFuture.runAsync(new AsyncTask(1));
	        CompletableFuture<Void> task2 = CompletableFuture.runAsync(new AsyncTask(2));
	        CompletableFuture<Void> task3 = CompletableFuture.runAsync(new AsyncTask(3));

	        // Handle completion of each task individually
	        task11.thenRun(() -> System.out.println("Task 1 finished successfully."));
	        task2.thenRun(() -> System.out.println("Task 2 finished successfully."));
	        task3.thenRun(() -> System.out.println("Task 3 finished successfully."));

	        // Combine tasks to execute when all are completed
	        CompletableFuture<Void> allTasks = CompletableFuture.allOf(task11, task2, task3);
	        allTasks.thenRun(() -> System.out.println("All tasks completed."));

	        // Wait for all tasks to complete (optional)
	        allTasks.join();  // This will block until all tasks complete
	        
	        System.out.println("############################## Fork Join Pool ");
	        int[] numbers = new int[100];
	        for (int i = 0; i < numbers.length; i++) {
	            numbers[i] = i + 1; // Fill array with numbers 1 to 100
	        }

	        // Create ForkJoinPool
	        ForkJoinPool pool2 = new ForkJoinPool();
	        // Create initial task
	        ForkJoinSum task12 = new ForkJoinSum(numbers, 0, numbers.length);

	        // Start parallel computation
	        long result = pool.invoke(task12);
	        System.out.println("Sum: " + result); // Should print 5050
	        

	        System.out.println("############################## Creating Scheduled Tasks with ScheduledExecutorService");
	        ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(2);

	        // Task 1: Periodic task
	        Runnable periodicTask = () -> {
	            System.out.println("Periodic Task executed at: " + java.time.LocalTime.now());
	        };

	        // Schedule the periodic task to run every 2 seconds
	        ScheduledFuture<?> periodicTaskHandle = scheduler.scheduleAtFixedRate(periodicTask, 0, 2, TimeUnit.SECONDS);

	        // Task 2: Dynamic controller task
	        Runnable dynamicTask = new Runnable() {
	            private int executionCount = 0;

	            @Override
	            public void run() {
	                executionCount++;
	                System.out.println("Dynamic Task executed at: " + java.time.LocalTime.now());

	                // Stop the periodic task after 5 executions
	                if (executionCount == 5) {
	                    System.out.println("Stopping periodic task...");
	                    periodicTaskHandle.cancel(false);
	                }

	                // Shut down the scheduler after 10 executions of the dynamic task
	                if (executionCount == 10) {
	                    System.out.println("Shutting down the scheduler...");
	                    scheduler.shutdown();
	                }
	            }
	        };

	        // Schedule the dynamic task to run every 1 second
	        scheduler.scheduleWithFixedDelay(dynamicTask, 0, 1, TimeUnit.SECONDS);

	        // Ensure the program shuts down gracefully
	        try {
	            scheduler.awaitTermination(10, TimeUnit.SECONDS);
	        } catch (InterruptedException e) {
	            e.printStackTrace();
	        }

	        System.out.println("Scheduler terminated.");
	        System.out.println("################# Using BlockingQueue for Thread Communication  ###########################");
	        
	        BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(3);
	        new Thread(new Producer(queue)).start();
	        new Thread(new Consumer(queue)).start();
	        
	        
	        System.out.println("################# Multithreading with Java Streams (Parallel Streams)  ###########################");
	        
	        
	        int sum = IntStream.range(1, 100)
                    .parallel()
                    .sum();
	        System.out.println("Sum: " + sum);
	        
	        
	}
}
