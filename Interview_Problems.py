from collections import defaultdict

name_pairs = [
    ["Alice", "Bob"],
    ["Bob", "Charlie"],
    ["Charlie", "David"],
    ["David", "Eve"],
    ["Eve", "Frank"],
    ["Grace", "Heidi"],
    ["Heidi", "Ivan"],
    ["Ivan", "Judy"],
    ["Judy", "Karl"],
    ["Karl", "Liam"],
    ["Liam", "Mallory"],
    ["Niaj", "Olivia"],
    ["Olivia", "Peggy"],
    ["Peggy", "Quentin"],
    ["Quentin", "Rupert"],
    ["Rupert", "Sybil"],
    ["Sybil", "Trent"],
    ["Trent", "Uma"],
    ["Uma", "Victor"],
    ["Victor", "Wendy"],
    ["Wendy", "Xavier"],
    ["Yvonne", "Zack"]
]

def longest_chain(name):
    graph = defaultdict(list)
    joke_starters = set()

    for src, target in name:
        graph[src].append(target)
        joke_starters.add(src)
        joke_starters.add(target)

    visited = {}

    def dfs(node):
        if node in visited:
            return visited[node]

        max_len = 1
        for neighbor in graph[node]:
            max_len = max(max_len, 1 + dfs(neighbor))

        visited[node] = max_len
        return max_len

    # Call DFS from all possible starting points and return the longest chain
    return max(dfs(node) for node in joke_starters)
    
print(longest_chain(name_pairs))
# # Run it
# print(longest_chain(name_pairs))  # Output should be 5: Alice -> Bob -> Charlie -> David -> Eve


# from collections import Counter

# def count_valid_kings_v2(arr):
#     sums = sum(arr)
#     count = Counter(arr)
#     result = 0

#     for num in arr:
#         target = (sums - num) / 2

#         # Skip if target is not an integer (i.e., decimal)
#         if not target.is_integer():
#             continue

#         target = int(target)
        
#         if target in count:
#             if (target == num and count[num] > 1) or (target != num):
#                 result += 1

#     return result            

# # Test case
# arr = [1, 2, 3, 4]
# print(count_valid_kings_v2(arr))  # Output: 2


# find min with lexographic orderings
def smallest_lex_string(s):		
	while True:
		merged = False
		i = 0
		while i < len(s) - 1:
			a, b = int(s[i]), int(s[i + 1])
			if a + b <= 9:
				s = s[:i] + str(a + b) + s[i + 2:]
				merged = True
				break  # important: only one merge per pass
			i += 1
		if not merged:
			break
	return s


print(smallest_lex_string("3124"))   # Output: "334"
print(smallest_lex_string("32581"))    # Output: "999"  (no pairs can be merged)
print(smallest_lex_string("123456")) # Output: "2346"  (1+2=3, 3+3=6, 6+4=10 → can't do that)
	

from collections import Counter
from itertools import combinations
from math import comb

def count_good_subsequences(s):
    MOD = 10**9 + 7

    # Step 1: Count frequency of each character
    freq = Counter(s)
    # For s = "aabbcccde", freq = {'a':2, 'b':2, 'c':3, 'd':1, 'e':1}

    letters = list(freq.keys())  # ['a','b','c','d','e']
    max_freq = max(freq.values())  # Max frequency = 3 (from 'c')

    result = 0

    # Step 2: Try forming good subsequences for each frequency f (1 to max_freq)
    for f in range(1, max_freq + 1):  
        # For f = 1: look for all subsequences where each included char appears exactly once
        # For f = 2: each included char appears twice
        # For f = 3: each included char appears 3 times

        # Step 3: For all possible subset lengths (non-empty)
        for r in range(1, len(letters) + 1):  
            # subsets of size 1: (a), (b), ...
            # subsets of size 2: (a,b), (a,c), ...
            for subset in combinations(letters, r):
                valid = True
                count = 1
                for ch in subset:
                    if freq[ch] < f:
                        # If character doesn't appear at least f times, skip
                        valid = False
                        break
                    # Multiply combinations: number of ways to choose `f` instances of `ch`
                    count = (count * comb(freq[ch], f)) % MOD

                if valid:
                    # If all characters in the subset had enough frequency, add this count
                    result = (result + count) % MOD

    return result


from collections import Counter
from math import comb

