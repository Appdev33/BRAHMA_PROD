# import numpy as np
# import time
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# from threading import Thread

# print("**********************BASIC MULTIPROCESSING COMPARISONS************************")

# # Matrix multiplication function
# def matrix_multiplication(start, end, matrix_a, matrix_b, result):
#     for i in range(start, end):
#         for j in range(len(matrix_b[0])):
#             result[i][j] = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_a[0])))

# # Generate random matrices for testing
# def generate_matrix(size):
#     return np.random.randint(1, 10, (size, size))

# # 1. Using ThreadPoolExecutor
# def thread_pool_executor_method(matrix_a, matrix_b):
#     result = np.zeros((len(matrix_a), len(matrix_b[0])))
#     num_threads = 4
#     chunk_size = len(matrix_a) // num_threads
#     with ThreadPoolExecutor(max_workers=num_threads) as pool:
#         futures = []
#         for i in range(num_threads):
#             start = i * chunk_size
#             end = (i + 1) * chunk_size if i != num_threads - 1 else len(matrix_a)
#             futures.append(pool.submit(matrix_multiplication, start, end, matrix_a, matrix_b, result))
#         for future in futures:
#             future.result()  # wait for all threads to complete
#     return result

# # 2. Using ProcessPoolExecutor
# def process_pool_executor_method(matrix_a, matrix_b):
#     result = np.zeros((len(matrix_a), len(matrix_b[0])))
#     num_processes = 4
#     chunk_size = len(matrix_a) // num_processes
#     with ProcessPoolExecutor(max_workers=num_processes) as pool:
#         futures = []
#         for i in range(num_processes):
#             start = i * chunk_size
#             end = (i + 1) * chunk_size if i != num_processes - 1 else len(matrix_a)
#             futures.append(pool.submit(matrix_multiplication, start, end, matrix_a, matrix_b, result))
#         for future in futures:
#             future.result()  # wait for all processes to complete
#     return result

# # 3. Using Threads (Manual Threading)
# def thread_method(matrix_a, matrix_b):
#     result = np.zeros((len(matrix_a), len(matrix_b[0])))
#     num_threads = 4
#     chunk_size = len(matrix_a) // num_threads
#     threads = []
#     for i in range(num_threads):
#         start = i * chunk_size
#         end = (i + 1) * chunk_size if i != num_threads - 1 else len(matrix_a)
#         t = Thread(target=matrix_multiplication, args=(start, end, matrix_a, matrix_b, result))
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()  # wait for all threads to complete
#     return result

# # Example Matrix Size
# matrix_size = 500

# # Generate random matrices
# matrix_a = generate_matrix(matrix_size)
# matrix_b = generate_matrix(matrix_size)

# # Protect the entry point with 'if __name__ == "__main__"'
# if __name__ == "__main__":
#     # Measure time for ThreadPoolExecutor
#     start_time = time.time()
#     result_thread_pool = thread_pool_executor_method(matrix_a, matrix_b)
#     end_time = time.time()
#     thread_pool_time = end_time - start_time
#     print(f"ThreadPoolExecutor Time: {thread_pool_time:.4f} seconds")

#     # Measure time for ProcessPoolExecutor
#     start_time = time.time()
#     result_process_pool = process_pool_executor_method(matrix_a, matrix_b)
#     end_time = time.time()
#     process_pool_time = end_time - start_time
#     print(f"ProcessPoolExecutor Time: {process_pool_time:.4f} seconds")

#     # Measure time for Manual Threading
#     start_time = time.time()
#     result_thread = thread_method(matrix_a, matrix_b)
#     end_time = time.time()
#     thread_time = end_time - start_time
#     print(f"Threading Time: {thread_time:.4f} seconds")




# # from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
# # import time
# # from multiprocessing import Process, Manager

# # # Function to compute the cube of a number
# # def cubes(x):
# #     return x * x * x

# # # Function to store results in a shared list (used for individual processes)
# # def cubes_with_shared_list(x, shared_list):
# #     shared_list.append(cubes(x))

# # if __name__ == "__main__":
# #     # Using ProcessPoolExecutor to calculate cubes for numbers from 0 to 99
# #     start_pool = time.time()
    
# #     with ProcessPoolExecutor(max_workers=5) as pool:
# #         results = pool.map(cubes, range(10000))
    
# #     stop_pool = time.time()
    
# #     print("Results from ProcessPoolExecutor:")
# #     #print(list(results))  # Display all cubes from 0^3 to 99^3
# #     total_time_process_pool = stop_pool - start_pool
# #     print(f"Total time taken with ProcessPoolExecutor: {total_time_process_pool:.2f} seconds\n")

# #     # Using individual Process instances to calculate the same cubes
# #     start_processes = time.time()
    
# #     with Manager() as manager:
# #         shared_results = manager.list()  # Shared list to store results

# #         processes = [Process(target=cubes_with_shared_list, args=(i, shared_results)) for i in range(10000)]

# #         for p in processes:
# #             p.start()
# #         for p in processes:
# #             p.join()
        
# #         stop_processes = time.time()
        
