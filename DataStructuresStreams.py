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

    squaredEvens = [ x**2 for x in array if x%2 == 0]
    print(squaredEvens) 

    ar = ["my", "name", "anthony"]
    # for number in array:
    #   print(number, end=' ')

    array.append(10)
    array.insert(2,21)
    array.remove(2)
    # array.sort()

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

    import heapq
    # Initialize a heap (as a list)
    heap = []

    # Insert elements (push)
    heapq.heappush(heap, 10)
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 20)
    heapq.heappush(heap, 1)

    # Peek (get min element without removing)
    min_element = heap[0]  # Simulating peek
    print("Peek (Min Element):", min_element)  # Output: 1

    # Remove and return the smallest element (pop)
    min_removed = heapq.heappop(heap)
    print("Popped Element:", min_removed)  # Output: 1

    # Push and pop in a single operation
    new_min = heapq.heappushpop(heap, 2)
    print("Push-Pop Operation:", new_min)  # Output: 2

    # Replace the smallest element
    replaced = heapq.heapreplace(heap, 8)
    print("Replaced Min Element:", replaced)  # Output: 5

    # Convert an existing list into a heap (heapify)
    nums = [10, 5, 3, 8, 2]
    heapq.heapify(nums)
    print("Heapified List:", nums)  # Output: [2, 5, 3, 8, 10]

    # import heapq

    # a = [1, 3, 5]
    # b = [2, 4, 6]

    # merged = heapq.merge(a, b)
    # print(list(merged))  # Output: [1, 2, 3, 4, 5, 6]

    # import heapq

    # numbers = [5, 1, 3, 10, 7, 2]
    # heapq.heapify(numbers)              # [1, 5, 2, 10, 7, 3]
    # heapq.heappush(numbers, 4)          # [1, 5, 2, 10, 7, 3, 4]
    # heapq.heappop(numbers)              # [2, 5, 3, 10, 7, 4]
    # heapq.heappushpop(numbers, 9)       # [3, 5, 4, 10, 7, 9]
    # heapq.heapreplace(numbers, 6)       # [4, 5, 6, 10, 7, 9]
    # print(heapq.nlargest(4, numbers))   # [10, 9, 7, 6]
    # print(heapq.nsmallest(4, numbers))  # [4, 5, 6, 7]

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
    del my_dict["Orange"]

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

    # Initial OrderedDict:
    # apple 3
    # banana 2
    # orange 4

    # After moving 'banana' to the end:
    # apple 3
    # orange 4
    # banana 2

    # After moving 'orange' to the start:
    # orange 4
    # apple 3
    # banana 2

    # After popping the last item:
    # Popped item: ('banana', 2)
    # orange 4
    # apple 3

    # After popping the first item:
    # Popped item: ('orange', 4)
    # apple 3

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

# import math
# a = math.inf
# print(a)

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
lambda word: [order.index(c) for c in word]

def custom_key(word):
    return [order.index(c) for c in word]

order = "cba"
word = "cab"
print([order.index(c) for c in word])  
# → [0, 2, 1]

# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         return words == sorted(words,key=lambda word:[order.index(c) for c in word])

# from typing import List

# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         order_map = {ch: i for i, ch in enumerate(order)}  # O(1) lookup
#
#         return words == sorted(words, key=lambda word: [order_map[c] for c in word])


# class Solution:
#     def isAlienSorted(self, words, order):
#         # Step 1: Create a mapping from character to its position in the alien alphabet
#         order_map = {char: index for index, char in enumerate(order)}
#
#         # Step 2: Compare each pair of adjacent words
#         for i in range(len(words) - 1):
#             word1 = words[i]
#             word2 = words[i + 1]
#
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
#
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

# 1. str.ljust(width, fillchar=' ')
# Left-justify the string, padding on the right
# s = "abc"
# print(s.ljust(6))          # 'abc   ' (pads with spaces by default)
# print(s.ljust(6, '-'))     # 'abc---' (pads with '-')

# 2. str.rjust(width, fillchar=' ')
# Right-justify the string, padding on the left
# s = "abc"
# print(s.rjust(6))          # '   abc' (pads with spaces by default)
# print(s.rjust(6, '0'))     # '000abc' (pads with '0')

