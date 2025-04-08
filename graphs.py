from collections import defaultdict
import heapq


def dijkstra(n, graph, src ):
    distance = [float('inf')] * n
    distance[src] = 0
    minhheap = [(0,src)]

    while minhheap:
        wt, u = heapq.heappop(minhheap)

        if wt>distance[u]:
            continue

        for v,w in graph[u]:
            if distance[v] > w+distance[u]:
               distance[v] = w+distance[u] 
               heapq.heappush(minhheap,(distance[v],v))

    return distance           



src = 0
n = 6
graph = defaultdict(list)

# Add edges (u, v, weight)
graph[0].append((1, 4))
graph[0].append((2, 2))
graph[1].append((2, 5))
graph[1].append((3, 10))
graph[2].append((4, 3))
graph[4].append((3, 4))
graph[3].append((5, 11))

distances = dijkstra(n, graph, src)

print(f"Shortest distances from node {src}: {distances}")


# import heapq
# from collections import defaultdict
# from typing import List

# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         graph = defaultdict(list)
        
#         # Build adjacency list
#         for src, dest, wt in times:
#             graph[src].append((dest, wt))

#         # Min-heap (distance, node)
#         min_heap = [(0, k)]
#         dist = {}

#         while min_heap:
#             curr_wt, curr_src = heapq.heappop(min_heap)

#             if curr_src in dist:  # If node already visited, skip it
#                 continue

#             dist[curr_src] = curr_wt

#             for neig_dest, neig_wt in graph[curr_src]:  # Use curr_src instead of src
#                 if neig_dest not in dist:
#                     heapq.heappush(min_heap, (curr_wt + neig_wt, neig_dest))

#         return max(dist.values()) if len(dist) == n else -1