# #         results_from_individual_processes = list(shared_results)
    
# #     print("Results from individual Process instances:")
# #    #print(results_from_individual_processes)  # Display all cubes from 0^3 to 99^3
# #     total_time_individual_processes = stop_processes - start_processes
# #     print(f"Total time taken with individual Process instances: {total_time_individual_processes:.2f} seconds\n")

# #     # Using ThreadPoolExecutor to calculate cubes for numbers from 0 to 99
# #     start_threads = time.time()
    
# #     # ThreadPoolExecutor is used to run tasks in multiple threads
# #     with ThreadPoolExecutor(max_workers=5) as executor:
# #         # Each thread calculates the cube of a number in range(100)
# #         results_threads = executor.map(cubes, range(1000))
    
# #     stop_threads = time.time()
    
# #     print("Results from ThreadPoolExecutor:")
# #     #print(list(results_threads))  # Display all cubes from 0^3 to 99^3
# #     total_time_threads = stop_threads - start_threads
# #     print(f"Total time taken with ThreadPoolExecutor: {total_time_threads:.2f} seconds")


# # # ProcessPoolExecutor should be the fastest method for CPU-bound tasks when the task is complex enough.
# # # ThreadPoolExecutor will be slower for CPU-bound tasks due to the GIL, but can still be useful for I/O-bound tasks.
# # # Individual processes are slower due to higher overhead in managing the processes.


# ***************** MULTIPROCESSING FOR POOLS ****************************
# from multiprocessing import Pool
# import time

# def cube(x):
#     time.sleep(1)
#     return x * x * x

# if __name__ == "__main__":
#     with Pool(4) as pool:
#         results = pool.map(cube, range(1, 4))
#     print(results)



# from concurrent.futures import ProcessPoolExecutor
# import time

# def cube(x):
#     time.sleep(1)  # Simulate a time-consuming task
#     return x * x * x

# if __name__ == "__main__":
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         results = list(executor.map(cube, range(1, 6)))  # Blocking call
#     print(results)
    
# The ProcessPoolExecutor API is a higher-level, more modern interface compared to Pool. 
# It is designed to be more intuitive for concurrent programming and is a part of the concurrent.futures module,
# which is easier to work with for managing threads and processes.   

# It’s a tool that also sends tasks to workers, but with a cleaner and more modern interface. 
# It’s like an updated version of Pool that makes your life easier by automatically cleaning up after the workers are done,
# so you don’t have to manually manage things like shutting down the workers.
    

# ***************** SHARED MULTIPROCESSING VALUE ****************************

# from multiprocessing import Process, Value
# import os
# import time

# # Function to increment the shared value
# def increment(shared_value):
#     # Lock the shared value to avoid race conditions else VALUE WILL BE RACE CONDITIONS
#     with shared_value.get_lock():
#         # Print the process ID and the current value before incrementing
#         print(f"Process ID: {os.getpid()} | Current value before increment: {shared_value.value}")
#         shared_value.value += 1
#         # Print the updated value after incrementing
#         print(f"Process ID: {os.getpid()} | Updated value after increment: {shared_value.value}")
#         time.sleep(0.5)  # Add a small delay to observe the order of execution

# if __name__ == "__main__":
#     # Create a shared integer value with initial value 0
#     shared_value = Value('i', 0)

#     # Create a list of processes
#     processes = [Process(target=increment, args=(shared_value,)) for _ in range(10)]

#     # Start each process
#     for p in processes:
#         p.start()

#     # Wait for all processes to complete
#     for p in processes:
#         p.join()

#     # Print the final result after all processes have run
#     print(f"Final shared value: {shared_value.value}")

# from multiprocessing import Process, Queue, Lock

# def producer(q, lock):
#     for item in range(10):
#         with lock:  # Locking access to the queue
#             q.put(item)
#             print(f"Produced {item}")
#     with lock:
#         q.put(None)  # Sentinel to indicate completion

# def consumer(q, lock):
#     while True:
#         with lock:  # Locking access to the queue
#             if not q.empty():
#                 item = q.get()
#                 if item is None:  # Check for the sentinel
#                     break
#                 print(f"Consumed {item}")
#             else:
#                 continue

# if __name__ == "__main__":
#     queue = Queue()
#     lock = Lock()
#     p1 = Process(target=producer, args=(queue, lock))
#     p2 = Process(target=consumer, args=(queue, lock))

#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

# **************  Using concurrent.futures.ProcessPoolExecutor ********************
# from concurrent.futures import ProcessPoolExecutor
# import time
# import os  # Import os to get process ID

# # Function to calculate factorial and print worker ID
# def factorial(n) -> float:
#     time.sleep(1)  # Simulate a time-consuming task
#     result = 1
#     for i in range(1, n + 1):  # Start from 1 to calculate factorial correctly
#         result *= i
#     worker_id = os.getpid()  # Get the current process ID (worker ID)
#     print(f"Worker ID {worker_id} calculated factorial({n}) = {result}")
#     return result

# if __name__ == "__main__":
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         # Map the factorial function to a range of values
#         results = executor.map(factorial, range(5, 10))
#         print("*********************************")
        
