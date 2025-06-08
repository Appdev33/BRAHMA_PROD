import time
import random

from itertools import chain, combinations, permutations, product
from functools import reduce



# # *******    EXCEPTIONS ********
# # bmt_common/exceptions.py

# class BMTBaseException(Exception):
#     """Base exception for all BMT-related errors."""

#     def __init__(self, message: str, code: int = 500):
#         super().__init__(message)
#         self.message = message
#         self.code = code  # Can be mapped to HTTP codes or internal status codes

#     def __str__(self):
#         return f"[{self.code}] {self.message}"



# # bmt_common/exceptions.py

# class BMTBaseException(Exception):
#     """Base exception for all BMT-related errors."""

#     def __init__(self, message: str, code: int = 500):
#         super().__init__(message)
#         self.message = message
#         self.code = code  # Can be mapped to HTTP codes or internal status codes

#     def __str__(self):
#         return f"[{self.code}] {self.message}"


# from bmt_common.exceptions import EncryptionError

# def encrypt_file(file_path: str):
#     try:
#         ...
#     except Exception as e:
#         raise EncryptionError(f"Failed to encrypt {file_path}: {e}")
		

# *************************** ENUMS ***************************

# from enum import Enum

# class Environment(Enum):
#     DEV = "dev"
#     STAGING = "staging"
#     PROD = "prod"

# print(Environment.PROD)         # Environment.PROD
# print(Environment.PROD.value)   # 'prod'


# *************************** DATACLASS ***************************
# A Python decorator from the dataclasses module (Python 3.7+).
# It automatically generates boilerplate methods like __init__, __repr__, __eq__, etc., 
# for data container classes.
# Reduces redundancy and improves readability

# from dataclasses import dataclass

# @dataclass(init=True, repr=True, eq=True, order=True, frozen=True)
# class Product:
#     id: int
#     name: str
#     price: float = 0.0

# init=True: Generates __init__(id, name, price)
# repr=True: Nice string output
# eq=True: Enables == comparison
# order=True: Enables sorting: <, <=, etc.
# frozen=True: Makes the instance immutable (cannot modify after creation)

# p1 = Product(1, "Pen", 10.5)
# print(p1)            # Product(id=1, name='Pen', price=10.5)
# print(p1 == p1)      # True
# # p1.price = 12.0     # ❌ Error: frozen instance



# *************************** BISECT MODULE ***************************
# import bisect

# a = [10, 20, 30, 30, 40]

# print(bisect.bisect_left(a, 30))   # 2
# print(bisect.bisect_right(a, 30))  # 4

# bisect.insort_left(a, 30)
# print(a)  # [10, 20, 30, 30, 30, 40]

# bisect.insort_right(a, 25)
# print(a)  # [10, 20, 25, 30, 30, 30, 40]


# Function	Inserts / Finds	Position relative to duplicates
# bisect_left	Finds	Leftmost (before duplicates)
# bisect_right	Finds	Rightmost (after duplicates)
# insort_left	Inserts	Leftmost
# insort_right	Inserts	Rightmost


# *************************** MIXINS ***************************
# A Mixin is a class designed to provide additional functionality to other classes
# through multiple inheritance — but it doesn't stand alone 
# (i.e., you don’t instantiate a Mixin by itself).
# Mixins help you reuse code without using deep inheritance trees.
# They add focused behavior to classes in a modular way.
# Typically, Mixins don’t define __init__ (or if they do, they call super() carefully).

# class LoggerMixin:
#     def log(self, message: str):
#         print(f"[LOG] {message}")

# class FileHandler(LoggerMixin):
#     def open(self, filename):
#         self.log(f"Opening file {filename}")
#         # code to open file

#     def close(self):
#         self.log("Closing file")
#         # code to close file

# # Usage
# file = FileHandler()
# file.open("test.txt")  # Prints: [LOG] Opening file test.txt
# file.close()           # Prints: [LOG] Closing file




# *************************** ANNOTATIONS ***************************

# from typing import List, Dict, Tuple

# def total(numbers: List[int]) -> int:
#     return sum(numbers)

# def phonebook() -> Dict[str, str]:
#     return {"Alice": "1234", "Bob": "5678"}

# def location() -> Tuple[float, float]:
#     return (12.9716, 77.5946)

# from typing import Optional, Union

# def greet(name: Optional[str] = None) -> str:
#     return f"Hello, {name or 'Guest'}"

# def square(x: Union[int, float]) -> float:
#     return float(x * x)


# Syntax	Meaning
# List[int]	List of integers
# Dict[str, int]	Dictionary with str keys, int values
# Optional[str]	str or None
# Union[int, float]	int or float
# Callable[[int, int], int]	function with 2 int args, returns int
# TypeVar('T')	generic type placeholder
# NoReturn	function that never returns (e.g., exits)

# # *************************** GENERICS ***************************

# from typing import TypeVar, Generic

# T = TypeVar('T')  # Define a generic type variable

# class Box(Generic[T]):
#     def __init__(self, content: T):
#         self.content = content

#     def get(self) -> T:
#         return self.content

