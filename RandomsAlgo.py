# KMP (Knuth-Morris-Pratt)
#
# Intuition: when a mismatch happens, do not restart from the next text
# character. The LPS table says how much of the pattern's prefix still matches
# the text suffix already seen. That lets KMP keep scanning forward without
# rechecking text characters.
#
# Use it to find one exact pattern in a large text, such as searching logs,
# documents, or DNA strings. Its O(n + m) time is guaranteed, including for
# patterns with many repeated characters; extra space is O(m).
# https://www.youtube.com/watch?v=qases-9gOpk

def compute_lps(pattern):
    # lps[i] is the longest proper prefix of pattern[:i + 1] that is also its
    # suffix. On mismatch, it gives the next pattern position to try.
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

# Example: the pattern occurs once, starting at index 10.
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

print(kmp_search(text, pattern))  # Output: [10]
#
# RABIN-KARP

# Intuition: hash the pattern and the first text window of the same length.
# Slide that window across the text, updating its hash in O(1). Only compare
# characters when the hashes match, because different strings can share a hash.
#
# Use it when checking many same-length candidate substrings, for example in
# plagiarism or duplicate-sequence detection. This function searches for one
# pattern; multi-pattern variants reuse the same rolling-window idea. Its
# expected time is O(n + m), with O(n * m) worst case if many hashes collide.
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




# ORDERLY QUEUE: LEXICOGRAPHICALLY SMALLEST STRING
#
# If k > 1, the allowed operation can produce any permutation, so sorting is
# optimal. If k == 1, each operation moves the first character to the end;
# therefore the only reachable strings are rotations of the original string.
# Booth's algorithm finds the smallest rotation in O(n) time.
class OrderlyQueueSolution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))

        n = len(s)
        if n == 0:
            return s

        # left_window and right_window are candidate rotation start indexes.
        # offset counts matching characters compared between the candidates.
        left_window = 0
        right_window = 1
        offset = 0

        while left_window < n and right_window < n and offset < n:
            left_char = s[(left_window + offset) % n]
            right_char = s[(right_window + offset) % n]

            if left_char == right_char:
                offset += 1
                continue

            # Skip starts that lose at this same first differing character.
            if right_char < left_char:
                left_window = max(left_window + offset + 1, right_window + 1)
            else:
                right_window = max(right_window + offset + 1, left_window + 1)
            offset = 0

        winning_start = min(left_window, right_window)
        return s[winning_start:] + s[:winning_start]


# For k == 1, the smallest rotation of "cba" is "acb".
print(OrderlyQueueSolution().orderlyQueue("cba", 1))  # "acb"
# For k > 1, any permutation is reachable, so the result is sorted.
print(OrderlyQueueSolution().orderlyQueue("baaca", 3))  # "aaabc"


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


# LIS: LONGEST INCREASING SUBSEQUENCE
#
# A subsequence keeps the original order, but may skip elements.
# It must be strictly increasing: [2, 3, 7, 18] is valid, but [2, 2] is not.
# Example: [10, 9, 2, 5, 3, 7, 101, 18] -> answer is 4.


# LIS METHOD 1: DYNAMIC PROGRAMMING - O(n^2)
# Best for learning because dp[i] directly describes a real subsequence.
def lis_n2(nums: List[int]) -> int:
    # DP meaning:
    # dp[i] = the longest increasing subsequence that ends exactly at i.
    #
    # Example for nums = [2, 5, 3]:
    # - dp[0] = 1 because [2] is the best sequence ending at 2.
    # - dp[1] = 2 because [2, 5] is possible.
    # - dp[2] = 2 because [2, 3] is possible.
    #
    # To calculate dp[i], try every earlier position j. If nums[j] is smaller,
    # append nums[i] to the sequence that ended at j.
    # Time: O(n^2), space: O(n).
    if not nums:
        return 0

    n = len(nums)
    # Every single number is an increasing subsequence of length 1.
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                # Either keep the old answer or extend the sequence at j.
                dp[i] = max(dp[i], dp[j] + 1)

    # The best sequence does not have to end at the last index.
    return max(dp)


from bisect import bisect_left


# LIS METHOD 2: BINARY SEARCH / TAILS - O(n log n)
# Best for large inputs when only the LIS length is required.
def lis_nlogn(nums: List[int]) -> int:
    # Instead of storing every sequence, store only the best tail values.
    #
    # tails[length - 1] = the smallest possible final value of an increasing
    # subsequence of this length found so far.
    #
    # Smaller tails are better: a sequence ending in 5 is easier to extend
    # than a sequence of the same length ending in 10.
    #
    # For each number:
    # - If it is bigger than every tail, it creates a longer sequence.
    # - Otherwise replace the first tail >= number. The length stays the same,
    #   but the smaller tail gives future numbers more room to extend it.
    #
    # bisect_left finds that first tail in O(log n).
    # Time: O(n log n), space: O(n).
    if not nums:
        return 0

    tails = []
    for number in nums:
        position = bisect_left(tails, number)
        if position == len(tails):
            tails.append(number)
        else:
            tails[position] = number

    # tails does not necessarily contain the actual LIS.
    # Its length does equal the LIS length, which is all this function needs.
    return len(tails)


# LIS examples
lis_input = [10, 9, 2, 5, 3, 7, 101, 18]
print(lis_n2(lis_input))     # 4
print(lis_nlogn(lis_input))  # 4