# 3. str.center(width, fillchar=' ')
# Center the string, padding evenly on both sides (if odd, right side gets extra padding)
# s = "abc"
# print(s.center(7))         # '  abc  ' (pads with spaces)
# print(s.center(7, '*'))    # '**abc**'

# 4. str.zfill(width)
# Pads with zeros on the left, keeping sign if any
# s = "-42"
# print(s.zfill(5))          # '-0042'

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
#
#         prefix = strs[0]
#
#         for s in strs[1:]:
#             while not s.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                    return ""
#
#         return prefix 

# def encode(self, strs: List[str]) -> str:
#         encoded = []
#         for s in strs:
#             encoded.append(f"{len(s)}#{s}")
#             # sb.append(s.length()).append("#").append(s);
#
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
# step: how many characters to skip and direction (positive for forward, negative for backward)

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

# iterables

# # Most Important itertools Functions
# 1. permutations(iterable, r=None)
# # Returns all possible orderings of r elements from the input iterable.


# from itertools import permutations
# list(permutations([1, 2, 3], 2))  # [(1, 2), (1, 3), (2, 1), ...]
# # 2. combinations(iterable, r)
# Returns all unordered combinations of r elements.

# from itertools import combinations
# list(combinations([1, 2, 3], 2))  # [(1, 2), (1, 3), (2, 3)]
# 3. combinations_with_replacement(iterable, r)
# # Like combinations, but allows repeating elements.

# from itertools import combinations_with_replacement
# list(combinations_with_replacement([1, 2], 2))  # [(1, 1), (1, 2), (2, 2)]

# 4. product(*iterables, repeat=1)
# Cartesian product (like nested loops).

# from itertools import product
# list(product([1, 2], ['a', 'b']))  # [(1, 'a'), (1, 'b'), (2, 'a'), ...]

# # 5. chain(*iterables)
# Flatten multiple iterables into a single iterable.
# from itertools import chain
# list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# # 6. cycle(iterable)
# Infinite cycle through iterable.
# from itertools import cycle
# # Example: next(cycle([1, 2, 3]))  → keeps repeating

# 7. repeat(object, times=None)
# Repeat a single object multiple times.
# from itertools import repeat
# list(repeat(10, 3))  # [10, 10, 10]

# # 8. islice(iterable, start, stop, step=1)
# Slice an iterable (like slicing a generator).
# from itertools import islice
# list(islice(range(10), 2, 8, 2))  # [2, 4, 6]


# 9. tee(iterable, n=2)
# # Create independent iterators from a single iterable.
# from itertools import tee
# a, b = tee([1, 2, 3])

# from itertools import tee

# a, b = tee([1, 2, 3])  # creates two independent iterators
# print(list(a))         # [1, 2, 3]
# print(list(b))         # [1, 2, 3]

# 10. groupby(iterable, key=None)
# # Group adjacent elements that have the same key.
# from itertools import groupby
# data = [("a", 1), ("a", 2), ("b", 3)]
# grouped = groupby(data, key=lambda x: x[0])

# from itertools import groupby
# data = [("a", 1), ("a", 2), ("b", 3)]
# grouped = groupby(data, key=lambda x: x[0])

# result = [(key, list(group)) for key, group in grouped]
# print(result)

from itertools import groupby

data = [("a", 1), ("a", 2), ("b", 3)]

# Correct way: Materialize the group into a list immediately
grouped_list = [(k, list(g)) for k, g in groupby(data, key=lambda x: x[0])]

print(grouped_list)
# Output: [('a', [('a', 1), ('a', 2)]), ('b', [('b', 3)])]

# Character Type Check Methods (on strings):
# Method	Description
# str.isalpha()	Returns True if all characters are alphabetic (a–z, A–Z) and string is non-empty.
# str.isdigit()	Returns True if all characters are digits (0–9).
# str.isalnum()	Returns True if all characters are alphanumeric (a–z, A–Z, 0–9).
# str.islower()	Returns True if all cased characters are lowercase, and there’s at least one cased character.
# str.isupper()	Returns True if all cased characters are uppercase, and there’s at least one cased character.
# str.isspace()	Returns True if all characters are whitespace (' ', \t, \n, etc.).
# str.istitle()	Returns True if string is in title case (e.g., "Hello World").
# str.isnumeric()	Returns True if all characters are numeric, including digits and other unicode numerals like superscripts.
# str.isdecimal()	Returns True if all characters are decimal characters (0–9 only).