#         # Print each result as it completes
#         for res in results:
#             print("Result:", res)
   

# **************  ASYCIO tasks for  ********************
# import asyncio

# async def async_task(task_name, duration):
#     print(f"Starting {task_name}")
#     await asyncio.sleep(duration)
#     print(f"Completed {task_name}")

# async def main():
#     await asyncio.gather(
#         async_task("Task 1", 2),
#         async_task("Task 2", 1),
#         async_task("Task 3", 3),
#     )

# asyncio.run(main())

# OPTIMISE FURTHER

# import asyncio
# import requests
# import aiohttp
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# import time
# import os
# import sys
# import cProfile



# # Increase the integer string conversion limit to handle large numbers
# sys.set_int_max_str_digits(1000000)   # Optional: Increase the limit to 10,000 digits

# # CPU-intensive task
# def cpu_intensive_task(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     process_id = os.getpid()  # Get process ID
#     print(f"CPU-bound task by Process ID {process_id}: factorial({n}) computed.")
#     return f"Factorial({n}) Result Length: {len(str(result))}"

# # I/O-intensive task - Fetching data from a public API
# # def io_intensive_task(url):
# #     response = requests.get(url)
# #     print(f"Fetching data from {url} | Status Code: {response.status_code}")
# #     return f"Data from {url}: {len(response.text)} characters"

# async def async_io_task_aiohttp(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             text = await response.text()
#             return f"Data from {url}: {len(text)} characters"

# # Now use asyncio for non-blocking HTTP requests


# # Async function to handle I/O tasks
# async def async_io_task(loop, executor, url):
#     # return await loop.run_in_executor(executor, io_intensive_task, url)
#     return await loop.run_in_executor(executor, async_io_task_aiohttp, url)

# # Main async function
# async def main():
#     # List of tasks for CPU and I/O bound operations
#     cpu_tasks = [10000, 20000, 30000, 15000]  # Large numbers for CPU-intensive factorial calculations
#     io_tasks = [
#         "https://jsonplaceholder.typicode.com/posts",  # Fetching posts from a public API
#         "https://jsonplaceholder.typicode.com/comments",  # Fetching comments from a public API
#         "https://jsonplaceholder.typicode.com/users",  # Fetching user information
#         "https://jsonplaceholder.typicode.com/albums",  # Fetching album data
#     ]

#     # Create executors
#     max_workers = os.cpu_count()  # Dynamically set the number of workers based on available cores
#     process_executor = ProcessPoolExecutor(max_workers=max_workers)
#     # process_executor = ProcessPoolExecutor(max_workers=4)
#     # thread_executor = ThreadPoolExecutor(max_workers=4)
#     # Adjust thread pool size dynamically based on task volume
#     thread_executor = ThreadPoolExecutor(max_workers=len(io_tasks))


#     # Start timing
#     start_time = time.time()

#     # Run CPU-bound tasks with ProcessPoolExecutor
#     cpu_futures = [process_executor.submit(cpu_intensive_task, num) for num in cpu_tasks]

#     # Run I/O-bound tasks with asyncio and ThreadPoolExecutor
#     loop = asyncio.get_event_loop()
#     io_futures = [async_io_task(loop, thread_executor, url) for url in io_tasks]

#     # Wait for all tasks to complete (I/O tasks)
#     io_results = await asyncio.gather(*io_futures)
    
#     for result in io_results:
#         print(f"Task Result: {result}")

#     # Wait for CPU-bound tasks to complete (ProcessPoolExecutor)
#     for future in cpu_futures:
#         result = future.result()
#         print(f"Task Result: {result}")

#     # End timing
#     end_time = time.time()
#     print(f"\nTotal time taken for all tasks: {end_time - start_time:.2f} seconds")

# if __name__ == "__main__":
#     # Ensure that asyncio.run is only called in the main program, not in a thread or subprocess.
#     asyncio.run(main())
#     # cProfile.run('asyncio.run(main())')



# Earlier: You used ThreadPoolExecutor (which manages threads) to handle I/O tasks concurrently. This was not ideal because, with
# aiohttp, you don’t need threads for I/O tasks since the library is designed to be non-blocking and can handle concurrency on its own.

# Now: You’ve removed the need for ThreadPoolExecutor altogether and are using asyncio directly for managing and running the I/O tasks. 
# You simply use aiohttp to fetch data, and asyncio handles running these tasks concurrently without using threads.
# This is simpler and more efficient because it avoids the overhead of managing threads manually.


# OPTIMISE FURTHER
# import asyncio
# import aiohttp
# import os
# import time
# import sys
# from concurrent.futures import ProcessPoolExecutor

# sys.set_int_max_str_digits(1000000)

# def cpu_intensive_task(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return f"Factorial({n}) Result Length: {len(str(result))}"

# async def async_io_task_aiohttp(url):
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
#         async with session.get(url) as response:
#             text = await response.text()
#             return f"Data from {url}: {len(text)} characters"

