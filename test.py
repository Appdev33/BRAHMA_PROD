# # import certifi
# # import aiohttp
# # import asyncio
# # import ssl
# # from memory_profiler import profile


# # ssl_context = ssl.create_default_context(cafile=certifi.where())
# # @profile
# # async def fetch(url):
# #     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
# #         async with session.get(url) as response:
# #             return await response.text()

# # urls = [
# #     "https://jsonplaceholder.typicode.com/posts/1",
# #     "https://jsonplaceholder.typicode.com/posts/2",
# #     "https://jsonplaceholder.typicode.com/posts/1",
# #     "https://jsonplaceholder.typicode.com/posts/2",
# #     "https://jsonplaceholder.typicode.com/posts/1",
# #     "https://jsonplaceholder.typicode.com/posts/2",
# #     "https://jsonplaceholder.typicode.com/posts/1",
# #     "https://jsonplaceholder.typicode.com/posts/2"
# # ]

# # async def main():
# #     tasks = [fetch(url) for url in urls]
# #     results = await asyncio.gather(*tasks)
# #     print(results[:3], end = '\n')


# # asyncio.run(main())
# # # print(*range(11,1,-1))

# import certifi
# import aiohttp
# import asyncio
# import ssl

# ssl_context = ssl.create_default_context(cafile=certifi.where())

# async def fetch(url):
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
#         async with session.get(url) as response:
#             return await response.text()

# urls = [
#     "https://jsonplaceholder.typicode.com/posts/1",
#     "https://jsonplaceholder.typicode.com/posts/2",
#     "https://jsonplaceholder.typicode.com/posts/1",
#     "https://jsonplaceholder.typicode.com/posts/2",
#     "https://jsonplaceholder.typicode.com/posts/1",
#     "https://jsonplaceholder.typicode.com/posts/2",
#     "https://jsonplaceholder.typicode.com/posts/1",
#     "https://jsonplaceholder.typicode.com/posts/2"
# ]

# async def main():
#     tasks = [fetch(url) for url in urls]
#     results = await asyncio.gather(*tasks)
#     print(results[:2])

# # ---- cProfile hook ----

# def run_with_profile():
#     import cProfile
#     import pstats
#     import io

#     profiler = cProfile.Profile()
#     profiler.enable()
    
#     asyncio.run(main())
    
#     profiler.disable()
#     s = io.StringIO()
#     sortby = pstats.SortKey.CUMULATIVE
#     ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
#     ps.print_stats(20)  # Top 20 slowest functions
#     print(s.getvalue())

# if __name__ == "__main__":
#     run_with_profile()

from collections import deque

dq = deque()
el = [1,2,3,4,5,6]

dq.extend(el)
print(dq , end="\n")

dq.rotate(2)
print(dq , end="\n")

dq.rotate(-2)
print(dq , end="\n")

map = { x: x**2 for x in range(5)}
print(map)

print(map.items(), end="\n")

print(type(map))



# def isAlienSorted(self, words: List[str], order: str) -> bool:
#     return words = sorted(words, key = lambda word : [ order.index(c) for char c in word ] )


str = "hello"
st1 = "21"
print(str.ljust(8,'#'))
print(str.rjust(8,'#'))
print(str.center(8,'#'))
print( str.zfill(8) )