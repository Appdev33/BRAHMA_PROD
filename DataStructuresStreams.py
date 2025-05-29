from functools import reduce
import random
from collections import deque
import heapq
from sortedcontainers import SortedDict
from collections import defaultdict
from collections import OrderedDict
from itertools import count

# https://leetcode.com/discuss/study-guide/2122306/python-cheat-sheet-for-leetcode

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
    print(*range(1, 11))

    # Step 1: Filter out even numbers using filter and lambda
    even_numbers = filter(lambda x: x % 2 == 0, numbers)

    # Step 2: Square the filtered even numbers using map and lambda
    squared_evens = map(lambda x: x ** 2, even_numbers)

    # Step 3: Calculate the sum of the squares using reduce and lambda
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


    # class Solution:
    # def calPoints(self, operations: List[str]) -> int:
    #     stack = []
    #     for ops in operations:
    #         match ops:
    #             case "C":  # Remove the last valid score
    #                 if stack:
    #                     stack.pop()
    #             case "D":  # Double the last valid score
    #                 if stack:
    #                     stack.append(2 * stack[-1])
    #             case "+":  # Sum the last two valid scores
    #                 if len(stack) >= 2:
    #                     stack.append(stack[-1] + stack[-2])
    #             case _:
    #                 stack.append(int(ops))  # Convert string number to integer

    #     return sum(stack)  # Return the sum of valid scores

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

    for i in q:
        if i%2 ==0: 
            print(i)

    dequeued_element = q.popleft()  
    print("Dequeued element:", dequeued_element)   
    # popleft() removes an element from the front of the queue.
    # pop() removes an element from the end of the queue.  
    # q[0] gives you the first element (like peek()). python has no peek() method

    # Original deque: deque([10, 20, 30, 40])
    # After pop(): deque([10, 20, 30]) -> popped: 40
    # After popleft(): deque([20, 30]) -> popped: 10

    print("**********************PRIORITY QUEUE/ HEAPS*************************")

    minHeap = []

    heapq.heappush(minHeap,21)   
    heapq.heappush(minHeap,26)
    heapq.heappush(minHeap,1)
    heapq.heappush(minHeap,2)
    print(minHeap)
 
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


    # import heapq

    # # Initialize a heap (as a list)
    # heap = []

    # # Insert elements (push)
    # heapq.heappush(heap, 10)
    # heapq.heappush(heap, 5)
    # heapq.heappush(heap, 20)
    # heapq.heappush(heap, 1)

    # # Peek (get min element without removing)
    # min_element = heap[0]  # Simulating peek
    # print("Peek (Min Element):", min_element)  # Output: 1

    # # Remove and return the smallest element (pop)
    # min_removed = heapq.heappop(heap)
    # print("Popped Element:", min_removed)  # Output: 1

    # # Push and pop in a single operation
    # new_min = heapq.heappushpop(heap, 2)
    # print("Push-Pop Operation:", new_min)  # Output: 2

    # # Replace the smallest element
    # replaced = heapq.heapreplace(heap, 8)
    # print("Replaced Min Element:", replaced)  # Output: 5

    # # Convert an existing list into a heap (heapify)
    # nums = [10, 5, 3, 8, 2]
    # heapq.heapify(nums)
    # print("Heapified List:", nums)  # Output: [2, 5, 3, 8, 10]

# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         maxheap = [(-stone, stone) for stone in stones]  # Store (-stone, stone) for max-heap behavior
#         heapq.heapify(maxheap)  # Convert list into a heap

#         while len(maxheap) > 1:
#             _, first = heapq.heappop(maxheap)  # Extract max stone
#             _, second = heapq.heappop(maxheap)  # Extract second max stone

#             if first != second:
#                 heapq.heappush(maxheap, (-abs(first - second), abs(first - second)))  # Push remaining weight

