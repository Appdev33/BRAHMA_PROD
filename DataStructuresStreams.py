
from functools import reduce
import random
from collections import deque
import heapq
from sortedcontainers import SortedDict
from collections import defaultdict
from collections import OrderedDict
from itertools import count

def main() -> None:

    # ARRAYS

    print("**********************ARRAYS/LIST*************************")
    array = [1,2,3,4,5,6,7]
    squares = [x**2 for x in array]
    print(squares)   

    squaredEvens = [ x**3 for x in array if x%2 == 0]
    print(squaredEvens) 

    ar = ["my", "name", "anthony"]

    # for number in array:
    #   print(number, end=' ')

    array.append(10)
    array.insert(2,21)
    array.remove(2)
    # array.sort()
    print()
    # array.append(ar)
    array.extend(ar)

    # subarray = array[1:4]
    # print(subarray, end=' ')

    # for number in array:
    #     print(array, end=' ')


    # [expression for item in iterable if condition] 
    # Lambda with map or filter:
    # With map: map(lambda x: expression, iterable)
    # With filter: filter(lambda x: condition, iterable)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Step 1: Filter out even numbers using filter and lambda
    even_numbers = filter(lambda x: x % 2 == 0, numbers)

    # Step 2: Square the filtered even numbers using map and lambda
    squared_evens = map(lambda x: x ** 2, even_numbers)
    
    sum_of_squares_of_evens = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
)
    # print(sum_of_squares_of_evens)
    # print(list(squared_evens))
    res = reduce(lambda x,y : x-y, numbers)
    print(res)

    has_positive = any(map(lambda x: x > 0, numbers))
    sorted_numbers = sorted(numbers, key=lambda x: x)
    
    # Sort based on the second element in descending order
    tuples = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
    sorted_tuples = sorted(tuples, key=lambda x: x[1], reverse=True)
    print(sorted_tuples)  # Output: [(3, 'cherry'), (2, 'banana'), (1, 'apple')]

    # from operator import itemgetter
    # tuples = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
    # sorted_tuples = sorted(tuples, key=itemgetter(1), reverse=True)

    all_positive = all(map(lambda x: x > 0, numbers))
    print(sorted_numbers)

    names = ['Alice', 'Bob', 'Charlie']
    ages = [30, 25, 35]
    combined = list(zip(names, ages))  # Combines names and ages
    print(combined)

    fruits = ['apple', 'banana', 'cherry']
    for index, fruit in enumerate(fruits):
        print(index, fruit)

    # Set comprehension
    unique_squared = {x ** 2 for x in [1, 2, 2, 3]}  # Unique squares
    print(unique_squared)  # Output: {1, 4, 9}
    # {} make above unique

    # Dictionary comprehension
    squared_dict = {x: x ** 2 for x in range(5)}  # Creates a dict of squares
    print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}    

    #  STACKS 
    print("**********************STACKS/LIST*************************")
    stack = []
    stack.append("23")
    stack.append("44")


    top = stack[-1]
    pop = stack.pop()
    sizeStack = len(stack)
    print(f"Stack functions printing: {top}  {pop}  {sizeStack}  {stack}")
    stack.append(random.randint(0, 100))

    print(stack)
    
    # Step 1: Convert and filter the stack
    converted_stack = filter(lambda x: x is not None, map(safe_convert, stack))

    # Step 2: Filter for numbers <= 20 and then square them
    filtered_and_squared = map(lambda x: x ** 2, filter(lambda x: x >= 20, converted_stack))

    # Convert to a list to see the result
    print(list(filtered_and_squared))

    print("**********************LINKED LIST*************************")
    linked_list = deque()
    linked_list.append(20)
    linked_list.append(23)

    print(f" {linked_list} {linked_list.pop()} {linked_list.appendleft(44) }")

    resLL = list(x*x for x in linked_list)
    print(resLL)

    print("**********************QUEUE*************************")
    q = deque()
    q.extend(numbers)
    # print(q)
    for i in q:
        if i%2 ==0: 
            print(i)

    dequeued_element = q.popleft()  
    print("Dequeued element:", dequeued_element)     

    print("**********************PRIORITY QUEUE/ HEAPS*************************")

    minHeap = []

    heapq.heappush(minHeap,21)   
    heapq.heappush(minHeap,26)
    heapq.heappush(minHeap,1)
    heapq.heappush(minHeap,2)
    print(minHeap)
    print()  
    removed_element = heapq.heappop(minHeap)
    print("Removed element:", removed_element) 
    removed_element = heapq.heappop(minHeap)
    print("Removed element:", removed_element) 

    maxHeap = []
    heapq.heappush(maxHeap, -3)
    heapq.heappush(maxHeap, -1)
    heapq.heappush(maxHeap, -5)

    print(maxHeap)
    print(heapq.heappop(maxHeap)) 

    print("**********************DEQUEUE*************************")
    dq = deque()
    dq.extend(numbers)

    print(list(dq))
    dq.appendleft(99)  # Add to front
    dq.append(12)      # Add to rear

    # Remove elements from the front and rear
    print("Removed from front:", dq.popleft())  # Output: 10
    print("Removed from rear:", dq.pop()) 

    print("Front element:", dq[0])  # Output: 5
    print("Rear element:", dq[-1])  # Output: 30

    filtered_dq = deque(filter(lambda x: x <4, dq))
    print(filtered_dq)

    print("**********************MAP/DICT*************************")

    my_dict = {"Apple": 50, "Banana": 30, "Orange": 20}

    print("Contains key 'Banana'? ", "Banana" in my_dict)  # Output: True

    # Remove a key-value pair
    my_dict.pop("Orange")

    # Iterate through the dictionary (keys and values)
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")

    for key in my_dict:
        print("Key:", key)
    
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")

    # Python doesn't have forEach, but you can use dictionary comprehension
    print({key: value for key, value in my_dict.items()})

    for index, (key, value) in enumerate(my_dict.items()):
        print(f"Index: {index}, Key: {key}, Value: {value}")

    filtered_dict = {k: v for k, v in my_dict.items() if v > 25}
    print( filtered_dict)

    keys = ["Apple", "Banana", "Orange"]
    values = [10, 15, 20]

    # Loop to add key-value pairs to the dictionary
    for i in range(len(keys)):
        my_dict[keys[i]] = values[i]

    for key, value in zip(keys, values):
        my_dict[key] = value    

    for key, value in zip(keys, values):
        if value > 10:
            my_dict[key] = value

    print("**********************TREE MAP*************************")

    treeMap = SortedDict()
    entries = [
        ("Banana", 30),
        ("Apple", 50),
        ("Orange", 20),
        ("Grapes", 40),
        ("Mango", 60),
    ]

    for key, value in entries:
        treeMap[key] = value

    print(treeMap)    

    key_to_check = "Mango"    

    print(f"Contains key '{key_to_check}'? ", key_to_check in treeMap) 

    for key, value in treeMap.items():
        print(f"Key: {key}, Value: {value}")
    
    filtered_dict = SortedDict(filter(lambda item: item[1] > 30, treeMap.items()))
    print("Filtered entries (value > 30):", filtered_dict)

    print("**********************SET*************************")

    my_set = set(range(0,100))
    my_set.add(999)
    my_set.discard(99)

    filtered_set = set(filter(lambda item: item>55, my_set))
    print("Filtered set (items starting with 'B'):", filtered_set)

    print("**********************TREE SET*************************")

    # Create a set of numbers (from 1 to 10)
    number_set = set(range(1, 11))

    # Sort the set (simulating TreeSet behavior)
    sorted_set = sorted(number_set)

    # Display the sorted set
    print("Sorted set of numbers (TreeSet equivalent):", sorted_set)

    # Python: Set elements can be sorted using sorted(), but the original set remains unordered.
    #  To simulate the behavior of a TreeSet, you have to explicitly sort the set when needed.
    # print("**********************SORTED SET*************************") 

    print("**********************DEFAULT DICT*************************") 

    # Create a defaultdict with default type as int
    d = defaultdict(int)

    # Adding elements
    d['apple'] += 1
    d['banana'] += 2

    print("DefaultDict:", d)  # Output: {'apple': 1, 'banana': 2}

    # Accessing a non-existent key provides the default value
    print("Grapes:", d['grapes'])  # Output: Grapes: 0

    # Iterate through elements
    for key, value in d.items():
        print(f"{key}: {value}")  # Output: apple: 1, banana: 2, grapes: 0

    # Use defaultdict for counting occurrences
    words = ['apple', 'banana', 'apple', 'orange']
    count = defaultdict(int)

    for word in words:
        count[word] += 1

    print("Word Count:", count)  # Output: {'apple': 2, 'banana': 1, 'orange': 1}

    print("**********************ORDERED DICT*************************") 

    # OrderedDict is a part of the collections module in Python that maintains the order of keys based on the order in
    # which they are inserted into the dictionary.


    # Create an OrderedDict and insert items
    od = OrderedDict()
    od['apple'] = 3
    od['banana'] = 2
    od['orange'] = 4

    # Print the OrderedDict
    print("Initial OrderedDict:")
    for key, value in od.items():
        print(key, value)

    # Move 'banana' to the end
    od.move_to_end('banana')
    print("\nAfter moving 'banana' to the end:")
    for key, value in od.items():
        print(key, value)

    # Move 'orange' to the start
    od.move_to_end('orange', last=False)
    print("\nAfter moving 'orange' to the start:")
    for key, value in od.items():
        print(key, value)

    # Remove and return the last item
    last_item = od.popitem()
    print("\nAfter popping the last item:")
    print("Popped item:", last_item)
    for key, value in od.items():
        print(key, value)

    # Remove and return the first item
    first_item = od.popitem(last=False)
    print("\nAfter popping the first item:")
    print("Popped item:", first_item)
    for key, value in od.items():
        print(key, value)

    # Reinsert items and sort by values using a lambda function
    od['apple'] = 3
    od['banana'] = 2
    od['orange'] = 4

    # Sort the OrderedDict by values
    sorted_ordered_dict = OrderedDict(sorted(od.items(), key=lambda x: x[1]))
    print("\nAfter sorting by values:")
    for key, value in sorted_ordered_dict.items():
        print(key, value)


