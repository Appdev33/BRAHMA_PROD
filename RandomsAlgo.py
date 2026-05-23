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