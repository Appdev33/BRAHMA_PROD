# # d1 = {'a':1}
# # d2 = {'b':2}
# # d4 = {'x':3, 'y':5}
# # d3 = {**d1, **d2, **d4}  # Merge dicts

# # print(d3)


# a = [[1,2,3],
#      [4,5,6,],
#      [7,8,9]]


# row, col = len(a), len(a[0])

# print(row)
# print(col)
                       

res = []
for row in zip(*a):
    res.append(list(row))
    print(row)

print(res)

def squares_return(n):
   result = []
   for i in range(n):
       result.append(i * i)
   return result


# Using yield
def squares_yield(n):
   for i in range(n):
       yield i * i


import sys

print(sys.getsizeof(squares_return(1000000)))
print(sys.getsizeof(squares_yield(1000000)))