print("**********************DECORATORS*************************")

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Code to execute before calling the original function
        print("Something before the original function.")

        # Call the original function
        result = original_function(*args, **kwargs)

        # Code to execute after calling the original function
        print("Something after the original function.")

        return result

    return wrapper_function

@decorator_function
def display():
    print("Display function executed.")



# Calling the decorated function
display()    

print("**********************ITERATORS*************************")
# In Python, an iterator is an object that can be iterated upon, meaning you can traverse through all its elements one at a time.
# It implements two special methods:

# __iter__() – Returns the iterator object itself and is called at the start of loops like for.
# __next__() – Returns the next item in the sequence, and raises StopIteration when there are no more items.


list = [10,20,30,40,50,60,70]
my_iter = iter(list)
print(next(my_iter))

# with open('sample.txt', 'r') as file:
#     file_iterator = iter(file)
#     for line in file_iterator:
#         print(line.strip())

for num in count(10, 2):  # Starts at 10, increments by 2
    if num > 20:
        break
    print(num)

# from itertools import cycle

# colors = ["red", "green", "blue"]
# color_cycle = cycle(colors)

# # Usage (we'll only print the first 6 items to avoid an infinite loop)
# for _ in range(6):
#     print(next(color_cycle))


print("**********************MONKEY PATCHING*************************")

