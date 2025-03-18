package DatStructuresStreams;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.Future;
import java.util.concurrent.Semaphore;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class CpuIoIntensiveTasks {
	
	// CPU-intensive task: Calculate factorial
    private static String cpuIntensiveTask(int n) {
        return "Factorial(" + n + ") Result Length: " + factorial(n).toString().length();
    }

    private static BigInteger factorial(int n) {
        BigInteger result = BigInteger.ONE;
        for (int i = 1; i <= n; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    }
    
 // I/O-bound task: Fetch data from a URL
    private static String ioTask(String url) {
        try {
            HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
            connection.setRequestMethod("GET");
            connection.setConnectTimeout(5000);
            connection.setReadTimeout(5000);

            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                StringBuilder response = new StringBuilder();
                String line;
                while ((line = reader.readLine()) != null) {
                    response.append(line);
                }
                return "Data from " + url + ": " + response.length() + " characters";
            }
        } catch (Exception e) {
            return "Error fetching " + url + ": " + e.getMessage();
        }
    }
    
    
 // Helper method to batch tasks and submit to the executor
    private static <T> List<CompletableFuture<String>> batchTasks(
            List<T> tasks, int batchSize, ExecutorService executorService, TaskProcessor<T> taskProcessor) {
        List<CompletableFuture<String>> futures = new ArrayList<>();
        for (int i = 0; i < tasks.size(); i += batchSize) {
            List<T> batch = tasks.subList(i, Math.min(i + batchSize, tasks.size()));
            futures.addAll(batch.stream()
                    .map(task -> CompletableFuture.supplyAsync(() -> taskProcessor.process(task), executorService))
                    .collect(Collectors.toList()));
        }
        return futures;
    }

    // Functional interface for processing tasks
    @FunctionalInterface
    private interface TaskProcessor<T> {
        String process(T task);
    }

	
	public static void main(String[] args) throws InterruptedException, ExecutionException {
		
		// CPU-intensive tasks
        List<Integer> cpuTasks = Arrays.asList(5000, 10000, 15000, 40000, 50000, 60000);

        // I/O-bound tasks
        List<String> ioTasks = Arrays.asList(
                "https://jsonplaceholder.typicode.com/posts",
                "https://jsonplaceholder.typicode.com/comments",
                "https://jsonplaceholder.typicode.com/comments",
                "https://jsonplaceholder.typicode.com/comments",
                "https://jsonplaceholder.typicode.com/comments",
                "https://jsonplaceholder.typicode.com/comments",
                "https://jsonplaceholder.typicode.com/comments"
        );

        long startTime = System.currentTimeMillis();

        // Execute CPU tasks sequentially
        for (int n : cpuTasks) {
            System.out.println(cpuIntensiveTask(n));
        }

        // Execute I/O tasks sequentially
        for (String url : ioTasks) {
            System.out.println(ioTask(url));
        }

        long endTime = System.currentTimeMillis();
        System.out.println("Total Time Taken: " + (endTime - startTime) + " ms");
        System.out.println("####################################################");
        
        
        //OPTIMISE BY MULTITHREADING
//        Here, we will use thread pools to execute CPU and I/O tasks concurrently.
     // CPU and I/O tasks
        List<Integer> cpuTasks2 = Arrays.asList(5000, 10000, 15000, 40000, 50000, 60000);

        // I/O-bound tasks
        List<String> ioTasks2 = Arrays.asList(
                "https://jsonplaceholder.typicode.com/posts",
                "https://jsonplaceholder.typicode.com/comments",
                "https://jsonplaceholder.typicode.com/comments",
                "https://jsonplaceholder.typicode.com/comments",
                "https://jsonplaceholder.typicode.com/comments",
                "https://jsonplaceholder.typicode.com/comments",
                "https://jsonplaceholder.typicode.com/comments"
        );
//        List<Integer> cpuTasks2 = Arrays.asList(5000, 10000, 15000);
//        List<String> ioTasks2 = Arrays.asList(
//                "https://jsonplaceholder.typicode.com/posts",
//                "https://jsonplaceholder.typicode.com/comments"
//        );

        ExecutorService cpuThreadPool = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        ExecutorService ioThreadPool = Executors.newCachedThreadPool();

        long startTime2 = System.currentTimeMillis();

        // Submit CPU tasks
        List<Future<String>> cpuFutures = new ArrayList<>();
        for (int n : cpuTasks2) {
            cpuFutures.add(cpuThreadPool.submit(() -> cpuIntensiveTask(n)));
        }

        // Submit I/O tasks
        List<Future<String>> ioFutures = new ArrayList<>();
        for (String url : ioTasks2) {
            ioFutures.add(ioThreadPool.submit(() -> ioTask(url)));
        }

        // Wait for CPU results
        for (Future<String> future : cpuFutures) {
            System.out.println(future.get());
        }

        // Wait for I/O results
        for (Future<String> future : ioFutures) {
            System.out.println(future.get());
        }

        long endTime2 = System.currentTimeMillis();
        System.out.println("Total Time Taken: " + (endTime2 - startTime2) + " ms");

        // Shutdown thread pools
        cpuThreadPool.shutdown();
        ioThreadPool.shutdown();
        System.out.println("####################################################");

//        Here, we’ll use CompletableFuture for non-blocking I/O tasks to further optimize the I/O operations.
        
        
        ExecutorService cpuThreadPool3 = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        ExecutorService ioThreadPool3 = Executors.newCachedThreadPool();

        long startTime3 = System.currentTimeMillis();

        // Submit CPU tasks
        List<CompletableFuture<String>> cpuFutures3 = cpuTasks.stream()
                .map(n -> CompletableFuture.supplyAsync(() -> cpuIntensiveTask(n), cpuThreadPool3))
                .collect(Collectors.toList());

        // Submit I/O tasks
        List<CompletableFuture<String>> ioFutures3 = ioTasks.stream()
                .map(url -> CompletableFuture.supplyAsync(() -> ioTask(url), ioThreadPool3))
                .collect(Collectors.toList());

        // Combine all futures
        List<CompletableFuture<String>> allTasks = new ArrayList<>();
        allTasks.addAll(cpuFutures3);
        allTasks.addAll(ioFutures3);

        // Wait for all tasks to complete
        CompletableFuture.allOf(allTasks.toArray(new CompletableFuture[0])).join();

        // Process results
        allTasks.forEach(future -> {
            try {
                System.out.println(future.get());
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        long endTime3 = System.currentTimeMillis();
        System.out.println("Total Time Taken: " + (endTime3 - startTime3) + " ms");

        cpuThreadPool3.shutdown();
        ioThreadPool3.shutdown();
        System.out.println("####################################################");
        
        
//        To further optimize the code, we can focus on several aspects:
//
//    	Task Batching: Instead of submitting all tasks at once, we can batch them into smaller chunks to avoid overwhelming the executor thread pools.
//    	Executor Initialization: We can reuse the same ExecutorService for both CPU-bound and I/O-bound tasks to minimize overhead.
//    	Task Cancellation Handling: Adding cancellation handling in case the tasks take too long or we need to handle timeouts.
        
        
        
     // Use a single thread pool for both CPU-bound and I/O-bound tasks
        ExecutorService executorService4 = Executors.newCachedThreadPool();

        // Batch processing: divide tasks into smaller batches for better resource management
        int batchSize = 5; // Set batch size according to your system resources
        List<CompletableFuture<String>> cpuFutures4 = batchTasks(cpuTasks, batchSize, executorService4, CpuIoIntensiveTasks::cpuIntensiveTask);
        List<CompletableFuture<String>> ioFutures4 = batchTasks(ioTasks, batchSize, executorService4, CpuIoIntensiveTasks::ioTask);

        // Combine all futures
        List<CompletableFuture<String>> allTasks4 = new ArrayList<>();
        allTasks.addAll(cpuFutures4);
        allTasks.addAll(ioFutures4);

        long startTime4 = System.currentTimeMillis();

        // Wait for all tasks to complete
        CompletableFuture.allOf(allTasks.toArray(new CompletableFuture[0])).join();

        // Process results
        allTasks.forEach(future -> {
            try {
                System.out.println(future.get());
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        long endTime4 = System.currentTimeMillis();
        System.out.println("Total Time Taken: " + (endTime4 - startTime4) + " ms");

        // Shutdown the executor gracefully
        executorService4.shutdown();
        System.out.println("####################################################");
        
        
        //Using streams API not useful increasing time only
        
     // Executor for CPU-bound tasks
        int numCpuThreads5 = Math.min(cpuTasks.size(), Runtime.getRuntime().availableProcessors());
        ExecutorService cpuExecutor5 = Executors.newFixedThreadPool(numCpuThreads5);

        // Executor for I/O-bound tasks (Async Executor)
        ExecutorService ioExecutor5 = Executors.newFixedThreadPool(10);  // Custom size for I/O-bound tasks

        long startTime5 = System.currentTimeMillis();

        // Parallel processing using streams for CPU-bound and I/O-bound tasks
        List<CompletableFuture<String>> cpuFutures5 = cpuTasks.parallelStream()
            .map(task -> CompletableFuture.supplyAsync(() -> cpuIntensiveTask(task), cpuExecutor5))
            .collect(Collectors.toList());

        List<CompletableFuture<String>> ioFutures5 = ioTasks.parallelStream()
            .map(task -> CompletableFuture.supplyAsync(() -> ioTask(task), ioExecutor5))
            .collect(Collectors.toList());

        // Combine all futures
        List<CompletableFuture<String>> allFutures = Stream.concat(cpuFutures5.stream(), ioFutures5.stream())
                .collect(Collectors.toList());

        // Use CompletableFuture's allOf to wait for all tasks to complete
        CompletableFuture<Void> allOf = CompletableFuture.allOf(allFutures.toArray(new CompletableFuture[0]));
        allOf.join();  // Wait for completion

        // Process results
        allFutures.forEach(future -> {
            try {
                System.out.println(future.get());
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        long endTime5 = System.currentTimeMillis();
        System.out.println("Total Time Taken: " + (endTime - startTime) + " ms");

        // Gracefully shut down executors
        cpuExecutor5.shutdown();
        ioExecutor5.shutdown();
        
        System.out.println("####################################################");
        
        
     // Executor for CPU-bound tasks
        int numCpuThreads6 = Math.min(cpuTasks.size(), Runtime.getRuntime().availableProcessors());
        ExecutorService cpuExecutor6 = Executors.newFixedThreadPool(numCpuThreads6);

        // Executor for I/O-bound tasks (Async Executor)
        int maxIoThreads6 = 10;  // Adjust this based on your use case
        ExecutorService ioExecutor6 = Executors.newFixedThreadPool(maxIoThreads6);

        // Semaphore to limit concurrent I/O tasks
        Semaphore semaphore = new Semaphore(maxIoThreads6);

        long startTime6 = System.currentTimeMillis();

        // Handle CPU-bound tasks
        List<CompletableFuture<String>> cpuFutures6 = cpuTasks.stream()
            .map(task -> CompletableFuture.supplyAsync(() -> cpuIntensiveTask(task), cpuExecutor6))
            .collect(Collectors.toList());

        // Handle I/O-bound tasks with semaphore control
        List<CompletableFuture<String>> ioFutures6 = ioTasks.stream()
            .map(task -> CompletableFuture.supplyAsync(() -> {
                try {
                    semaphore.acquire();  // Limit the number of concurrent I/O tasks
                    return ioTask(task);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    return "Error acquiring semaphore for " + task;
                } finally {
                    semaphore.release();  // Release the semaphore after task completion
                }
            }, ioExecutor6))
            .collect(Collectors.toList());

        // Combine both CPU and I/O futures
        List<CompletableFuture<String>> allFutures6 = Stream.concat(cpuFutures6.stream(), ioFutures6.stream())
            .collect(Collectors.toList());

        // Wait for all tasks to complete
        CompletableFuture<Void> allOf6 = CompletableFuture.allOf(allFutures.toArray(new CompletableFuture[0]));
        allOf.join();  // Wait for completion

        // Process results
        allFutures.forEach(future -> {
            try {
                System.out.println(future.get());
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        long endTime6 = System.currentTimeMillis();
        System.out.println("Total Time Taken: " + (endTime - startTime) + " ms");

        // Gracefully shut down executors
        cpuExecutor6.shutdown();
        ioExecutor6.shutdown();
        System.out.println("####################################################");
        
        // USING FORK JOIN POOLS FOR ABOVE
        
        
        
     // Use a ForkJoinPool for CPU-bound tasks
        ForkJoinPool cpuThreadPool7 = new ForkJoinPool(Runtime.getRuntime().availableProcessors());

        // Executor for I/O-bound tasks: a fixed thread pool with a cap on maximum threads
        ExecutorService ioThreadPool7 = Executors.newFixedThreadPool(50); // Limit number of threads for I/O tasks

        long startTime7 = System.currentTimeMillis();

        // Submit CPU tasks using CompletableFuture with ForkJoinPool
        List<CompletableFuture<String>> cpuFutures7 = cpuTasks.stream()
                .map(n -> CompletableFuture.supplyAsync(() -> cpuIntensiveTask(n), cpuThreadPool7))
                .collect(Collectors.toList());

        // Submit I/O tasks using CompletableFuture with a fixed thread pool
        List<CompletableFuture<String>> ioFutures7 = ioTasks.stream()
                .map(url -> CompletableFuture.supplyAsync(() -> ioTask(url), ioThreadPool7))
                .collect(Collectors.toList());

        // Combine all futures (CPU and I/O tasks)
        List<CompletableFuture<String>> allTasks7 = new ArrayList<>();
        allTasks.addAll(cpuFutures7);
        allTasks.addAll(ioFutures7);

        // Use CompletableFuture.allOf to wait for all tasks to complete
        CompletableFuture.allOf(allTasks.toArray(new CompletableFuture[0])).join();

        // Process results in parallel using a stream
        allTasks.parallelStream().forEach(future -> {
            try {
                System.out.println(future.get());
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        long endTime7 = System.currentTimeMillis();
        System.out.println("Total Time Taken: " + (endTime - startTime) + " ms");

        // Gracefully shut down the executors
        cpuThreadPool7.shutdown();
        ioThreadPool7.shutdown();





		
	}
}