# # Usage
# int_box: Box[int] = Box(100)
# str_box: Box[str] = Box("Hello")

# print(int_box.get())  # 100
# print(str_box.get())  # Hello

# from typing import TypeVar, List

# T = TypeVar('T')  # Declare a generic type variable

# def get_first(items: List[T]) -> T:
#     return items[0]

# # Usage
# int_list = [1, 2, 3]
# str_list = ["apple", "banana", "cherry"]

# print(get_first(int_list))  # Output: 1
# print(get_first(str_list))  # Output: "apple"


# ************ CUSTOM CONTEXT MANAGER ************
# class MyContextManager:
#     def __enter__(self):
#         print("Entering the block")
#         return self  # Whatever is returned here is assigned to the 'as' variable
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exiting the block")

# with MyContextManager() as mgr:
#     print("Inside the block")



# *************************** REUSING ITERATORS AND GENERATORS ***************************


# my_list = [10, 20, 30]

# # Create an iterator from the list
# it = iter(my_list)
# print(next(it))  # 10
# print(next(it))  # 20

# # Exhaust the iterator
# print(next(it))  # 30
# print(next(it, "No more items"))  # No more items

# # The iterator `it` is now exhausted and cannot be reused.

# # But we can reuse the original list by creating a NEW iterator
# it2 = iter(my_list)
# print(next(it2))  # 10  ← starts fresh
# print(next(it2))  # 20


# def my_gen():
#     yield 10
#     yield 20
#     yield 30

# gen = my_gen()
# print(next(gen))  # 10
# print(next(gen))  # 20
# print(next(gen))  # 30

# # Generator is exhausted now
# print(next(gen, "No more items"))  # No more items

# # You *cannot* reuse the same `gen` again — it's exhausted

# # To reuse, create a *new* generator object by calling the function again
# gen2 = my_gen()
# print(next(gen2))  # 10  ← starts fresh
# print(next(gen2))  # 20



# *************************** GENERATORS ***************************


# from itertools import combinations

# def generator_combinations(n):
#     # This yields one combination at a time (generator)
#     for combo in combinations(range(n), 3):
#         yield combo

# def generator_example(n):
#     gen = generator_combinations(n)  # Create generator
    
#     while True:
#         item = next(gen, None)
#         if item is None:
#             print("No more items")
#             break
#         print(item)

# # generator_example(6)
# gen = generator_combinations(4)

# # First iteration: consume some items
# print(next(gen))  # (0, 1)
# print(next(gen))  # (0, 2)

# # Exhaust the rest of the generator
# for item in gen:
#     print(item)

# print("Trying to reuse the same exhausted generator:")
# try:
#     print(next(gen))
# except StopIteration:
#     print("Generator is exhausted and cannot be reused")

# *************************** ITERATORS ***************************

# class Countdown:
#     def __init__(self, start):
#         self.current = start

#     def __iter__(self):
#         return self  # An iterator must return itself

#     def __next__(self):
#         if self.current <= 0:
#             raise StopIteration  # End of iteration
#         value = self.current
#         self.current -= 1
#         return value

# # Usage
# for number in Countdown(5):
#     print(number)

# # Output:
# # 5
# # 4
# # 3
# # 2
# # 1


# def iterators(n):
#     list_numbers = list(combinations(range(n), 3))

#     iterator = iter(list_numbers)
#     while True:
#         item = next(iterator, None)
#         if item is None:
#             print("No more items")
#             break
#         print(item)


# iterators(6)




# *************************** Itertools Examples ***************************
# *************************** LAMBDAS ***************************

# def practice_functions(n):
#     return list(permutations(range(n)))[2]

# def lamdas_practice():

#     permute = practice_functions(5)
#     print(permute)
#     print(f"Permutations of 5: {list(filter(lambda x: x>2, permute))}")  
#     print(f"Permutations of 5: {list(map(lambda x: x**2, permute))}") 
#     print(f"Permutations of 5: {reduce(lambda x,y : x+y, permute)}") 



# lamdas_practice()

# *************************** Monkey Patching Example ***************************

# class Math:
#     def __init__(self, a=None, b=None):
#         self.a = a
#         self.b = b

#     def add(self, a=None, b=None):
#         x = a if a is not None else self.a
#         y = b if b is not None else self.b
#         if x is None or y is None:
#             raise ValueError("Both values must be provided either during init or method call.")
#         return x + y

# # ✅ Step 1: Save original
# original_add = Math.add

# # ✅ Step 2: Define monkey-patched version
# def patched_add(self, a=None, b=None):
#     result = original_add(self, a, b)
#     print(f"[patched] Adding {a} and {b} → {result} → {float(result)}")
#     return float(result)

# # ✅ Step 3: Monkey patch the class
# # Math.add = patched_add

# # ✅ Test it
# m = Math(2, 3)
# print(m.add())         # Output: 5.0
# print(m.add(10, 20))   # Output: 30.0


# *************************** CLOSURES ***************************

# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count  # Needed to modify 'count' from outer scope
#         count += 1
#         return count
#     return counter