def rotate_string(x: str, k: int) -> str:
    n = len(x)
    if n == 0:
        return x

    k %= n
    if k == 0:
        return x

    if k > 0:
        # Right rotation
        return x[-k:] + x[:-k]
    else:
        # Left rotation
        k = -k
        return x[k:] + x[:k]


# Examples:
# rotate_string("abcdef", 2) -> "efabcd"  (right)
# rotate_string("abcdef", -2) -> "cdefab" (left)

def rotate_right(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k %= n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums

def rotate_left(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k %= n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, n - k - 1)
    reverse(n - k, n - 1)
    return nums


def rotate_array(nums, k):
    n = len(nums)
    if n == 0:
        return nums

    # k > 0 → right rotation, k < 0 → left rotation
    k %= n
    if k < 0:
        k += n  # convert negative left rotation to equivalent right rotation

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums

from collections import deque

def rotate_deque(nums, k):
    if not nums:
        return nums
    n = len(nums)
    dq = deque(nums)
    dq.rotate(k)  # k > 0 → right, k < 0 → left
    return list(dq)


def rotate_right_recursive(nums, k):
    n = len(nums)
    if n == 0 or k % n == 0:
        return nums
    k %= n
    # Base case
    if k == 0:
        return nums
    # Move last element to front
    last = nums.pop()
    nums.insert(0, last)
    return rotate_right_recursive(nums, k - 1)

def rotate_left_recursive(nums, k):
    n = len(nums)
    if n == 0 or k % n == 0:
        return nums
    k %= n
    # Base case
    if k == 0:
        return nums
    # Move first element to end
    first = nums.pop(0)
    nums.append(first)
    return rotate_left_recursive(nums, k - 1)

# from collections import deque
# def rotate_array_left(nums, k): 
#    if not nums: # return nums 
#       n = len(nums) # dq = deque(nums) 
#    dq.rotate(-(k % n)) # Negative for left rotation, modulo to avoid over-rotation # return list(dq)

# The functools module in Python provides higher-order functions and operations on callable objects. It’s essential for writing cleaner, more efficient, and functional-style code.

# Here are the most important functools functions with usage examples:

# ✅ 1. lru_cache – Caching / Memoization
# Caches the result of function calls to improve performance, especially for expensive computations.


from functools import lru_cache
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))  # Fast due to caching

# ✅ 2. partial – Fixes some arguments of a function
# Used to create a new version of a function with some arguments preset.
from functools import partial
def power(base, exponent):
    return base ** exponent
square = partial(power, exponent=2)
print(square(5))  # 25

# ✅ 3. reduce – Reduces a sequence to a single value
# Applies a function cumulatively to the items of an iterable.

from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24

# ✅ 4. cmp_to_key – Convert old-style comparison to key function
# Used to convert a comparison function into a key for sorted().

from functools import cmp_to_key
def compare(x, y):
    return (x > y) - (x < y)  # classic cmp style

