#SEGMENT TREES

# Segment Tree for Range Sum Queries (0-indexed, no None defaults)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg_tree = [0] * (4 * self.n)
        self.build(arr, 0, self.n - 1, 0)

    # Build the tree recursively
    def build(self, arr, left, right, node_index):
        if left == right:
            self.seg_tree[node_index] = arr[left]
            return
        mid = (left + right) // 2
        self.build(arr, left, mid, 2 * node_index + 1)
        self.build(arr, mid + 1, right, 2 * node_index + 2)
        self.seg_tree[node_index] = self.seg_tree[2 * node_index + 1] + self.seg_tree[2 * node_index + 2]

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

# BST COUNT
def numTrees(n):
    dp = [0] * (n + 1)
    
    dp[0] = 1  # empty tree
    dp[1] = 1  # single node
    
    for i in range(2, n + 1):
        l = 0
        r = i - 1
        while l <= i - 1:
            dp[i] += dp[l] * dp[r]
            l += 1
            r -= 1
    
    return dp[n]
