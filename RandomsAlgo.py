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

# Intuition:
# Convert each fixed-size window into a number (hash).
# If window-hash == pattern-hash, then verify characters to avoid false positives.
# Rolling hash lets us update hash in O(1) when window slides.
def rabin_karp_search(text, pattern):
    if not pattern or len(pattern) > len(text):
        return []

    base = 256
    mod = 10**9 + 7
    n, m = len(text), len(pattern)

    high_base = pow(base, m - 1, mod)
    p_hash = 0
    w_hash = 0

    for i in range(m):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        w_hash = (w_hash * base + ord(text[i])) % mod

    result = []
    for i in range(n - m + 1):
        if p_hash == w_hash and text[i:i + m] == pattern:
            result.append(i)

        if i < n - m:
            # Remove left char, shift, add next char.
            w_hash = (w_hash - ord(text[i]) * high_base) % mod
            w_hash = (w_hash * base + ord(text[i + m])) % mod

    return result


# MANACHER ALGO

# Intuition:
# 1) Insert separators to treat even/odd palindromes uniformly.
# 2) p[i] = palindrome radius around i in transformed string.
# 3) Use mirror info around current center to skip re-checking.
def longest_palindrome_manacher(s):
    if not s:
        return ""

    t = "^#" + "#".join(s) + "#$"
    p = [0] * len(t)
    center = right = 0

    for i in range(1, len(t) - 1):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])

        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        if i + p[i] > right:
            center, right = i, i + p[i]

    max_len = max(p)
    center_idx = p.index(max_len)
    start = (center_idx - max_len) // 2
    return s[start:start + max_len]


# Z ALGORITHM

# Intuition:
# z[i] = length of longest prefix of string that matches starting at i.
# For pattern search, build pattern + "$" + text.
# Whenever z[i] == len(pattern), we found a match.
def z_array(s):
    n = len(s)
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z


def z_search(text, pattern):
    if not pattern:
        return []

    combined = pattern + "$" + text
    z = z_array(combined)
    m = len(pattern)
    ans = []

    for i in range(m + 1, len(combined)):
        if z[i] == m:
            ans.append(i - m - 1)

    return ans


# Other useful string matching algorithms

# 1) Naive search (baseline, easiest to reason about)
def naive_search(text, pattern):
    if not pattern:
        return []
    n, m = len(text), len(pattern)
    out = []
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            out.append(i)
    return out


# 2) Boyer-Moore (bad character heuristic only)
# Intuition: compare from right to left and jump farther on mismatch.
def boyer_moore_bad_char_search(text, pattern):
    if not pattern:
        return []

    n, m = len(text), len(pattern)
    last = {}
    for i, ch in enumerate(pattern):
        last[ch] = i

    res = []
    shift = 0
    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            res.append(shift)
            shift += 1
        else:
            bad = text[shift + j]
            shift += max(1, j - last.get(bad, -1))

    return res


# String matching examples
txt = "AABAACAADAABAABA"
pat = "AABA"
print(rabin_karp_search(txt, pat))           # [0, 9, 12]
print(z_search(txt, pat))                    # [0, 9, 12]
print(naive_search(txt, pat))                # [0, 9, 12]
print(boyer_moore_bad_char_search(txt, pat)) # [0, 9, 12]

# Manacher example
print(longest_palindrome_manacher("babad"))  # "bab" or "aba"




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