# async def main():
#     cpu_tasks = [10000, 20000, 30000, 15000]
#     io_tasks = [
#         "https://jsonplaceholder.typicode.com/posts",
#         "https://jsonplaceholder.typicode.com/comments",
#         "https://jsonplaceholder.typicode.com/users",
#         "https://jsonplaceholder.typicode.com/albums",
#     ]

#     max_workers = os.cpu_count()
#     process_executor = ProcessPoolExecutor(max_workers=max_workers)

#     start_time = time.time()

#     cpu_futures = [process_executor.submit(cpu_intensive_task, num) for num in cpu_tasks]
#     io_results = await asyncio.gather(*(async_io_task_aiohttp(url) for url in io_tasks))

#     for result in io_results:
#         print(f"Task Result: {result}")

#     for future in cpu_futures:
#         result = future.result()
#         print(f"Task Result: {result}")

#     end_time = time.time()
#     print(f"\nTotal time taken for all tasks: {end_time - start_time:.2f} seconds")

# if __name__ == "__main__":
#     asyncio.run(main())






# Yes, using asyncio does have an advantage in this specific scenario, particularly for I/O-bound tasks like fetching data from APIs.
#  Here's a detailed explanation of why and when asyncio provides an advantage:

# Why does asyncio offer an advantage for I/O-bound tasks?
# Non-blocking nature:

# I/O-bound tasks (like HTTP requests, reading files, database queries, etc.) typically spend most of their time waiting for responses from external sources (e.g., waiting for data to arrive from the web server).
# With asyncio, instead of blocking the execution while waiting for the response (which would happen in a standard, synchronous program), it allows other tasks to run concurrently while waiting for I/O. This means while one task is waiting for I/O, another task can make progress, leading to better utilization of system resources and time efficiency.
# Concurrency with a single thread:

# asyncio allows multiple I/O-bound tasks to run concurrently within a single thread, which avoids the overhead of thread context switching.
# In contrast, if you used threads (ThreadPoolExecutor), each thread would block while waiting for I/O, which introduces overhead due to multiple threads being created and managed by the OS.
# asyncio uses a single thread (event loop) and handles all tasks asynchronously, which is much more efficient than using threads when the tasks are I/O-bound.
# In your example:
# The I/O tasks (like fetching data from the public API) spend most of their time waiting for a response. Without asyncio, these tasks would block each other, one waiting for the server to respond before the next request can be made.
# With asyncio, while one request is waiting, other requests can be processed concurrently without the need to wait for the previous one to finish.
# Benefits of asyncio:
# Reduced Blocking: Tasks like HTTP requests are inherently slow due to network latency. Instead of waiting for each request to complete, asyncio allows the program to initiate multiple requests at once and handle them concurrently.
# Less Overhead: Since asyncio runs on a single thread, it doesn't have the overhead of managing multiple threads, which reduces the memory and CPU overhead that would typically come with using threads.
# Faster Execution: For I/O-bound tasks, using asyncio can speed up the overall execution because it allows concurrent execution without waiting for blocking operations to complete.
# Comparisons:
# Without asyncio:
# If you were to run the I/O tasks one by one synchronously (without asyncio), the program would block and wait for each HTTP request to finish before starting the next one.
# With asyncio:
# asyncio allows you to send all the HTTP requests at once, and while waiting for their responses, other tasks can continue executing. This is particularly advantageous when dealing with many I/O-bound operations, such as API calls or file downloads.
# When would you not need asyncio?
# If you are working with CPU-bound tasks, like complex calculations (e.g., your factorial calculation), asyncio is not useful. Instead, you would use multithreading or multiprocessing to take advantage of multiple CPU cores since I/O is not involved. For CPU-bound tasks, asyncio won't speed up execution because it is designed to handle I/O-bound tasks efficiently.

# If you only have a small number of I/O-bound tasks (say, one or two network requests), the performance difference between using asyncio and using threads might be negligible.

# Conclusion:
# Using asyncio does provide a significant advantage for I/O-bound tasks, especially when you have many concurrent tasks like HTTP requests. It allows you to handle multiple tasks concurrently without the overhead of creating multiple threads, and without blocking the program during I/O operations. For CPU-bound tasks, you would still need to use multiprocessing or multithreading.

# In your example with multiple I/O tasks (like fetching data from URLs), asyncio helps maximize efficiency by allowing you to perform many requests in parallel and use time more effectively while waiting for I/O to complete.



# OPTIMISE FURTHER
# import asyncio
# import aiohttp
# import os
# import time
# import math
# import sys
# from concurrent.futures import ProcessPoolExecutor

# # Set a higher limit for integer string conversion if needed (adjust based on your use case)
# sys.set_int_max_str_digits(1000000)  # Adjusted limit to handle large factorial results

# # Optimized CPU-intensive task using math.factorial
# def cpu_intensive_task(n):
#     result = math.factorial(n)
#     return f"Factorial({n}) Result Length: {len(str(result))}"

# # Asynchronous I/O task - Fetching data from a public API
# async def async_io_task_aiohttp(url):
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
#         async with session.get(url) as response:
#             text = await response.text()
#             return f"Data from {url}: {len(text)} characters"

