#SEGMENT TREES

# Segment Tree for Range Sum Queries (0-indexed, no None defaults)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg_tree = [0] * (4 * self.n)
        self.build(arr, 0, self.n - 1, 0)
        self.lazy = [0] * (4 * self.n)

    # Build the tree recursively
    def build(self, arr, left, right, node_index):
        if left == right:
            self.seg_tree[node_index] = arr[left]
            return
        mid = (left + right) // 2
        self.build(arr, left, mid, 2 * node_index + 1)
        self.build(arr, mid + 1, right, 2 * node_index + 2)
        self.seg_tree[node_index] = self.seg_tree[2 * node_index + 1] + self.seg_tree[2 * node_index + 2]

    def lazy_propogate(self, node_index, left, right):
        if self.lazy[node_index] != 0:
            self.seg_tree[node_index] += (right - left + 1) * self.lazy[node_index]

            if left != right:
                self.lazy[2 * node_index + 1] += self.lazy[node_index]
                self.lazy[2 * node_index + 2] += self.lazy[node_index]

            self.lazy[node_index] = 0


    def lazy_update(self, update_left, update_right, value, left, right, node_index):
        self.lazy_propogate(node_index, left, right)

        # No overlap
        if update_right < left or update_left > right:
            return

        # Complete overlap
        if update_left <= left and right <= update_right:
            self.lazy[node_index] += value
            self.lazy_propogate(node_index, left, right)
            return

        mid = (left + right) // 2

        self.lazy_update(update_left, update_right, value, left, mid, 2 * node_index + 1)
        self.lazy_update(update_left, update_right, value, mid + 1, right, 2 * node_index + 2)

        self.seg_tree[node_index] = (
            self.seg_tree[2 * node_index + 1] +
            self.seg_tree[2 * node_index + 2]
        )



    def lazy_update(self, update_left, update_right, value, left, right, node_index):
        
        # 🔥 Inline propagation
        if self.lazy[node_index] != 0:
            self.seg_tree[node_index] += (right - left + 1) * self.lazy[node_index]
            
            if left != right:
                self.lazy[2 * node_index + 1] += self.lazy[node_index]
                self.lazy[2 * node_index + 2] += self.lazy[node_index]
            
            self.lazy[node_index] = 0

        # ❌ No overlap
        if update_right < left or update_left > right:
            return

        # ✅ Complete overlap
        if update_left <= left and right <= update_right:
            self.seg_tree[node_index] += (right - left + 1) * value
            
            if left != right:
                self.lazy[2 * node_index + 1] += value
                self.lazy[2 * node_index + 2] += value
            
            return

        # 🔁 Partial overlap
        mid = (left + right) // 2

        self.lazy_update(update_left, update_right, value, left, mid, 2 * node_index + 1)
        self.lazy_update(update_left, update_right, value, mid + 1, right, 2 * node_index + 2)

        self.seg_tree[node_index] = (
            self.seg_tree[2 * node_index + 1] +
            self.seg_tree[2 * node_index + 2]
        )

    # Internal update function
    def _update(self, index, value, left, right, node_index):
        if left == right:
            self.seg_tree[node_index] = value
            return
        mid = (left + right) // 2
        if index <= mid:
            self._update(index, value, left, mid, 2 * node_index + 1)
        else:
            self._update(index, value, mid + 1, right, 2 * node_index + 2)
        self.seg_tree[node_index] = self.seg_tree[2 * node_index + 1] + self.seg_tree[2 * node_index + 2]

    # Public update function
    def update(self, index, value):
        self._update(index, value, 0, self.n - 1, 0)

    # Internal query function
    def _query(self, query_left, query_right, left, right, node_index):
        if query_right < left or query_left > right:  # No overlap
            return 0
        if query_left <= left and right <= query_right:  # Complete overlap
            return self.seg_tree[node_index]
        mid = (left + right) // 2
        left_sum = self._query(query_left, query_right, left, mid, 2 * node_index + 1)
        right_sum = self._query(query_left, query_right, mid + 1, right, 2 * node_index + 2)
        return left_sum + right_sum

    # Public query function
    def query(self, query_left, query_right):
        return self._query(query_left, query_right, 0, self.n - 1, 0)


