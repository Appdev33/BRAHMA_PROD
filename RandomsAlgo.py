# KMP
# https://www.youtube.com/watch?v=qases-9gOpk

def compute_lps(pattern):
    n = len(pattern)
    lps = [0] * n
    length = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    if not pattern:
        return []
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = j = 0
    results = []
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                results.append(i - j)
                j = lps[j - 1]
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
    return results          

# Example
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

print(kmp_search(text, pattern))  # Output: [10]
# RABIN KARP



# MANACHER ALGO



# Z ALGORITHM




# QUICK SELECT ALGO
from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert kth largest to kth smallest index
        k = len(nums) - k

        def partition(l, r):
            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[r] = nums[r], nums[i]
            return i

        def quickselect(l, r):
            if l == r:
                return nums[l]

            # (Optional) randomized pivot for expected O(n)
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            p = partition(l, r)

            if p == k:
                return nums[p]
            elif p > k:
                return quickselect(l, p - 1)
            else:
                return quickselect(p + 1, r)

        return quickselect(0, len(nums) - 1)


# CONVEX HULL OPTIMIZATION (Fence Boundary / Erect the Fence)
# Problem intuition:
# Given points as tree locations, we need the minimum-length fence that encloses
# all trees. Return all trees that lie on the fence boundary (including collinear).
#
# Intuitive steps:
# 1) Sort points by x, then y. This gives a left-to-right sweep order.
# 2) Build lower hull:
#    - Keep adding points.
#    - If the last turn is clockwise, remove the middle point (it is inside).
# 3) Build upper hull similarly but sweeping from right-to-left.
# 4) Merge both hulls and remove duplicates.
# 5) For fence-boundary version, keep collinear boundary points by removing points
#    only on strict clockwise turns (cross < 0), not on cross == 0.

class ConvexHullSolution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 1:
            return trees

        points = sorted(set(map(tuple, trees)))
        if len(points) <= 2:
            return [list(p) for p in points]

        def cross(o, a, b):
            # Cross product of OA x OB
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Remove duplicate endpoints and combine.
        hull = set(lower[:-1] + upper[:-1])
        return [list(p) for p in hull]


# Example (fence boundary):
# Input points form a rectangle with a middle point.
# Boundary points should include all corner points.
fence_points = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
print(ConvexHullSolution().outerTrees(fence_points))


# Deque variation of convex hull (same fence-boundary behavior).
from collections import deque


class ConvexHullDequeSolution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 1:
            return trees

        points = sorted(set(map(tuple, trees)))
        if len(points) <= 2:
            return [list(p) for p in points]

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        lower = deque()
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        upper = deque()
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        hull = set(list(lower)[:-1] + list(upper)[:-1])
        return [list(p) for p in hull]


print(ConvexHullDequeSolution().outerTrees(fence_points))


# LIS (Longest Increasing Subsequence)
# ------------------------------------------------------------
# Goal: return the length of the longest strictly increasing subsequence.
# Example: [10, 9, 2, 5, 3, 7, 101, 18] -> 4 (one LIS is [2, 3, 7, 18])


def lis_n2(nums: List[int]) -> int:
    # O(n^2) DP intuition:
    # dp[i] = length of LIS that MUST end at index i.
    # For each i, look at all previous j < i.
    # If nums[j] < nums[i], then nums[i] can extend subsequence ending at j.
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # Each element alone is an LIS of length 1.

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Best LIS can end anywhere, so return max over dp.
    return max(dp)


from bisect import bisect_left


def lis_nlogn(nums: List[int]) -> int:
    # O(n log n) intuition with tails:
    # tails[k] = smallest possible tail value of an increasing subsequence
    #            of length (k + 1) seen so far.
    #
    # Why this works:
    # - Smaller tails are better because they are easier to extend later.
    # - For each x, find first tail >= x and replace it with x.
    # - If x is larger than all tails, append it (we found longer subsequence).
    if not nums:
        return 0

    tails = []
    for x in nums:
        idx = bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x

    # Length of tails equals LIS length.
    return len(tails)


# LIS examples
lis_input = [10, 9, 2, 5, 3, 7, 101, 18]
print(lis_n2(lis_input))     # 4
print(lis_nlogn(lis_input))  # 4