def count_good_subsequences(s):
    MOD = 10**9 + 7

    freq = Counter(s)
    letters = list(freq.keys())
    n = len(letters)
    max_freq = max(freq.values())
    result = 0

    # Try all possible frequencies from 1 to max_freq
    for f in range(1, max_freq + 1):
        # Use bitmask to represent all subsets of the distinct characters
        for mask in range(1, 1 << n):  # 1 to 2^n - 1 (skip empty subset)
            count = 1
            valid = True

            for i in range(n):
                if (mask >> i) & 1:
                    ch = letters[i]
                    if freq[ch] < f:
                        valid = False
                        break
                    count = (count * comb(freq[ch], f)) % MOD

            if valid:
                result = (result + count) % MOD

    return result

# https://leetcode.com/problems/beautiful-towers-ii/
def getMaximumSumOfHeights(maxHeight):
    n = len(maxHeight)
    max_sum = 0

    for peak in range(n):
        height = [0] * n
        height[peak] = maxHeight[peak]  

        # Go left
        for i in range(peak - 1, -1, -1):
            height[i] = min(height[i + 1], maxHeight[i])

        # Go right
        for i in range(peak + 1, n):
            height[i] = min(height[i - 1], maxHeight[i])

        max_sum = max(max_sum, sum(height))  

    return max_sum


class OptimizedMessageTracker:
    def __init__(self):
        self.received = set()
        self.current_max = 0

    def receive(self, msg_id: int):
        self.received.add(msg_id)
        # Only progress current_max if the next in sequence exists
        while self.current_max + 1 in self.received:
            self.current_max += 1
            self.received.remove(self.current_max)  # Optional: frees memory

    def get_highest_contiguous(self):
        return self.current_max


tracker = OptimizedMessageTracker()
tracker.receive(1)
tracker.receive(2)
tracker.receive(4)
tracker.receive(5)
tracker.receive(6)

print(tracker.get_highest_contiguous())  # Output: 2

tracker.receive(3)
print(tracker.get_highest_contiguous())  # Output: 6

# class SparseVector:
#     def __init__(self, nums):
#         # Store only non-zero values with their indices
#         self.data = {i: val for i, val in enumerate(nums) if val != 0}
# 
#     def dot_product(self, other):
#         # Efficient dot product: loop through smaller dictionary
#         if len(self.data) > len(other.data):
#             self, other = other, self
#         return sum(val * other.data.get(i, 0) for i, val in self.data.items())
# 
#     def add(self, other):
#         result = dict(self.data)
#         for i, val in other.data.items():
#             result[i] = result.get(i, 0) + val
#         return SparseVector.from_sparse(result)
# 
#     def scalar_multiplication(self, scalar):
#         return SparseVector.from_sparse({i: val * scalar for i, val in self.data.items()})
# 
#     @classmethod
#     def from_sparse(cls, data):
#         return cls([data.get(i, 0) for i in range(max(data.keys(), default=-1) + 1)])
# 
#     def __repr__(self):
#         return f"SparseVector({self.data})"

class SparseVector:
    
    def __init__(self, nums):
        self.data = {}
        for i, val in enumerate(nums):
            if val != 0:
                self.data[i] = val

    def dot_product(self, other):
        result = 0
        for i in self.data:
            if i in other.data:
                result += self.data[i] * other.data[i]
        return result

    def add(self, other):
        result = dict(self.data)
        for i in other.data:
            if i in result:
                result[i] += other.data[i]
            else:
                result[i] = other.data[i]
        return SparseVector.from_dict(result)

    def scalar_multiplication(self, scalar):
        result = {}
        for i, val in self.data.items():
            result[i] = scalar * val
        return SparseVector.from_dict(result)

    @staticmethod
    def from_dict(data):
        max_index = max(data.keys(), default=-1)
        full = [0] * (max_index + 1)
        for i, val in data.items():
            full[i] = val
        return SparseVector(full)

    def __repr__(self):
        return str(self.data)


a = SparseVector([0, 3, 0, 0, 4])
b = SparseVector([0, 0, 0, 5, 2])