#         return maxheap[0][1] if maxheap else 0  # Return last stone weight or 0 if empty
    
        

    print("**********************DEQUEUE*************************")
    # dq = deque()
    # dq.extend(numbers)

    # from collections import deque

    # Initialize with some numbers
    dq = deque([1, 2, 3])
    print("Initial deque:", dq)
    # Output: Initial deque: deque([1, 2, 3])

    # Append to the right and left
    dq.append(4)
    dq.appendleft(0)
    print("After append & appendleft:\n", dq)
    # Output: After append & appendleft:
    # deque([0, 1, 2, 3, 4])

    # Pop from the right and left
    right = dq.pop()
    left = dq.popleft()
    print("Popped from right:", right)
    # Output: 4
    print("Popped from left:", left)
    # Output: 0
    print("After pop & popleft:\n", dq)
    # Output: deque([1, 2, 3])

    # Extend right and left
    dq.extend([5, 6])
    dq.extendleft([-1, -2])
    print("After extend & extendleft:\n", dq)
    # Output: After extend & extendleft:
    # deque([-2, -1, 1, 2, 3, 5, 6])

    # Remove a specific element (first occurrence)
    dq.remove(2)
    print("After remove(2):\n", dq)
    # Output: After remove(2):
    # deque([-2, -1, 1, 3, 5, 6])

    # Reverse and rotate
    dq.reverse()
    print("After reverse:\n", dq)
    # Output: After reverse:
    # deque([6, 5, 3, 1, -1, -2])

    dq.rotate(2)
    print("After rotate(2):\n", dq)
    # Output: After rotate(2):
    # deque([1, -1, -2, 6, 5, 3])

    # Length and indexing
    print("Length:", len(dq))
    # Output: Length: 6

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

    # from collections import deque
    # first_element = my_deque[0]  # Peek first
    # last_element = my_deque[-1]  # Peek last

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

# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         return words == sorted(words,key=lambda word:[order.index(c) for c in word])

# from typing import List

# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         order_map = {ch: i for i, ch in enumerate(order)}  # O(1) lookup

#         return words == sorted(words, key=lambda word: [order_map[c] for c in word])


# class Solution:
#     def isAlienSorted(self, words, order):
#         # Step 1: Create a mapping from character to its position in the alien alphabet
#         order_map = {char: index for index, char in enumerate(order)}

#         # Step 2: Compare each pair of adjacent words
#         for i in range(len(words) - 1):
#             word1 = words[i]
#             word2 = words[i + 1]

#             # Compare character by character
#             for j in range(min(len(word1), len(word2))):
#                 if word1[j] != word2[j]:
#                     if order_map[word1[j]] > order_map[word2[j]]:
#                         return False
#                     break  # Found the first different character, stop comparing
#             else:
#                 # If we didn't find any different character, shorter word should come first
#                 if len(word1) > len(word2):
#                     return False

#         return True


# import java.util.*;

# class Solution {
#     public boolean isAlienSorted(String[] words, String order) {
#         // Step 1: Map each character to its index in the alien alphabet
#         int[] orderMap = new int[26];
#         for (int i = 0; i < order.length(); i++) {
#             orderMap[order.charAt(i) - 'a'] = i;
#         }

#         // Step 2: Compare each pair of adjacent words
#         for (int i = 0; i < words.length - 1; i++) {
#             if (!inCorrectOrder(words[i], words[i + 1], orderMap)) {
#                 return false;
#             }
#         }

#         return true;
#     }

#     private boolean inCorrectOrder(String word1, String word2, int[] orderMap) {
#         int len = Math.min(word1.length(), word2.length());

#         for (int i = 0; i < len; i++) {
#             char c1 = word1.charAt(i);
#             char c2 = word2.charAt(i);

#             if (c1 != c2) {
#                 if (orderMap[c1 - 'a'] > orderMap[c2 - 'a']) {
#                     return false;
#                 }
#                 return true;
#             }
#         }

#         // If words are same up to min length, shorter word should come first
#         return word1.length() <= word2.length();
#     }
# }


# from typing import List
# from functools import lru_cache

# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rows, cols = len(grid), len(grid[0])

#         @lru_cache(None)
#         def helper(row, col):
#             # Out of bounds → invalid path
#             if row >= rows or col >= cols:
#                 return float('inf')

#             # Base case: reached destination
#             if row == rows - 1 and col == cols - 1:
#                 print(f"Reached end: grid[{row}][{col}] = {grid[row][col]}")
#                 return grid[row][col]

#             # Recursive calls
#             down = helper(row + 1, col)
#             right = helper(row, col + 1)

#             result = grid[row][col] + min(down, right)

#             print(f"At grid[{row}][{col}] = {grid[row][col]}, min(down: {down}, right: {right}) → total: {result}")

#             return result

#         return helper(0, 0)

