from collections import defaultdict
import heapq


# def dijkstra(n, graph, src ):
#     distance = [float('inf')] * n
#     # distance[u] represents the shortest known distance from the src node to node u, not the edge weight to u.
#     distance[src] = 0  # distance from src to itself is 0
    
#     minhheap = [(0,src)]


#     while minhheap:
#         wt, u = heapq.heappop(minhheap)  # distance from src to itself is u is wt

#         if wt>distance[u]:
#             continue
#         # This checks if the value we just popped (wt) is outdated.
#         # Why outdated? Because a shorter path to u may have already been found and stored in distance[u].
#         # If so, we skip processing this outdated version of u

#         for v,w in graph[u]:
#             if distance[v] > w+distance[u]:
#                distance[v] = w+distance[u] 
#                heapq.heappush(minhheap,(distance[v],v))

#         # This checks if the new path to v through u is shorter than the previously known one.
#         # distance[v]: current best known distance from src to v
#         # w + distance[u]: going from src → … → u → v
#         # (i.e., path to u + edge from u to v)       

#     return distance           



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


import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        # Build adjacency list
        for src, dest, wt in times:
            graph[src].append((dest, wt))

        # Min-heap (distance, node)
        min_heap = [(0, k)]
        dist = {}

        while min_heap:
            curr_wt, curr_src = heapq.heappop(min_heap)

            if curr_src in dist:  # If node already visited, skip it
                continue

            dist[curr_src] = curr_wt

            for neig_dest, neig_wt in graph[curr_src]:  # Use curr_src instead of src
                if neig_dest not in dist:
                    heapq.heappush(min_heap, (curr_wt + neig_wt, neig_dest))

        return max(dist.values()) if len(dist) == n else -1





from collections import defaultdict

edges = [('a','b'), ('b','c'), ('c','a')]  # Cycle exists

graph = defaultdict(list)
for src, dest in edges:
    graph[src].append(dest)

# def dfs(node, visited, rec_stack):
#     visited.add(node)
#     rec_stack.add(node)

#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             if dfs(neighbor, visited, rec_stack):
#                 return True
#         elif neighbor in rec_stack:
#             return True  

#     rec_stack.remove(node)
#     return False

# visited = set()

# for node in graph:
#     if node not in visited:
#         if dfs(node, visited, set()):
#             print("Loop Detected")
#             break
# else:
#     print("No Loops")



# from collections import defaultdict

# edges = [('a','b'), ('b','c'), ('c','a')]  # Cycle exists

# graph = defaultdict(list)
# for src, dest in edges:
#     graph[src].append(dest)
#     graph[dest].append(src)

# def dfs(node, visited, parent):
    
#     visited.add(node)

#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             if dfs(neighbor, visited, node):
#                 return True
#         elif neighbor != parent:
#             return True  

#     return False

# visited = set()

# for node in graph:
#     if node not in visited:
#         if dfs(node, visited, -1):
#             print("Loop Detected")
#             break
# else:
#     print("No Loops")



# def has_cycle_directed(v, graph, visited, rec_stack):
#     visited[v] = True
#     rec_stack[v] = True

#     for neighbor in graph[v]:
#         if not visited[neighbor]:
#             if has_cycle_directed(neighbor, graph, visited, rec_stack):
#                 return True
#         elif rec_stack[neighbor]:  # cycle found via back edge
#             return True

#     rec_stack[v] = False  # remove from recursion stack
#     return False


# def detect_cycle_directed(graph, num_vertices):
    visited = [False] * num_vertices
    rec_stack = [False] * num_vertices

    for v in range(num_vertices):
        if not visited[v]:
            if has_cycle_directed(v, graph, visited, rec_stack):
                return True
    return False



# def has_cycle_undirected(v, graph, visited, parent):
#     visited[v] = True

#     for neighbor in graph[v]:
#         if not visited[neighbor]:
#             if has_cycle_undirected(neighbor, graph, visited, v):
#                 return True
#         elif neighbor != parent:
#             return True

#     return False

# def detect_cycle_undirected(graph, num_vertices):
    visited = [False] * num_vertices

    for v in range(num_vertices):
        if not visited[v]:
            if has_cycle_undirected(v, graph, visited, -1):
                return True
    return False


# TOPOLOGICAL DIRECT GRAPHS

# from collections import defaultdict, deque

# edges = [('a', 'b'), ('b', 'c'), ('c', 'a')]  # Cycle exists

# graph = defaultdict(list)
# indegree = defaultdict(int)
# nodes = set()

# for src, dest in edges:
#     graph[src].append(dest)
#     indegree[dest] += 1
#     nodes.add(src)
#     nodes.add(dest)

# # Ensure all nodes are in indegree dict
# for node in nodes:
#     indegree[node] = indegree.get(node, 0)

# queue = deque()
# for node in indegree:
#     if indegree[node] == 0:
#         queue.append(node)

# visited_count = 0

# while queue:
#     curr = queue.popleft()
#     visited_count += 1

#     for neigh in graph[curr]:
#         indegree[neigh] -= 1
#         if indegree[neigh] == 0:
#             queue.append(neigh)

# # Final check
# if visited_count == len(indegree):
#     print("No Cycle")
# else:
#     print("Cycle Detected")


class SparseVector:
    def __init__(self, nums):
        # Store only non-zero values with their indices
        self.index_to_val = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.index_to_val[i] = nums[i]
    
    def dot_product(self, vec):
        result = 0

        # Loop over the current vector's non-zero elements
        for i in self.index_to_val:
            if i in vec.index_to_val:
                result += self.index_to_val[i] * vec.index_to_val[i]
        
        return result
    
class SparseVector:
    def __init__(self, nums):
        self.index_to_val = {ind: num for ind, num in enumerate(nums) if num != 0}
        
    def dot_product(self, vec: 'SparseVector') -> int:
        result = 0
        
        # Iterate over the smaller dict to improve performance
        if len(self.index_to_val) > len(vec.index_to_val):
            return vec.dot_product(self)
        
        for i in self.index_to_val:
            if i in vec.index_to_val:
                result += self.index_to_val[i] * vec.index_to_val[i]
        
        return result
      

v1 = SparseVector([0, 3, 0, 4])
v2 = SparseVector([0, 2, 0, 1])