# Example usage
arr = [1, 3, 5, 7, 9, 11]
seg = SegmentTree(arr)
print("Sum [1,3]:", seg.query(1, 3))  # 3+5+7=15
seg.update(1, 10)
print("After update sum [1,3]:", seg.query(1, 3))  # 10+5+7=22


# FENWICK TREES    
# https://www.youtube.com/watch?v=pTg7NezkV28&list=PL-Jc9J83PIiGkI_pL8l67OVvbpnwf-5yO&index=7

class FenwickTree:

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n + 1)

        # Build Fenwick Tree using point updates
        for i in range(self.n):
            self.update(i + 1, arr[i])

    def update(self, index, delta):
        """
        Adds delta to index (1-based)
        """
        while index <= self.n:
            self.tree[index] += delta
            index += (index & -index)   # move to next responsible node

    def prefix_sum(self, index):
        """
        Sum from 1 to index
        """
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= (index & -index)   # 🔥 FIX: move backward
        return result

    def range_sum(self, left, right):
        """
        Sum from left to right
        """
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

arr = [3, 2, -1, 6, 5, 4, -3, 3]

ft = FenwickTree(arr)

print(ft.prefix_sum(5))      # 15
print(ft.range_sum(3, 7))    # 11

ft.update(4, 5)              # index 4 += 5

print(ft.prefix_sum(5))      # 20