def compare(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0

from functools import cmp_to_key

def compare(x, y):
    return (x > y) - (x < y)


def compare(x, y):
    if x < y:
        return 1
    elif x > y:
        return -1
    else:
        return 0

from functools import cmp_to_key

lists = [2,5,1,68,0,4]

print(sorted(lists, key = cmp_to_key(compare)) )
[68, 5, 4, 2, 1, 0]

# ✅ 5. wraps – Preserve metadata in decorators
# Used when writing decorators to maintain original function’s metadata (name, docstring).

from functools import wraps

def my_decorator(func):
    @wraps(func) # Preserves metadata like __name__ and docstrings
    def wrappersing(*args, **kwargs):
        print("Hello from decorator")
        result = func(*args, **kwargs) # Pass arguments through
        return result # Return the actual function result
    return wrappersing
        
@my_decorator
def say_hello():
    """Says hello"""
    print("Hello!")

# Scenario A: Checking the function name
print(f"Function name is: {say_hello.__name__}") 

# Scenario B: Executing and getting the return value
say_hello() # say_hello (not 'wrapper')

# ✅ 6. cache (Python 3.9+) – Unbounded version of lru_cache
# Just like lru_cache but with no size limit.
# from functools import cache

# @cache
# def slow_add(x, y):
#     return x + y

# print(slow_add(2, 3))  # 5

# ✅ 7. total_ordering – Auto-complete comparison methods
# Simplifies writing rich comparison methods (<, <=, etc.).
# from functools import total_ordering

# @total_ordering
# class Person:
#     def __init__(self, age):
#         self.age = age

#     def __eq__(self, other):
#         return self.age == other.age

#     def __lt__(self, other):
#         return self.age < other.age

# p1 = Person(25)
# p2 = Person(30)
# print(p1 <= p2)  # True

######### Summary Table #########

# Function	        Use Case
# lru_cache	        Memoization with limited cache size
# cache	            Infinite cache (Python 3.9+)
# partial	        Pre-fill some arguments of a function
# reduce	        Cumulative reduction of iterable
# cmp_to_key	    Old-style comparison in sorting
# wraps	Preserve    function metadata in decorators
# total_ordering	Auto-implement comparison methods

# Got it! Let’s talk about index vs startswith in Python strings, 
# and then I’ll list the most important string methods you should know.

# 1. str.index(sub[, start[, end]])
# Finds the first occurrence of substring sub in the string.
# Returns the lowest index where sub starts.
# Raises ValueError if sub is not found.
# Optional start and end let you search within a substring slice.

# s = "hello world"
# print(s.index("o"))       # 4 (first 'o' at index 4)
# print(s.index("o", 5))    # 7 (search starting from index 5)
# # print(s.index("z"))     # Raises ValueError: substring not found
# 2. str.startswith(prefix[, start[, end]])
# Returns True if the string starts with the given prefix (can be a string or tuple of strings).
# Optional start and end restrict the check to a substring slice.
# Does not raise error, just returns False if no match.

# s = "hello world"
# print(s.startswith("he"))       # True
# print(s.startswith("wo", 6))    # True (checks substring from index 6)
# print(s.startswith("Wo"))       # False (case-sensitive)
# Key difference:
# Aspect	        index()	startswith()
# Purpose	        Find position of substring	Check if string starts with prefix
# Return type	    Integer (index)	Boolean (True/False)
# Behavior on no match	Raises ValueError	Returns False
# Can search inside substring with start/end	Yes	Yes

# Most Important Python String Methods
# Method	What it does	Example
# len(s)	Length of string	len("abc") → 3
# s.lower()	Converts string to lowercase	"Hello".lower() → "hello"
# s.upper()	Converts string to uppercase	"hello".upper() → "HELLO"
# s.strip()	Removes leading and trailing whitespace	" hello ".strip() → "hello"
# s.lstrip() / s.rstrip()	Removes leading/trailing whitespace	" hi ".lstrip() → "hi "
# s.find(sub)	Returns lowest index of substring or -1 if not found	"abc".find("b") → 1
# s.index(sub)	Same as find but raises error if not found	"abc".index("b") → 1
# s.startswith(prefix)	Checks if string starts with prefix	"abc".startswith("a") → True
# s.endswith(suffix)	Checks if string ends with suffix	"abc".endswith("c") → True
# s.replace(old, new)	Replace all occurrences of substring	"abcabc".replace("a", "x") → "xbcxbc"
# s.split(sep=None)	Split string into list by separator	"a,b,c".split(",") → ["a", "b", "c"]
# sep.join(list_of_strings)	Join list elements into a string separated by sep	",".join(["a","b"]) → "a,b"
# s.isdigit()	Returns True if all characters are digits	"123".isdigit() → True
# s.isalpha()	Returns True if all characters are alphabetic	"abc".isalpha() → True
# s.count(sub)	Counts occurrences of substring	"abab".count("ab") → 2


#A dictionary in Python is a mutable, unordered collection of key-value pairs. It’s also called a hash map in other languages.

# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)

# 1. Dictionary Creation
# a) Using curly braces
d = {"a": 1, "b": 2}

# b) Using dict() constructor
d = dict(a=1, b=2)  # keys are strings

# c) Using fromkeys()
# Creates a dict with default value.
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)  # {'a':0, 'b':0, 'c':0}