# a = "1010"     # Length = 4
# b = "11"       # Length = 2

# max_len = max(len(a), len(b))  # max_len = 4

# a = a.zfill(max_len)  # "1010" (unchanged)
# b = b.zfill(max_len)  # "0011" (padded)

# print(a)  # "1010"
# print(b)  # "0011"


# @lru_cache is a decorator in Python from the functools module that stands for Least Recently Used cache. 
# It helps you cache/memoize the results of expensive function calls, so that when the same inputs are used again, 
# the cached result is returned instead of recomputing the result.

# from functools import lru_cache

# @lru_cache(maxsize=3)
# def add(a, b):
#     print(f"Computing {a} + {b}")
#     return a + b

# print(add(2, 3))  # Computed
# print(add(2, 3))  # Cached
# print(add(4, 5))  # Computed
# print(add(6, 7))  # Computed
# print(add(2, 3))  # Might be recomputed if it was evicted (depends on maxsize policy)


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""

        
#         prefix = strs[0]

#         for s in strs[1:]:
#             while not s.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                    return ""


#         return prefix 
# def encode(self, strs: List[str]) -> str:
#         encoded = []
#         for s in strs:
#             encoded.append(f"{len(s)}#{s}")
#             # sb.append(s.length()).append("#").append(s);

#         return encoded


# 1. .zfill(width)
# Pads with zeros (0) on the left
# Only works on strings
# Preserves +/- signs


# "42".zfill(5)     # '00042'
# "-42".zfill(5)    # '-0042'
# "+7".zfill(4)     # '+007'

# 🧵 2. .rjust(width, fillchar=' ')
# Right-justifies the string (pads on the left)
# fillchar can be any single character


# "42".rjust(5)          # '   42'  (default fill is space)
# "42".rjust(5, '0')     # '00042'
# "42".rjust(5, '*')     # '**42'

# 🧵 3. .ljust(width, fillchar=' ')
# Left-justifies the string (pads on the right)


# "42".ljust(5)          # '42   '
# "42".ljust(5, '-')     # '42---'
# "42".ljust(5, '.')     # '42...'

# 🧵 4. .center(width, fillchar=' ')
# Centers the string with padding on both sides
# If total padding is odd, right side gets one extra char


# "42".center(6)         # '  42  '
# "42".center(7, '*')    # '**42***'
# "42".center(8, '-')    # '---42---'

# 🧵 5. str.format() or f-strings with fill/alignment specifiers
# More flexible control with formatting mini-language


# f"{'42':>5}"        # '   42' (right-align)
# f"{'42':<5}"        # '42   ' (left-align)
# f"{'42':^6}"        # ' 42  ' (center)
# f"{'42':*^6}"       # '**42**' (center with '*')
# f"{'42':0>5}"       # '00042' (right-align with '0')



# Syntax

# s[start:stop:step]
# start: index to begin (inclusive)

# stop: index to end (exclusive)

# step: how many characters to skip

# 📚 Examples
# ▶ Basic Slicing

# s = "abcdef"

# s[1:4]    # 'bcd'     (from index 1 to 3)
# s[:3]     # 'abc'     (from start to index 2)
# s[2:]     # 'cdef'    (from index 2 to end)
# s[:]      # 'abcdef'  (full string copy)
# 🔁 With Step

# s[::2]    # 'ace'     (every 2nd character)
# s[1::2]   # 'bdf'     (every 2nd character starting at index 1)
# 🔙 Reverse a String

# s[::-1]   # 'fedcba'  (reverse string)
# s[::-2]   # 'fdb'     (reverse every 2nd character)
# 📏 Using Negative Indices

# abcdef
# s[-1]     # 'f'       (last character)
# s[-3:-1]  # 'de'      (3rd-last to 2nd-last)
# s[-4:]    # 'cdef'    (last 4 characters)
# 🧪 Out of Bounds
# Python handles index overflow gracefully:


# s[0:100]  # 'abcdef'  (no error, returns until end)
# s[100:]   # ''        (empty string, index too high)
# ⚠️ Strings are Immutable
# You cannot assign using slicing:


# s[0] = 'x'   # ❌ TypeError: 'str' object does not support item assignment
# ✅ Combine Slicing + Concatenation to Modify

# s = "abcdef"
# s = s[:2] + 'Z' + s[3:]   # 'abZdef' (replaces 'c' with 'Z')