# # Main async function
# async def main():
#     # List of tasks for CPU and I/O bound operations
#     cpu_tasks = [10000, 20000, 30000, 15000]  # Large numbers for CPU-intensive factorial calculations
#     io_tasks = [
#         "https://jsonplaceholder.typicode.com/posts",
#         "https://jsonplaceholder.typicode.com/comments",
#         "https://jsonplaceholder.typicode.com/users",
#         "https://jsonplaceholder.typicode.com/albums",
#     ]

#     # Define the maximum workers for CPU tasks
#     max_workers = os.cpu_count()
#     process_executor = ProcessPoolExecutor(max_workers=max_workers)

#     # Start timing
#     start_time = time.time()

#     # Run CPU-bound tasks with ProcessPoolExecutor
#     loop = asyncio.get_running_loop()
#     cpu_futures = [loop.run_in_executor(process_executor, cpu_intensive_task, num) for num in cpu_tasks]

#     # Run I/O-bound tasks with asyncio directly
#     io_futures = [async_io_task_aiohttp(url) for url in io_tasks]

#     # Gather all tasks (both CPU-bound and I/O-bound) in a single await
#     results = await asyncio.gather(*cpu_futures, *io_futures)

#     # Process and print results
#     for result in results:
#         print(f"Task Result: {result}")

#     # End timing
#     end_time = time.time()
#     print(f"\nTotal time taken for all tasks: {end_time - start_time:.2f} seconds")

#     # Shutdown ProcessPoolExecutor after use
#     process_executor.shutdown()

# if __name__ == "__main__":
#     asyncio.run(main())



# Explanation of the Optimizations:
# Use of math.factorial(): This function is much faster than a manual factorial loop for large numbers, especially in Python
# where integer handling is optimized.
# Single asyncio.gather: By calling asyncio.gather on both cpu_futures and io_futures together, the event loop handles all tasks
# concurrently, optimizing time and resource use.
# Process Pool Context Management: Wrapping the ProcessPoolExecutor in async with ensures proper resource cleanup without 
# additional code, which is efficient in Python 3.9+.

# OPTIMISE FURTHER

# import asyncio
# import aiohttp
# import os
# import time
# import math
# import sys
# from concurrent.futures import ProcessPoolExecutor

# # Set a higher limit for integer string conversion (adjusted for large factorial results)
# sys.set_int_max_str_digits(1000000)

# # Optimized CPU-intensive task using math.factorial
# def cpu_intensive_task(n):
#     result = math.factorial(n)
#     return f"Factorial({n}) Result Length: {len(str(result))}"

# # Asynchronous I/O task - Fetching data from a public API (reuse ClientSession for efficiency)
# async def async_io_task_aiohttp(session, url):
#     async with session.get(url) as response:
#         text = await response.text()
#         return f"Data from {url}: {len(text)} characters"

# # Main async function
# async def main():
#     # List of tasks for CPU and I/O bound operations
#     cpu_tasks = [10000, 20000, 30000, 15000]  # Large numbers for CPU-intensive factorial calculations
#     io_tasks = [
#         "https://jsonplaceholder.typicode.com/posts",
#         "https://jsonplaceholder.typicode.com/comments",
#         "https://jsonplaceholder.typicode.com/users",
#         "https://jsonplaceholder.typicode.com/albums",
#     ]

#     # Define the maximum workers for CPU tasks
#     max_workers = os.cpu_count()
#     process_executor = ProcessPoolExecutor(max_workers=max_workers)

#     # Start timing
#     start_time = time.time()

#     # Create an aiohttp ClientSession once and pass it to tasks
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:

#         # Run CPU-bound tasks with ProcessPoolExecutor
#         loop = asyncio.get_running_loop()
#         cpu_futures = [loop.run_in_executor(process_executor, cpu_intensive_task, num) for num in cpu_tasks]

#         # Run I/O-bound tasks with asyncio directly using the same session
#         io_futures = [async_io_task_aiohttp(session, url) for url in io_tasks]

#         # Gather all tasks (both CPU-bound and I/O-bound) in a single await
#         results = await asyncio.gather(*cpu_futures, *io_futures)

#         # Process and print results
#         for result in results:
#             print(f"Task Result: {result}")

#     # End timing
#     end_time = time.time()
#     print(f"\nTotal time taken for all tasks: {end_time - start_time:.2f} seconds")

#     # Shutdown ProcessPoolExecutor after use
#     process_executor.shutdown()

# if __name__ == "__main__":
#     asyncio.run(main())
    

# Key Optimizations:
# Reuse ClientSession: By creating a single aiohttp.ClientSession and reusing it across all I/O tasks, we 
# avoid the overhead of creating a new session for each individual request. This minimizes the performance penalty 
# that comes from repeatedly opening new connections.
# Efficient Task Handling: asyncio.gather() is used to manage both CPU-bound and I/O-bound tasks concurrently. 
# The CPU-bound tasks run in a separate process pool to avoid blocking the event loop, while the I/O-bound tasks benefit
# from the async nature of aiohttp.
# Reused Session in I/O tasks: The I/O tasks now share a single session instead of creating one per task. 
# This is more efficient and reduces overhead, especially when dealing with many HTTP requests.


