import gc
import tracemalloc
from itertools import permutations

# print(gc.get_count())

# print(gc.get_stats())

# print(gc.get_threshold())   


# tracemalloc.start()

# list_ = [1, 2,2, 3, 4]
# result = list(permutations(list_, 2))
# print(result)

str_n = "123"
palindrome = int(str_n + str_n[:-1])  # 12321

print(str_n[:-1][::-3], end = ' ')
print(palindrome)