# 2. Accessing Elements
# a) Using keys
print(my_dict['name'])  # Alice

# b) Using get() (safer)
print(my_dict.get('name'))  # Alice
print(my_dict.get('salary', 0))  # 0, default if key not found

# Tip for interviews: get() prevents KeyError; always consider it for optional keys.
# 3. Updating Dictionary
# a) Adding new key-value pair
my_dict['salary'] = 50000

# b) Updating multiple keys using update()
my_dict.update({"age": 26, "city": "Boston"})

# 4. Deleting Elements
# del keyword
del my_dict['city']

# pop() (removes and returns value)
salary = my_dict.pop('salary')

# popitem() (removes last inserted key-value pair)
last_item = my_dict.popitem()
# clear() (empties dictionary)
my_dict.clear()

# 5. Iterating Over Dictionary
# a) Keys
for key in my_dict:
    print(key)

# b) Values
for value in my_dict.values():
    print(value)

# c) Items (key-value pairs)
for key, value in my_dict.items():
    print(key, value)

# 6. Dictionary Comprehensions
# Powerful feature for transforming or filtering dicts.
# Square numbers
nums = [1, 2, 3]
squares = {x: x**2 for x in nums}  # {1:1, 2:4, 3:9}

# Filter even numbers
even_squares = {x: x**2 for x in nums if x % 2 == 0}  # {2:4}

# Interview Tip: Dictionary comprehension is often asked for transforming input to a mapping in one line.

# 7. Advanced Dictionary Methods
# Method	                Description
# setdefault(key, default)	Returns the value if key exists, else sets it to default.
# copy()	                Returns a shallow copy of dict.
dict.items()	# Returns view object of key-value pairs.
dict.keys()	    # Returns view of keys.
dict.values()	# Returns view of values.

# Example:
my_dict.setdefault('age', 30)  # returns 26 (existing)
my_dict.setdefault('country', 'USA')  # adds 'country': 'USA'

# 8. Merging Dictionaries
# a) Using update()

d1 = {'a':1}
d2 = {'b':2}
d1.update(d2)  # {'a':1, 'b':2'}

# b) Using | operator (Python 3.9+)
d3 = d1 | d2

# c) Using ChainMap (Python 3.3+)
from collections import ChainMap
d = ChainMap(d1, d2)  # searches in d1 first, then d2

# 9. Nested Dictionaries
users = {
    "alice": {"age": 25, "city": "NY"},
    "bob": {"age": 30, "city": "LA"}
}
print(users["alice"]["city"])  # NY

# a) Updating nested values
users["alice"]["age"] = 26
# b) Safely accessing nested keys
age = users.get("alice", {}).get("age", 0)

# 10. Dictionary Sorting
# Python dicts are insertion-ordered (Python 3.7+), but you may want sorted by key or value.

d = {'b': 2, 'a': 1, 'c': 3}

# Sort by key
sorted_by_key = dict(sorted(d.items()))  # {'a':1, 'b':2, 'c':3}

# Sort by value
sorted_by_value = dict(sorted(d.items(), key=lambda item: item[1]))  # {'a':1,'b':2,'c':3}

# 11. Common Interview Patterns
# a) Frequency Counter
from collections import Counter
arr = [1,2,2,3,3,3]
freq = Counter(arr)  # {1:1, 2:2, 3:3}

# b) Grouping items
from collections import defaultdict
words = ["apple", "bat", "banana"]
group = defaultdict(list)
for word in words:
    group[len(word)].append(word)
# group: {5:['apple'], 3:['bat'], 6:['banana']}

# c) Two-sum problem (using dictionary)
nums = [2,7,11,15]
target = 9
d = {}
for i, num in enumerate(nums):
    if target - num in d:
        print(d[target-num], i)
    d[num] = i

# Interview Tip: Using a dictionary reduces nested loops to O(n) time complexity.
# 12. Dictionary Tricks
# Defaultdict for automatic initialization

from collections import defaultdict
d = defaultdict(int)
d['a'] += 1  # No KeyError

# Dictionary unpacking
d1 = {'a':1}
d2 = {'b':2}
d3 = {**d1, **d2}  # Merge dicts

# Mapping with map() and comprehension
numbers = [1,2,3]
squared_dict = {x:x**2 for x in map(int, numbers)}