# import asyncio
# import aiohttp
# import os
# import time
# import math
# import sys
# from concurrent.futures import ProcessPoolExecutor
# from functools import partial

# # Set a higher limit for integer string conversion (adjusted for large factorial results)
# sys.set_int_max_str_digits(100000000)

# # Optimized CPU-intensive task using math.factorial
# def cpu_intensive_task(n):
#     result = math.factorial(n)
#     return f"Factorial({n}) Result Length: {len(str(result))}"

# # Asynchronous I/O task - Fetching data from a public API (reuse ClientSession for efficiency)
# async def async_io_task_aiohttp(session, url):
#     async with session.get(url) as response:
#         text = await response.text()
#         return f"Data from {url}: {len(text)} characters"

# # Main async function
# async def main():
#     # List of tasks for CPU and I/O bound operations
#     cpu_tasks = [10000, 20000, 30000, 15000, 20000, 30000, 400000]  # Large numbers for CPU-intensive factorial calculations
#     io_tasks = [
#         "https://jsonplaceholder.typicode.com/posts",
#         "https://jsonplaceholder.typicode.com/comments",
#         "https://jsonplaceholder.typicode.com/users",
#         "https://jsonplaceholder.typicode.com/albums",
#         "https://jsonplaceholder.typicode.com/posts",
#         "https://jsonplaceholder.typicode.com/comments",
#         "https://jsonplaceholder.typicode.com/users",
#         "https://jsonplaceholder.typicode.com/albums",
#         "https://jsonplaceholder.typicode.com/posts",
#         "https://jsonplaceholder.typicode.com/comments",
#         "https://jsonplaceholder.typicode.com/users",
#         "https://jsonplaceholder.typicode.com/albums",
#     ]

#     # Define the maximum workers for CPU tasks
#     max_workers = os.cpu_count()

#     # Start timing
#     start_time = time.time()

#     # Create an aiohttp ClientSession once and pass it to tasks
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:

#         # Use asyncio.to_thread for CPU-bound tasks to avoid process management overhead
#         cpu_futures = [asyncio.to_thread(cpu_intensive_task, num) for num in cpu_tasks]

#         # Run I/O-bound tasks concurrently using the same session
#         io_futures = [async_io_task_aiohttp(session, url) for url in io_tasks]

#         # Gather all tasks (both CPU-bound and I/O-bound) in a single await
#         results = await asyncio.gather(*cpu_futures, *io_futures)

#         # Process and print results
#         for result in results:
#             print(f"Task Result: {result}")

#     # End timing
#     end_time = time.time()
#     print(f"\nTotal time taken for all tasks: {end_time - start_time:.2f} seconds")

# if __name__ == "__main__":
#     asyncio.run(main())


# import asyncio
# import aiohttp
# import os
# import time
# import math
# import sys
# from concurrent.futures import ProcessPoolExecutor
# from aiohttp import ClientTimeout

# # Set a higher limit for integer string conversion (adjusted for large factorial results)
# sys.set_int_max_str_digits(100000000)

# # Optimized CPU-intensive task using math.factorial
# def cpu_intensive_task(n):
#     result = math.factorial(n)
#     return f"Factorial({n}) Result Length: {len(str(result))}"

# # Asynchronous I/O task - Fetching data from a public API (reuse ClientSession for efficiency)
# async def async_io_task_aiohttp(session, url, semaphore):
#     async with semaphore:
#         try:
#             async with session.get(url) as response:
#                 response.raise_for_status()  # Raise an exception for non-2xx status codes
#                 text = await response.text()
#                 return f"Data from {url}: {len(text)} characters"
#         except Exception as e:
#             return f"Error fetching {url}: {str(e)}"

# # Main async function
# async def main():
#     # List of tasks for CPU and I/O bound operations
#     cpu_tasks = [10000, 20000, 30000, 15000, 20000, 30000, 400000]  # Large numbers for CPU-intensive factorial calculations
#     io_tasks = [
#         "https://jsonplaceholder.typicode.com/posts",
#         "https://jsonplaceholder.typicode.com/comments",
#         "https://jsonplaceholder.typicode.com/users",
#         "https://jsonplaceholder.typicode.com/albums",
#     ]

#     # Define the maximum workers for CPU tasks
#     max_workers = os.cpu_count()

#     # Limit the concurrency of I/O-bound tasks
#     io_concurrency_limit = 10  # Limit concurrent I/O tasks to 10 at once
#     semaphore = asyncio.Semaphore(io_concurrency_limit)

#     # Start timing
#     start_time = time.time()

#     # Create an aiohttp ClientSession once and pass it to tasks
#     timeout = ClientTimeout(total=10)  # Set a reasonable timeout for all requests
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), timeout=timeout) as session:

#         # Use ProcessPoolExecutor for CPU-bound tasks to avoid GIL issues
#         with ProcessPoolExecutor() as pool:
#             # CPU-bound tasks (use `submit` to run them in processes instead of threads)
#             cpu_futures = [
#                 asyncio.get_event_loop().run_in_executor(pool, cpu_intensive_task, num) 
#                 for num in cpu_tasks
#             ]
        