# QUAD TREES
class QuadNode:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class QuadTree:

    def is_same(self, grid, x, y, n):
        """
        Check if all values in the n x n subgrid starting at (x, y) are the same
        """
        first = grid[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if grid[i][j] != first:
                    return False
        return True

    def solve(self, grid, x, y, n):
        """
        Recursively build QuadTree
        """
        # Base case: all values are same
        if self.is_same(grid, x, y, n):
            return QuadNode(grid[x][y], True)

        # Otherwise, split into 4 quadrants
        half = n // 2
        return QuadNode(
            val=1,              # value doesn't matter for non-leaf
            isLeaf=False,
            topLeft=self.solve(grid, x, y, half),
            topRight=self.solve(grid, x, y + half, half),
            bottomLeft=self.solve(grid, x + half, y, half),
            bottomRight=self.solve(grid, x + half, y + half, half)
        )

# OPTIMSED CODE FOR ISSAME
class QuadTree:

    def build_prefix(self, grid):
        n = len(grid)
        ps = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                ps[i + 1][j + 1] = (
                    grid[i][j]
                    + ps[i][j + 1]
                    + ps[i + 1][j]
                    - ps[i][j]
                )
        return ps

    def is_same(self, ps, x, y, n):
        """
        O(1) uniformity check using prefix sum
        """
        total = (
            ps[x + n][y + n]
            - ps[x][y + n]
            - ps[x + n][y]
            + ps[x][y]
        )
        return total == 0 or total == n * n

    def solve(self, grid, ps, x, y, n):
        if self.is_same(ps, x, y, n):
            return QuadNode(grid[x][y], True)

        half = n // 2
        return QuadNode(
            val=1,
            isLeaf=False,
            topLeft=self.solve(grid, ps, x, y, half),
            topRight=self.solve(grid, ps, x, y + half, half),
            bottomLeft=self.solve(grid, ps, x + half, y, half),
            bottomRight=self.solve(grid, ps, x + half, y + half, half)
        )

    # LeetCode-style wrapper
    def construct(self, grid):
        ps = self.build_prefix(grid)
        return self.solve(grid, ps, 0, 0, len(grid))


#COUNT OF BST CATALAN NUMBER
def numTrees(n):
    # dp[i] = number of unique BSTs possible using i nodes
    dp = [0] * (n + 1)

    # Base Case:
    # Empty tree is also considered 1 valid BST
    dp[0] = 1

    # Build answers from smaller node counts -> larger
    for nodes in range(1, n + 1):

        # Try every possible left subtree size
        # If total nodes = 5:
        #
        # root takes 1 node
        # remaining = 4 nodes
        #
        # left can take:
        # 0,1,2,3,4 nodes
        #
        # right automatically gets:
        # 4,3,2,1,0 nodes

        for left in range(nodes):

            # Remaining nodes go to right subtree
            right = nodes - 1 - left

            # Number of BSTs formed:
            #
            # (ways to build left subtree)
            # *
            # (ways to build right subtree)
            #
            # because every left BST can combine
            # with every right BST
            dp[nodes] += dp[left] * dp[right]

    return dp[n]



#BINARY LIFTING

import math

class TreeAncestor:

    def _init_(self, n: int, parent: List[int]):
        self.bit = int(math.log2(n)) + 1
        self.ancestor = [[-1] * self.bit for _ in range(n)]

        for i in range(n):
            self.ancestor[i][0] = parent[i]

        for j in range(1, self.bit):
            for node in range(n):
                mid = self.ancestor[node][j - 1]
                if mid != -1:
                    self.ancestor[node][j] = self.ancestor[mid][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:

        for i in range(self.bit):
            if k & (1 << i):
                node = self.ancestor[node][i]
                if node == -1:
                    return -1
        return node
    

from collections import defaultdict
import math

class LCA:

    def __init__(self, n, edges, root=0):
        self.bit = math.ceil(math.log2(n)) + 1
        self.graph = defaultdict(list)

        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.depth = [0] * n
        self.ancestor = [[-1] * self.bit for _ in range(n)]
        self.dfs(root, -1)

    def dfs(self, node, parent):
        self.ancestor[node][0] = parent

        for j in range(1, self.bit):
            prev = self.ancestor[node][j - 1]
            if prev != -1:
                self.ancestor[node][j] = self.ancestor[prev][j - 1]

        for nei in self.graph[node]:
            if nei == parent:
                continue
            self.depth[nei] = self.depth[node] + 1
            self.dfs(nei, node)

    def kth_ancestor(self, node, k):
        for j in range(self.bit):
            if k & (1 << j):
                node = self.ancestor[node][j]
                if node == -1:
                    return -1
        return node

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]
        u = self.kth_ancestor(u, diff)

        if u == v:
            return u

        for j in range(self.bit - 1, -1, -1):
            if self.ancestor[u][j] != self.ancestor[v][j]:
                u = self.ancestor[u][j]
                v = self.ancestor[v][j]
        return self.ancestor[u][0]    


#SPARSE TABLE MIN MAX SEARCH
class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        self.log = [0] * (n + 1)

        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

        max_power = self.log[n] + 1

        # dp[i][j] = min in range [i, i + 2^j - 1]
        self.dp = [[0] * max_power for _ in range(n)]

        for i in range(n):
            self.dp[i][0] = arr[i]

        for power in range(1, max_power):
            half = 1 << (power - 1)

            for start in range(n - (1 << power) + 1):
                self.dp[start][power] = min(
                    self.dp[start][power - 1],
                    self.dp[start + half][power - 1]
                )

    def query(self, left, right):
        length = right - left + 1
        power = self.log[length]

        return min(
            self.dp[left][power],
            self.dp[right - (1 << power) + 1][power]
        )
#OPTIMAL BINARY SEARCH TREE
# https://www.youtube.com/watch?v=HnslzEs8dbY

def optimal_bst(keys, frequency):
    n = len(keys)
    
    # dp[i][j] = optimal cost for keys i..j
    dp = [[0] * n for _ in range(n)]
    
    # GAP strategy
    for g in range(n):                     # gap
        i = 0
        j = g
        while j < n:
            
            # Case 1: single key
            if g == 0:
                dp[i][j] = frequency[i]
            
            # Case 2: two keys
            elif g == 1:
                f1 = frequency[i]
                f2 = frequency[j]
                dp[i][j] = min(
                    f1 + 2 * f2,
                    f2 + 2 * f1
                )
            
            # Case 3: more than two keys
            else:
                min_cost = float('inf')
                
                # sum of frequencies from i to j
                fs = 0
                for x in range(i, j + 1):
                    fs += frequency[x]
                
                # try each key as root
                for k in range(i, j + 1):
                    left = 0 if k == i else dp[i][k - 1]
                    right = 0 if k == j else dp[k + 1][j]
                    
                    cost = left + right + fs
                    min_cost = min(min_cost, cost)
                
                dp[i][j] = min_cost
            
            i += 1
            j += 1
    
    return dp[0][n - 1]

def optimal_bst(keys, frequency):
    n = len(keys)
    
    # dp[i][j] = optimal cost from i..j
    dp = [[0] * n for _ in range(n)]
    
    # prefix sum of frequencies
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + frequency[i]
    
    # helper for sum frequency[i..j]
    def freq_sum(i, j):
        return prefix[j + 1] - prefix[i]
    
    # GAP based DP
    for g in range(n):
        i = 0
        j = g
        while j < n:
            
            if g == 0:
                dp[i][j] = frequency[i]
            
            elif g == 1:
                f1 = frequency[i]
                f2 = frequency[j]
                dp[i][j] = min(f1 + 2 * f2, f2 + 2 * f1)
            
            else:
                min_cost = float('inf')
                fs = freq_sum(i, j)
                
                for k in range(i, j + 1):
                    left = 0 if k == i else dp[i][k - 1]
                    right = 0 if k == j else dp[k + 1][j]
                    
                    min_cost = min(min_cost, left + right + fs)
                
                dp[i][j] = min_cost
            
            i += 1
            j += 1
    
    return dp[0][n - 1]


#HUFFMANN TREE
class Node:
    def __init__(self, val, char):
        self.val = val
        self.char = bit
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.val<other.val

import heapq
from collections import Counter
class Solution:
    def huffmanCodes(self,s,f):
        
        heap = [ Node(f[i],s[i])  for i in range(len(s)) ]
        heapq.heapify(heap)
        
        while len(heap)>1:
            left = heapq.heapify(heap)
            right = heapq.heapify(heap)
            
            top = Node(left.val+right.val)
            top.left = left
            top.right = right
            heapq.heapush(top)
            
        root = heap[0]
        res = []
        
        def traverse(node, current_node):
            if not node:
                return None
            
            if node.char:
                res.append(current_node)
                return
            
            traverse(node.left, '0')
            traverse(node.right, '1')
            
        traverse(root, "")
        
        return res
        

#https://www.geeksforgeeks.org/problems/huffman-encoding3345/1
import heapq

class Node:
    def __init__(self, val=None, sum_=0, idx=-1):
        self.val = val
        self.sum = sum_
        self.idx = idx
        self.left = None
        self.right = None

    # needed for heap comparison
    def __lt__(self, other):
        if self.sum != other.sum:
            return self.sum < other.sum
        return self.idx < other.idx

def preorder(root, path, mp):
    if not root:
        return
    
    if root.val is not None:
        mp[root.val] = path if path != "" else "0"
    
    preorder(root.left, path + '0', mp)
    preorder(root.right, path + '1', mp)


class Solution:
    def huffmanCodes(self, s, f):
        # code here
        pq = []
        
        for i in range(len(s)):
            heapq.heappush(pq, Node(s[i], f[i], i))
        
        while len(pq) > 1:
            t1 = heapq.heappop(pq)
            t2 = heapq.heappop(pq)
            
            temp = Node(None, t1.sum + t2.sum, min(t1.idx, t2.idx))
            temp.left = t1
            temp.right = t2
            
            heapq.heappush(pq, temp)
        
        mp = {}
        preorder(pq[0], "", mp)
        
        return sorted([mp[ch] for ch in s])

        