# Using enumerate for index-value mapping
lst = ['a','b','c']
index_dict = {val: idx for idx, val in enumerate(lst)}  # {'a':0, 'b':1, 'c':2}

# 13. Performance Tips
# Dictionaries have O(1) average case for get, set, pop.
# For large datasets:
# Use defaultdict or Counter to avoid repetitive checks.
# Minimize nested loops by leveraging dictionaries as lookup tables.
# Python dictionaries are memory-efficient but have hashing overhead.

# 14. Pitfalls / Gotchas
# Mutable keys not allowed:
d = {[1,2]: "value"}  # Error! list is unhashable

# Order before Python 3.7:
# Dictionaries were unordered, so iterations may not be deterministic.

# Shallow copy:
d1 = {'a':[1,2]}
d2 = d1.copy()
d2['a'].append(3)
print(d1['a'])  # [1,2,3] -> points to same list

# Accessing missing keys without get
d = {}
d['x']  # KeyError

# ✅ Key Takeaways for Interviews
# Know basic CRUD operations.
# Understand get, setdefault, update, pop, popitem.
# Be comfortable with nested dictionaries and safe access.
# Use dictionary comprehensions for transformation.
# Use dictionaries for lookup optimization, e.g., two-sum, grouping.
# Understand defaultdict, Counter, ChainMap for advanced scenarios.
# Avoid mutable keys and remember shallow copy issues.

# 1. Python sort() and sorted()
# Python provides two ways to sort lists:
# 1.1 Using list.sort()
# Sorts a list in-place (modifies the original list).
# Default is ascending order.
# Can accept a key function and a reverse flag.
# Example:

numbers = [5, 2, 9, 1, 7]

# In-place sort
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 7, 9]

# Descending sort
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 7, 5, 2, 1]

# Sort by a key (length of string)
words = ["apple", "banana", "kiwi", "cherry"]
words.sort(key=len)
print(words)  # Output: ['kiwi', 'apple', 'banana', 'cherry']

# 1.2 Using sorted()
# Returns a new sorted list without modifying the original.

numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 5, 7, 9]
print(numbers)         # [5, 2, 9, 1, 7] (original unchanged)

# 2. Python bisect Module
# The bisect module helps you insert elements in a sorted list while maintaining order. It also helps to find insertion points efficiently using binary search.

import bisect

# 2.1 bisect.bisect_left(list, x)
# Returns the index where x should be inserted to maintain order.
# Inserts before any existing entries of x.

import bisect

numbers = [1, 3, 4, 4, 7]
index = bisect.bisect_left(numbers, 4)
print(index)  # Output: 2

# 2.2 bisect.bisect_right(list, x) / bisect.bisect(list, x)
# Returns the index after any existing entries of x.

index = bisect.bisect_right(numbers, 4)
print(index)  # Output: 4

# Difference:
# bisect_left → insert before duplicates.
# bisect_right → insert after duplicates.

# 3. Python insort Functions
# The insort functions combine bisect and insert. They insert an element into a sorted list, keeping it sorted.

3.1 bisect.insort_left(list, x)

# Inserts x before existing duplicates.

numbers = [1, 3, 4, 4, 7]
bisect.insort_left(numbers, 4)
print(numbers)  # Output: [1, 3, 4, 4, 4, 7]

3.2 bisect.insort_right(list, x) / bisect.insort(list, x)

# Inserts x after existing duplicates.

numbers = [1, 3, 4, 4, 7]
bisect.insort_right(numbers, 4)
print(numbers)  # Output: [1, 3, 4, 4, 4, 7]


# Use case:
# insort is faster than manually sorting after each insertion, because it uses binary search to find the correct insertion index (O(log n)) and inserts at that position (O(n) for the shift).
# 4. Practical Example: Maintaining a Sorted List
import bisect

# Start with empty list
sorted_list = []

# Insert elements in arbitrary order
for num in [5, 1, 8, 3, 7]:
    bisect.insort(sorted_list, num)
    print(f"After inserting {num}: {sorted_list}")

# Output:
# After inserting 5: [5]
# After inserting 1: [1, 5]
# After inserting 8: [1, 5, 8]
# After inserting 3: [1, 3, 5, 8]
# After inserting 7: [1, 3, 5, 7, 8]