#         # Run I/O-bound tasks concurrently using the same session
#         io_futures = [async_io_task_aiohttp(session, url, semaphore) for url in io_tasks]

#         # Gather all tasks (both CPU-bound and I/O-bound) in a single await
#         results = await asyncio.gather(*cpu_futures, *io_futures)

#         # Process and print results
#         for result in results:
#             print(f"Task Result: {result}")

#     # End timing
#     end_time = time.time()
#     print(f"\nTotal time taken for all tasks: {end_time - start_time:.2f} seconds")

# if __name__ == "__main__":
#     asyncio.run(main())

# import asyncio
# import aiohttp
# import os
# import time
# import math
# import sys
# from concurrent.futures import ProcessPoolExecutor
# from aiohttp import ClientTimeout

# # Set a higher limit for integer string conversion (adjusted for large factorial results)
# sys.set_int_max_str_digits(2500000)

# # Optimized CPU-intensive task using math.factorial
# def cpu_intensive_task(n):
#     result = math.factorial(n)
#     return f"Factorial({n}) Result Length: {len(str(result))}"

# # Asynchronous I/O task - Fetching data from a public API (reuse ClientSession for efficiency)
# async def async_io_task_aiohttp(session, url, semaphore):
#     async with semaphore:
#         try:
#             async with session.get(url) as response:
#                 response.raise_for_status()  # Raise an exception for non-2xx status codes
#                 text = await response.text()
#                 return f"Data from {url}: {len(text)} characters"
#         except Exception as e:
#             return f"Error fetching {url}: {str(e)}"

# # Helper function to manage CPU and I/O tasks concurrently in batches
# async def run_in_batches(cpu_futures, io_futures, batch_size=5):
#     results = []
#     # Batch execution for CPU-bound tasks
#     for i in range(0, len(cpu_futures), batch_size):
#         batch_cpu = cpu_futures[i:i + batch_size]
#         results.extend(await asyncio.gather(*batch_cpu))
        
#     # Batch execution for I/O-bound tasks
#     for i in range(0, len(io_futures), batch_size):
#         batch_io = io_futures[i:i + batch_size]
#         results.extend(await asyncio.gather(*batch_io))

#     return results

# # Main async function
# async def main():
#     # List of tasks for CPU and I/O bound operations
#     cpu_tasks = [10000, 20000, 30000, 15000, 20000, 30000, 400000]  # Large numbers for CPU-intensive factorial calculations
#     io_tasks = [
#         "https://jsonplaceholder.typicode.com/posts",
#         "https://jsonplaceholder.typicode.com/comments",
#         "https://jsonplaceholder.typicode.com/users",
#         "https://jsonplaceholder.typicode.com/albums",
#     ]

#     # Define the maximum workers for CPU tasks
#     max_workers = os.cpu_count()

#     # Limit the concurrency of I/O-bound tasks
#     io_concurrency_limit = 10  # Limit concurrent I/O tasks to 10 at once
#     semaphore = asyncio.Semaphore(io_concurrency_limit)

#     # Start timing
#     start_time = time.time()

#     # Create an aiohttp ClientSession once and pass it to tasks
#     timeout = ClientTimeout(total=10)  # Set a reasonable timeout for all requests
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), timeout=timeout) as session:

#         # Use ProcessPoolExecutor for CPU-bound tasks to avoid GIL issues
#         with ProcessPoolExecutor() as pool:
#             # CPU-bound tasks (use `submit` to run them in processes instead of threads)
#             cpu_futures = [
#                 asyncio.get_event_loop().run_in_executor(pool, cpu_intensive_task, num) 
#                 for num in cpu_tasks
#             ]
        
#         # Run I/O-bound tasks concurrently using the same session
#         io_futures = [async_io_task_aiohttp(session, url, semaphore) for url in io_tasks]

#         # Run both I/O and CPU-bound tasks in batches for better resource management
#         results = await run_in_batches(cpu_futures, io_futures)

#         # Process and print results
#         for result in results:
#             print(f"Task Result: {result}")

#     # End timing
#     end_time = time.time()
#     print(f"\nTotal time taken for all tasks: {end_time - start_time:.2f} seconds")

# if __name__ == "__main__":
#     asyncio.run(main())


# import asyncio
# import aiohttp
# import os
# import time
# import math
# import sys
# from concurrent.futures import ProcessPoolExecutor
# from aiohttp import ClientTimeout

# # Set a higher limit for integer string conversion (adjusted for large factorial results)
# sys.set_int_max_str_digits(2500000)

# # Optimized CPU-intensive task using math.factorial
# def cpu_intensive_task(n):
#     result = math.factorial(n)
#     return f"Factorial({n}) Result Length: {len(str(result))}"

# # Asynchronous I/O task - Fetching data from a public API (reuse ClientSession for efficiency)
# async def async_io_task_aiohttp(session, url, semaphore):
#     async with semaphore:
#         try:
#             async with session.get(url) as response:
#                 response.raise_for_status()  # Raise an exception for non-2xx status codes
#                 text = await response.text()
#                 return f"Data from {url}: {len(text)} characters"
#         except Exception as e:
#             return f"Error fetching {url}: {str(e)}"