print("Dot product:", a.dot_product(b))          # Output: 8
print("Addition:", a.add(b))                     # Output: {1: 3, 3: 5, 4: 6}
print("Scalar multiplication:", a.scalar_multiplication(2))  # Output: {1: 6, 4: 8}

		
class Vector2D:
    def __init__(self, vec):
        self.vec = vec
        self.row = 0
        self.col = 0

    def _advance(self):
        # Skip empty rows or when the current row is exhausted
        while self.row < len(self.vec) and self.col >= len(self.vec[self.row]):
            self.row += 1
            self.col = 0

    def next(self):
        if self.hasNext():  # Check first if there's a next element
            result = self.vec[self.row][self.col]
            self.col += 1
            return result
        else:
            raise Exception("No more elements")

    def hasNext(self):
        self._advance()
        return self.row < len(self.vec)

v = Vector2D([[1, 2], [], [3], [], [], [4, 5]])
while v.hasNext():
    print(v.next(), end=" ")
# Output: 1 2 3 4 5


from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.front = Node(None, None)
        self.rear = Node(None, None)
        self.front.next = self.rear
        self.rear.prev = self.front

    def append_front(self, node):
        node.next = self.front.next
        node.prev = self.front
        self.front.next.prev = node
        self.front.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_rear(self):
        if self.is_empty():
            return None
        node = self.rear.prev
        self.remove(node)
        return node

    def is_empty(self):
        return self.front.next == self.rear

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = {}                     # key -> Node
        self.freq_to_dll = defaultdict(DoubleLinkedList)  # freq -> DLL
        self.min_freq = 0
        self.size = 0

    def _update_freq(self, node):
        freq = node.freq
        self.freq_to_dll[freq].remove(node)

        # Update min_freq if needed
        if freq == self.min_freq and self.freq_to_dll[freq].is_empty():
            self.min_freq += 1

        node.freq += 1
        self.freq_to_dll[node.freq].append_front(node)

    def get(self, key):
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self._update_freq(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._update_freq(node)
        else:
            if self.size == self.capacity:
                # Evict least freq node from min_freq list
                lfu_list = self.freq_to_dll[self.min_freq]
                evict_node = lfu_list.pop_rear()
                if evict_node:
                    del self.key_to_node[evict_node.key]
                    self.size -= 1

            # Add new node
            new_node = Node(key, value)
            self.freq_to_dll[1].append_front(new_node)
            self.key_to_node[key] = new_node
            self.min_freq = 1
            self.size += 1

# design TrieData Structure

class TrieNode:
    def __init__(self):
        self.children = {}           # ✅ Removed 'val = c' (undefined variable 'c')
        self.isEndWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()  # ✅ Added parentheses to instantiate TrieNode
            curr = curr.children[ch]
        curr.isEndWord = True

    def contains_word(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.isEndWord

    def is_prefix(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True

    def delete_word(self, node, word, depth):
        if node is None:
            return False

        if depth == len(word):
            if not node.isEndWord:
                return False
            node.isEndWord = False  # ✅ Corrected: was just accessing it, not modifying
            return len(node.children) == 0  # ✅ Return true if node has no children (safe to delete)

        ch = word[depth]
        if ch not in node.children:
            return False

        should_delete = self.delete_word(node.children[ch], word, depth + 1)

        if should_delete:
            del node.children[ch]  # ✅ Corrected: used 'del', not 'delete'
            return len(node.children) == 0 and not node.isEndWord

        return False

    def delete(self, word):
        self.delete_word(self.root, word, 0)  # ✅ Added wrapper for easier external call

    def update_word(self, word, target):
        if self.contains_word(word):
            self.delete(word)  # ✅ Call the fixed wrapper function
            self.insert_word(target)


def collect_unique(data, seen=None):
    if seen is None:
        seen = set()

    if isinstance(data, dict):
        for k, v in data.items():
            collect_unique(k, seen)
            collect_unique(v, seen)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            collect_unique(item, seen)
    else:
        try:
            seen.add(data)
        except TypeError:
            # Skip unhashable types like dicts or custom objects
            pass

    return seen	


import json

def flatten_json(obj, parent_key='', sep='_'):
    items = {}
    for k, v in obj.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep=sep))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, (dict, list)):
                    items.update(flatten_json(item, f"{new_key}_{i}", sep=sep))
                else:
                    items[f"{new_key}_{i}"] = item
        else:
            items[new_key] = v
    return items


flat_output = flatten_json(input_data)
for k, v in flat_output.items():
    print(f'"{k}": {json.dumps(v)},')            