# Monkey patching is a technique in Python where you dynamically modify or extend existing classes or modules at runtime.
# This can be used to add new methods, override existing methods, or alter the behavior of classes or modules without changing
# their original source code.

# While powerful, monkey patching should be used sparingly because it can make code harder to understand, maintain, and debug. 
# It’s commonly used in testing or when working with libraries for which you don’t have access to the source code.

# Define a new function or method to replace the existing one
# def new_function(*args, **kwargs):
#     # Define the behavior you want
#     pass

# # Apply monkey patch by assigning the new function to the existing one
# SomeClass.some_method = new_function


class MathOperations:
    def add(self, a, b):
        return a + b

# Original usage
math_op = MathOperations()
print(math_op.add(2, 3))  # Output: 5

# Define a new function to replace `add`
def patched_add(self, a, b):
    return a * b  # Change behavior to multiplication

# Apply the monkey patch
MathOperations.add = patched_add

# Usage after patching
print(math_op.add(2, 3))  # Output: 6



print("**********************CODING SHORTCUTS************************")
# current_sum = 0
# overall_sum =float('-inf')
# overall_max = max(overall_max, current_sum)

# class Solution(object):
#     def __init__(self):
#         self.mp = {}

#     def recur(self, a, b):
#         if a <= 0 and b <= 0:
#             return 0.5
#         if a <= 0 and b > 0:
#             return 1
#         if a > 0 and b <= 0:
#             return 0
#         if (a, b) in self.mp:
#             return self.mp[(a, b)]

#         op1 = self.recur(a - 100, b)
#         op2 = self.recur(a - 75, b - 25)
#         op3 = self.recur(a - 50, b - 50)
#         op4 = self.recur(a - 25, b - 75)

#         self.mp[(a, b)] = 0.25 * (op1 + op2 + op3 + op4)
#         return self.mp[(a, b)]

#     def soupServings(self, n):
#         if n >= 4800:
#             return 1
#         ans = self.recur(n, n)
#         return ans

# array = []
# for i in range(m):
#     array.append([0] * n)

# # Lengths of the input strings
#     m, n = len(str1), len(str2)
    
#     # Initialize a 2D array to store the edit distances
#     dp = [[0] * (n + 1) for _ in range(m + 1)]


# def safe_convert(x):
#     try:
#         return int(x)  # Attempt to convert to int
#     except ValueError:
#         return None  # Return None if conversion fails

# main()