# # Optimized function for concurrently running tasks (CPU and I/O tasks)
# async def run_concurrent_tasks(cpu_futures, io_futures):
#     # Run CPU-bound tasks and I/O-bound tasks concurrently
#     return await asyncio.gather(*cpu_futures, *io_futures)

# # Main async function
# async def main():
#     # List of tasks for CPU and I/O bound operations
#     cpu_tasks = [10000, 20000, 30000, 15000, 20000, 30000, 400000]  # Large numbers for CPU-intensive factorial calculations
#     io_tasks = [
#         "https://jsonplaceholder.typicode.com/posts",
#         "https://jsonplaceholder.typicode.com/comments",
#         "https://jsonplaceholder.typicode.com/users",
#         "https://jsonplaceholder.typicode.com/albums",
#     ]

#     # Define the maximum workers for CPU tasks
#     max_workers = os.cpu_count()

#     # Limit the concurrency of I/O-bound tasks
#     io_concurrency_limit = 10  # Limit concurrent I/O tasks to 10 at once
#     semaphore = asyncio.Semaphore(io_concurrency_limit)

#     # Start timing
#     start_time = time.time()

#     # Create an aiohttp ClientSession once and pass it to tasks
#     timeout = ClientTimeout(total=10)  # Set a reasonable timeout for all requests
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), timeout=timeout) as session:

#         # Use ProcessPoolExecutor for CPU-bound tasks to avoid GIL issues
#         with ProcessPoolExecutor(max_workers=max_workers) as pool:
#             # CPU-bound tasks (use `submit` to run them in processes instead of threads)
#             cpu_futures = [
#                 asyncio.get_event_loop().run_in_executor(pool, cpu_intensive_task, num)
#                 for num in cpu_tasks
#             ]
        
#         # Run I/O-bound tasks concurrently using the same session
#         io_futures = [async_io_task_aiohttp(session, url, semaphore) for url in io_tasks]

#         # Run both I/O and CPU-bound tasks concurrently
#         results = await run_concurrent_tasks(cpu_futures, io_futures)

#         # Process and print results
#         for result in results:
#             print(f"Task Result: {result}")

#     # End timing
#     end_time = time.time()
#     print(f"\nTotal time taken for all tasks: {end_time - start_time:.2f} seconds")

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import aiohttp
import os
import time
import math
import sys
from aiohttp import ClientTimeout

# Set a higher limit for integer string conversion (adjusted for large factorial results)
sys.set_int_max_str_digits(2500000)

# Optimized CPU-intensive task using math.factorial
def cpu_intensive_task(n):
    result = math.factorial(n)
    return f"Factorial({n}) Result Length: {len(str(result))}"

# Asynchronous I/O task - Fetching data from a public API (reuse ClientSession for efficiency)
async def async_io_task_aiohttp(session, url, semaphore):
    async with semaphore:
        try:
            async with session.get(url) as response:
                response.raise_for_status()  # Raise an exception for non-2xx status codes
                text = await response.text()
                return f"Data from {url}: {len(text)} characters"
        except Exception as e:
            return f"Error fetching {url}: {str(e)}"

# Optimized function for concurrently running tasks (CPU and I/O tasks)
async def run_concurrent_tasks(cpu_futures, io_futures):
    # Run CPU-bound tasks and I/O-bound tasks concurrently
    return await asyncio.gather(*cpu_futures, *io_futures)

# Main async function
async def main():
    # List of tasks for CPU and I/O bound operations
    cpu_tasks = [10000, 20000, 30000, 15000, 20000, 30000, 400000]  # Large numbers for CPU-intensive factorial calculations
    io_tasks = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/users",
        "https://jsonplaceholder.typicode.com/albums",
    ]

    # Define the maximum workers for CPU tasks
    max_workers = os.cpu_count()

    # Limit the concurrency of I/O-bound tasks
    io_concurrency_limit = 10  # Limit concurrent I/O tasks to 10 at once
    semaphore = asyncio.Semaphore(io_concurrency_limit)

    # Start timing
    start_time = time.time()

    # Create an aiohttp ClientSession once and pass it to tasks
    timeout = ClientTimeout(total=10)  # Set a reasonable timeout for all requests
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), timeout=timeout) as session:

        # Using asyncio.to_thread for CPU-bound tasks to avoid process pool overhead
        cpu_futures = [
            asyncio.to_thread(cpu_intensive_task, num)
            for num in cpu_tasks
        ]
        
        # Run I/O-bound tasks concurrently using the same session
        io_futures = [async_io_task_aiohttp(session, url, semaphore) for url in io_tasks]

        # Run both I/O and CPU-bound tasks concurrently
        results = await run_concurrent_tasks(cpu_futures, io_futures)

        # Process and print results
        for result in results:
            print(f"Task Result: {result}")

    # End timing
    end_time = time.time()
    print(f"\nTotal time taken for all tasks: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())








