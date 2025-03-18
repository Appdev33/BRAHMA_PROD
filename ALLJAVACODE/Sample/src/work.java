import java.util.*;
import java.util.concurrent.*;
import java.net.*;
import java.io.*;
import java.math.BigInteger;

public class work {

    // Optimized CPU-intensive task using BigInteger for large factorials
    public static String cpuIntensiveTask(int n) {
        BigInteger result = BigInteger.ONE;
        for (int i = 2; i <= n; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return "Factorial(" + n + ") Result Length: " + result.toString().length();
    }

    // Asynchronous I/O task - Fetching data from a public API
    public static CompletableFuture<String> asyncIoTask(String url, Semaphore semaphore) {
        return CompletableFuture.supplyAsync(() -> {
            try {
                semaphore.acquire();
                HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
                connection.setRequestMethod("GET");
                connection.setConnectTimeout(10000);
                connection.setReadTimeout(10000);
                int responseCode = connection.getResponseCode();
                if (responseCode == 200) {
                    InputStream in = connection.getInputStream();
                    BufferedReader reader = new BufferedReader(new InputStreamReader(in));
                    StringBuilder response = new StringBuilder();
                    String line;
                    while ((line = reader.readLine()) != null) {
                        response.append(line);
                    }
                    reader.close();
                    return "Data from " + url + ": " + response.length() + " characters";
                } else {
                    return "Error fetching " + url + ": " + responseCode;
                }
            } catch (Exception e) {
                return "Error fetching " + url + ": " + e.getMessage();
            } finally {
                semaphore.release();
            }
        });
    }

    // Main method to execute both I/O and CPU tasks concurrently
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        List<Integer> cpuTasks = Arrays.asList(10000, 20000, 30000, 15000, 20000, 30000, 400000);
        List<String> ioTasks = Arrays.asList(
                "https://jsonplaceholder.typicode.com/posts",
                "https://jsonplaceholder.typicode.com/comments",
                "https://jsonplaceholder.typicode.com/users",
                "https://jsonplaceholder.typicode.com/albums"
        );

        int maxWorkers = Runtime.getRuntime().availableProcessors();
        ExecutorService cpuExecutor = Executors.newFixedThreadPool(maxWorkers);
        Semaphore semaphore = new Semaphore(10); // Limit concurrent I/O tasks

        long startTime = System.currentTimeMillis();

        // CPU-bound tasks: Use CompletableFuture to run CPU-bound tasks in parallel
        List<CompletableFuture<String>> cpuFutures = new ArrayList<>();
        for (int n : cpuTasks) {
            cpuFutures.add(CompletableFuture.supplyAsync(() -> cpuIntensiveTask(n), cpuExecutor));
        }

        // I/O-bound tasks: Run them asynchronously
        List<CompletableFuture<String>> ioFutures = new ArrayList<>();
        for (String url : ioTasks) {
            ioFutures.add(asyncIoTask(url, semaphore));
        }

        // Combine CPU and I/O tasks into a single list
        List<CompletableFuture<String>> allFutures = new ArrayList<>();
        allFutures.addAll(cpuFutures);
        allFutures.addAll(ioFutures);

        // Wait for all tasks to complete
        CompletableFuture<Void> allTasks = CompletableFuture.allOf(allFutures.toArray(new CompletableFuture[0]));

        allTasks.join(); // Block until all tasks are complete

        // Collect results from all tasks
        for (CompletableFuture<String> future : allFutures) {
            System.out.println(future.join());
        }

        long endTime = System.currentTimeMillis();
        System.out.println("\nTotal time taken for all tasks: " + (endTime - startTime) + " milliseconds");

        // Shutdown the executor service
        cpuExecutor.shutdown();
    }
}