# # Create two independent counters
# c1 = make_counter()
# c2 = make_counter()

# print(c1())  # 1
# print(c1())  # 2
# print(c2())  # 1 (independent)
# print(c1())  # 3


# def make_multiplier(factor):
#     def multiplier(number):
#         return number * factor
#     return multiplier

# # Create a times-two function
# times_two = make_multiplier(2)
# times_three = make_multiplier(3)

# print(times_two(5))     # Output: 10
# print(times_three(5))   # Output: 15
	
			
# *************************** Decorator to measure execution time of a function ***************************

# def timed_decorate(func):
#     def wrapper(*args, **kwargs):  # Accept arguments for the wrapped function
#         print("Before Decorator")
#         print(f"Function {func.__name__} is being executed with arguments: {args} and keyword arguments: {kwargs}")
#         st = time.time()  # Start time
#         res = func(*args, **kwargs)  # Call the original function with arguments
#         et = time.time()  # End time
#         print(f"After Decorator: Execution time = {et - st:.6f} seconds")  # Calculate and print execution time
#         print(f"After Decorator {res}")
#         return res  # Return the result of the original function
#     return wrapper  # Return the wrapper function


# @timed_decorate
# def display_res(val):
#     for i in range(1000000):  # Simulate some processing
#         pass
#     print(f"Hello {val} ")
#     return random.randint(1, 100)  # Return a random integer as an example
    
# display_res("Values")

# *************************** RANDOMs ***************************

# def fibonaci(n):
# 	a, b = 0, 1
# 	for _ in range(n):
# 		yield a
# 		a, b = b, a + b

# print(list(fibonaci(5)))

# def even_numbers(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i

# for num in even_numbers(10):
#     print(num)


# class SquareIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0

#     def __iter__(self):
#         return self  # returns itself as the iterator

#     def __next__(self):
#         if self.current >= self.limit:
#             raise StopIteration
#         result = self.current ** 2
#         self.current += 1
#         return result

# # Usage
# squares = SquareIterator(5)
# for num in squares:
#     print(num)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Transpose using unpacking and zip
# transpose = list(zip(*matrix))

# print(transpose)

# namedtuple is a factory function from the collections module that 
# creates tuple subclasses with named fields — making your code:
# More readable
# Immutable like tuples
# Memory-efficient

# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])

# p = Point(3, 4)
# print(p.x, p.y)         # Output: 3 4
# print(p[0], p[1])       # Still supports indexing


# functools.partial() lets you preload arguments into a function to produce a new, 
# simpler function.

# It’s like function composition or currying in functional programming.
# from functools import partial

# def add(x, y):
#     return x + y

# add_10 = partial(add, 10)

# nums = [1, 2, 3]
# result = list(map(add_10, nums))
# print(result)  # [11, 12, 13]

# from functools import partial

# def greet(title, name):
#     return f"Hello, {title} {name}"

# mr_greet = partial(greet, "Mr.")
# print(mr_greet("Anderson"))  # Hello, Mr. Anderson


# from functools import cmp_to_key

# def my_cmp(a, b):
#     if len(a) != len(b):
#         return len(a) - len(b)
#     return (a > b) - (a < b)  # Pythonic way of cmp(a, b)

# words = ['pear', 'apple', 'fig', 'banana', 'date']
# sorted_words = sorted(words, key=cmp_to_key(my_cmp))
# print(sorted_words)

# Complete Example — Fast I/O in Competitive Programming
# Problem: Given t test cases, each with two integers a and b, output their sum.

# import sys

# def main():
#     input_data = sys.stdin.read().strip().split()
#     t = int(input_data[0])
#     output = []
#     idx = 1
#     for _ in range(t):
#         a = int(input_data[idx])
#         b = int(input_data[idx+1])
#         idx += 2
#         output.append(str(a + b))
#     sys.stdout.write("\n".join(output) + "\n")

# if __name__ == "__main__":
#     main()


# def search_in_rotated_sorted_array(nums, target):
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
        
#         # If left portion is sorted
#         if nums[left] <= nums[mid]:
#             if nums[left] <= target < nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         # Right portion is sorted
#         else:
#             if nums[mid] < target <= nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
    
#     return -1


# import random

# def kth_smallest(nums, k):
#     """Returns the k-th smallest element of nums (1-based index)."""
#     return quickselect(nums, 0, len(nums)-1, k-1)  # k-1 for 0-based index

# def quickselect(arr, left, right, k_index):
#     pivot_index = random_partition(arr, left, right)
    
#     if pivot_index == k_index:
#         return arr[pivot_index]
#     elif pivot_index < k_index:
#         return quickselect(arr, pivot_index + 1, right, k_index)
#     else:
#         return quickselect(arr, left, pivot_index - 1, k_index)

# def random_partition(arr, left, right):
#     pivot_idx = random.randint(left, right)
#     arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
#     return partition(arr, left, right)

# def partition(arr, left, right):
#     pivot = arr[right]
#     i = left - 1
#     for j in range(left, right):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[right] = arr[right], arr[i + 1]
#     return i + 1