# ============================================================================
# SQUARE-ROOT DECOMPOSITION
# ============================================================================
# Split the array into blocks of about sqrt(n) values.
# Store one sum per block, so a range query can skip complete blocks.
#
# Build: O(n) | update: O(1) | range sum: O(sqrt(n))
class SqrtDecomposition:
    def __init__(self, values: List[int]):
        self.values = values[:]
        self.block_size = max(1, int(len(values) ** 0.5))
        block_count = (len(values) + self.block_size - 1) // self.block_size
        self.block_sum = [0] * block_count

        for index, value in enumerate(self.values):
            self.block_sum[index // self.block_size] += value

    def update(self, index: int, value: int) -> None:
        """Replace values[index] with value."""
        block = index // self.block_size
        self.block_sum[block] += value - self.values[index]
        self.values[index] = value

    def range_sum(self, left: int, right: int) -> int:
        """Return the inclusive sum from left to right."""
        if not (0 <= left <= right < len(self.values)):
            raise IndexError("invalid inclusive range")

        answer = 0

        # Consume the unaligned values at the left edge.
        while left <= right and left % self.block_size != 0:
            answer += self.values[left]
            left += 1

        # Consume complete blocks in one operation.
        while left + self.block_size - 1 <= right:
            answer += self.block_sum[left // self.block_size]
            left += self.block_size

        # Consume the unaligned values at the right edge.
        while left <= right:
            answer += self.values[left]
            left += 1
        return answer


# ============================================================================
# MO'S ALGORITHM
# ============================================================================
# Use this for many OFFLINE range queries when the array does not change.
# Queries are reordered so the current window moves only a small distance.
# This version returns the number of distinct values in every range.
def mo_distinct_queries(values: List[int], queries: List[tuple[int, int]]) -> List[int]:
    if not values:
        return [0] * len(queries)

    block_size = max(1, int(len(values) ** 0.5))
    ordered_queries = sorted(
        enumerate(queries),
        key=lambda item: (
            item[1][0] // block_size,
            item[1][1] if (item[1][0] // block_size) % 2 == 0 else -item[1][1],
        ),
    )

    frequency = {}
    distinct = 0
    current_left, current_right = 0, -1
    answer = [0] * len(queries)

    def add(index: int) -> None:
        nonlocal distinct
        value = values[index]
        frequency[value] = frequency.get(value, 0) + 1
        if frequency[value] == 1:
            distinct += 1

    def remove(index: int) -> None:
        nonlocal distinct
        value = values[index]
        frequency[value] -= 1
        if frequency[value] == 0:
            distinct -= 1

    for query_index, (left, right) in ordered_queries:
        if not (0 <= left <= right < len(values)):
            raise IndexError("invalid inclusive range")

        while current_left > left:
            current_left -= 1
            add(current_left)
        while current_right < right:
            current_right += 1
            add(current_right)
        while current_left < left:
            remove(current_left)
            current_left += 1
        while current_right > right:
            remove(current_right)
            current_right -= 1
        answer[query_index] = distinct

    return answer


# ============================================================================
# MODULAR ARITHMETIC
# ============================================================================
# Modular exponentiation: calculate base^exponent % modulus in O(log exponent).
def modular_power(base: int, exponent: int, modulus: int) -> int:
    if modulus <= 0 or exponent < 0:
        raise ValueError("modulus must be positive and exponent non-negative")

    result = 1 % modulus
    base %= modulus

    while exponent:
        # If the current binary bit is 1, use this power of base.
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1

    return result


def gcd(a: int, b: int) -> int:
    """Euclid's algorithm: repeatedly keep the remainder."""
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    return 0 if a == 0 or b == 0 else abs(a // gcd(a, b) * b)


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return g, x, y where a*x + b*y = g = gcd(a, b)."""
    if b == 0:
        return abs(a), (1 if a >= 0 else -1), 0

    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


# Modular inverse means: (a * inverse) % modulus == 1.
# For a prime modulus, Fermat says inverse(a) = a^(modulus - 2).
def modular_inverse_prime(a: int, prime_modulus: int) -> int:
    if a % prime_modulus == 0:
        raise ValueError("inverse does not exist")
    return modular_power(a, prime_modulus - 2, prime_modulus)


# Extended GCD works with any modulus, but only if gcd(a, modulus) == 1.
def modular_inverse(a: int, modulus: int) -> int:
    g, x, _ = extended_gcd(a, modulus)
    if g != 1:
        raise ValueError("inverse exists only when gcd(a, modulus) == 1")
    return x % modulus


# ============================================================================
# SIEVE AND COMBINATIONS
# ============================================================================
def primes_up_to(limit: int) -> List[int]:
    """Return all primes <= limit in O(n log log n)."""
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    number = 2

    while number * number <= limit:
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False
        number += 1

    return [number for number, prime in enumerate(is_prime) if prime]


def combinations_mod_prime(n: int, r: int, prime_modulus: int) -> int:
    """Return nCr % prime_modulus for a prime modulus."""
    if r < 0 or r > n:
        return 0

    factorial = [1] * (n + 1)
    for value in range(1, n + 1):
        factorial[value] = factorial[value - 1] * value % prime_modulus

    denominator = factorial[r] * factorial[n - r] % prime_modulus
    inverse_denominator = modular_inverse_prime(denominator, prime_modulus)
    return factorial[n] * inverse_denominator % prime_modulus


# Small checks/examples:
# sqrt_data = SqrtDecomposition([1, 2, 3, 4, 5])
# print(sqrt_data.range_sum(1, 3))                    # 9
# sqrt_data.update(2, 10)
# print(sqrt_data.range_sum(1, 3))                    # 16
# print(mo_distinct_queries([1, 2, 1, 3], [(0, 2), (1, 3)]))  # [2, 3]
# print(modular_power(2, 10, 1_000_000_007))         # 1024
# print(modular_inverse_prime(3, 11))                # 4
# print(modular_inverse(3, 10))                      # 7
# print(primes_up_to(20))                            # [2, 3, 5, 7, 11, ...]