# Notice how the list always stays sorted.

# 5. Summary Table
# Function	Purpose	Notes
# list.sort()	Sorts list in place	O(n log n)
# sorted(list)	Returns new sorted list	O(n log n)
# bisect.bisect_left(l,x)	Find index to insert x before duplicates	O(log n)
# bisect.bisect_right(l,x) / bisect.bisect(l,x)	Find index to insert x after duplicates	O(log n)
# bisect.insort_left(l,x)	Insert x in sorted list before duplicates	O(n) for insertion
# bisect.insort_right(l,x) / bisect.insort(l,x)	Insert x in sorted list after duplicates

# from functools import cmp_to_key

# arr = [5, 2, 8, 1]

# asc = lambda x, y: (x > y) - (x < y)
# desc = lambda x, y: -((x > y) - (x < y))

# print(sorted(arr, key=cmp_to_key(asc)))   # [1, 2, 5, 8]
# print(sorted(arr, key=cmp_to_key(desc)))  # [8, 5, 2, 1]
# ✅ Final summary (for ascending):

# Comparator return	Meaning	Effect
# -1	x < y	Keep order
# 0	x == y	Keep
# +1	x > y	Swap (reverse just this pair)

# So to answer your question directly:

# ❌ No, return 1 does not mean “keep as is.”
# ✅ It means “swap the two elements” (for ascending).
# return -1 means “keep them as-is.”

# You said:
# if i hav 4 5 
# 4<5 lambda becomes return -1-(-1) = 0 no change
# 6>5 lambda is (1)-(?

# ChatGPT said:
# Perfect — you’re thinking exactly the right way 👏
# Let’s slow it down carefully and compute it step by step so you never get confused again.

# lambda x, y: (x > y) - (x < y)
# Now let’s apply it case by case.

# 🧠 Case 1: x = 4, y = 5
# Check each part:
# (x > y) → (4 > 5) → False → 0
# (x < y) → (4 < 5) → True → 1
# So result =
# (x > y) - (x < y) = 0 - 1 = -1

# ✅ Return = -1
# Meaning (for ascending sort):
# → x (4) is smaller than y (5),
# → keep order (4 before 5).

# So output stays [4, 5]
# 🧠 Case 2: x = 6, y = 5
# Check again:

# (x > y) → (6 > 5) → True → 1
# (x < y) → (6 < 5) → False → 0
# So result =
# (x > y) - (x < y) = 1 - 0 = +1

# ✅ Return = +1
# Meaning (for ascending sort):
# → x (6) is greater than y (5),
# → swap them (put 5 before 6).
# So output becomes [5, 6]

# (x > y) - (x < y) → ascending
# -1 = keep order

# +1 = swap
# -((x > y) - (x < y)) → descending
# -1 = swap
# +1 = keep order

# Dictionary creations WAYS
# Sequence of key-value pairs
student_dict2 = dict(name="Jane Doe", age=22, courses=["Biology", "Chemistry"])
student ={}
# From another dictionary
student_dict_combined = dict(student, **student_dict2)

keys = ["a", "b", "c"]
values = [1, 2, 3]

zipped = zip(keys, values)
dict_from_zip = dict(zipped) # Result: {"a": 1, "b": 2, "c": 3}

# Using the `dict()` constructor
student_dict = dict([
    ("name", "John Doe"),
    ("age", 21),
    ("courses", ["Math", "Physics"])
])

# Using the shorthand syntax
student_dict_short = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Physics"]
}


# 1. Mental Model
# bisect_left(x)
# Returns:
# First position where x can be inserted
# or
# First element >= x
# bisect_right(x)
# Returns:
# Last position where x can be inserted
# or
# First element > x

import bisect

arr = [1,2,3,4,6,7,9]

print(bisect.bisect_left(arr,4) )
print(bisect.bisect_right(arr,4) )
3
4

arr = [1,2,3,4,4,4,6,7,9]

print(bisect.bisect_left(arr,4) )
print(bisect.bisect_right(arr,4) )
3
6


arr = [1,2,3,6,7,9]

print(bisect.bisect_left(arr,4) )
print(bisect.bisect_right(arr,4) )
3
3
