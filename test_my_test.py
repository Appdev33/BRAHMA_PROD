import gc
import tracemalloc
from itertools import permutations

# print(gc.get_count())

# print(gc.get_stats())

print(gc.get_threshold())   


tracemalloc.start()

list_ = [1, 2,2, 3, 4]
result = list(permutations(list_, 2))
print(result)