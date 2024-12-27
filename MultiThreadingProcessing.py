import threading
import time


print("**********************THREADING CONCEPTS************************")


def print_numbers() -> None:
    for i in range(5):
        print(i)
        # time.sleep(1)


def print_letters():
    for letters in 'abcde':
        print(letters)
        # time.sleep(1)


thread1 = threading.Thread(target=print_numbers)    
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread2.join()
thread1.join()

print('numbers printing for threading concept')



print("**********************LOCK/SYNCHRONISED CONCEPTS************************")
lock = threading.Lock()
counter = 0

def increment_counter():
    global counter
    for _ in range(10):
        lock.acquire()
        counter += 1
        print(f"Thread {threading.current_thread} : {counter}") 
        lock.release()

threads = [threading.Thread(target =increment_counter) for _ in range(100) ]

for t in threads:
    t.start()
for t in threads:
    t.join()

print('Locking mechanisms in threads......')        


print("**********************THREAD POOL CONCURRENT FUTURES************************")

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def cubes(n) -> int:
    # Simulating a blocking operation
    time.sleep(1)  
    return n * n * n

# if __name__ == "__main__":
    # Using ThreadPoolExecutor
start = time.time()
with ThreadPoolExecutor(max_workers=5) as pool:
    results = pool.map(cubes, range(5))
stop = time.time()

print("Results from ThreadPoolExecutor:")
print(list(results))
total_time_threads = stop - start
print(f"Total time taken with ThreadPoolExecutor: {total_time_threads:.2f} seconds")















#AGAIN

# Creating and Starting a Thread

import threading

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

print("Main thread finished.")

# Running Multiple Threads

import threading

def task(name):
    print(f"Task {name} is running.")

# Create multiple threads
threads = []
for i in range(3):
    thread = threading.Thread(target=task, args=(f"Thread-{i+1}",))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished.")

# Using a Lock to Avoid Race Conditions

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:  # Acquire lock
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")


# Deadlocks and Avoiding Them


import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    with lock1:
        print("Task 1 acquired lock1")
        with lock2:
            print("Task 1 acquired lock2")

def task2():
    with lock2:
        print("Task 2 acquired lock2")
        with lock1:
            print("Task 2 acquired lock1")

# Create threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Finished without deadlock!")


# Using Queue for Thread Communication

import threading
import queue

def producer(q):
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consuming {item}")

q = queue.Queue()

# Create threads
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # Send signal to stop consumer
consumer_thread.join()



# from concurrent.futures import ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor

def task(name):
    print(f"Task {name} is running.")

# Create a thread pool
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(task, [f"Thread-{i}" for i in range(5)])


# Daemon Threads

import threading
import time

def background_task():
    while True:
        print("Background task running...")
        time.sleep(1)

# Create a daemon thread
daemon_thread = threading.Thread(target=background_task, daemon=True)
daemon_thread.start()

time.sleep(3)
print("Main thread finished.")


# Using Thread Identifiers and Current Thread
import threading

def task():
    print(f"Running in thread: {threading.current_thread().name}")

threads = [threading.Thread(target=task, name=f"CustomThread-{i}") for i in range(3)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


# Example: Profiling Active Threads

import threading
import time

def task(name, duration):
    print(f"Thread {name} starting.")
    time.sleep(duration)
    print(f"Thread {name} finished.")

# Create multiple threads
threads = [
    threading.Thread(target=task, args=(f"Thread-{i+1}", i+1)) 
    for i in range(3)
]

# Start all threads
for thread in threads:
    thread.start()

# Profile active threads
while any(thread.is_alive() for thread in threads):
    active_threads = threading.enumerate()  # Get list of active threads
    print(f"Active threads: {[t.name for t in active_threads]}")
    time.sleep(1)  # Pause for a moment before checking again

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished.")
