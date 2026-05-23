
import heapq
from collections import defaultdict

# Number of nodes
n = 6

# Graph as adjacency list:
# graph[u] = list of (v, weight)
graph = defaultdict(list)

# Build graph
graph[0].append((1, 4))
graph[0].append((2, 2))
graph[1].append((2, 5))
graph[1].append((3, 10))
graph[2].append((4, 3))
graph[4].append((3, 4))
graph[3].append((5, 11))


def dijkstra(source):
    """
    Returns shortest distance from source to all nodes
    """

    # Step 1: Initialize all distances as infinity
    # Meaning: we don't know how to reach them yet
    dist = [float('inf')] * n

    # Distance to source is 0 (starting point)
    dist[source] = 0

    # Min-heap (priority queue)
    # Stores (current_distance, node)
    # Always expands the node with smallest distance first
    min_heap = [(0, source)]

    # Process nodes until heap is empty
    while min_heap:

        # Get node with smallest known distance
        current_distance, current_node = heapq.heappop(min_heap)

        # IMPORTANT OPTIMIZATION:
        # If this entry is outdated (we already found a shorter path),
        # skip it
        if current_distance > dist[current_node]:
            continue

        # Explore all neighbors of current node
        for neighbor, weight in graph[current_node]:

            # Try taking this path through current_node
            new_distance = current_distance + weight

            # If this path is shorter than previously known path
            if new_distance < dist[neighbor]:

                # Update shortest distance
                dist[neighbor] = new_distance

                # Push updated distance into heap
                # (we don't remove old one → lazy update)
                heapq.heappush(min_heap, (new_distance, neighbor))

    # Final shortest distances from source
    return dist


# Run algorithm
result = dijkstra(0)
print(result)


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



# CYCLES DIRECTED GRAPH

from collections import defaultdict

# -------------------------------
# BUILD DIRECTED GRAPH
# -------------------------------
def build_directed_graph():
    """
    Example graph:
    0 → 1 → 2 → 3 → 1 (cycle)
          ↓
          4 → 5
    """
    graph = defaultdict(list)

    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 1),  # 🔥 cycle here
        (1, 4),
        (4, 5)
    ]

    for src, dest in edges:
        graph[src].append(dest)  # directed → one direction only

    return graph, 6


# -------------------------------
# DIRECTED CYCLE DETECTION
# -------------------------------
def has_cycle_directed(graph, num_nodes):
    """
    Detect cycle in directed graph using DFS + recursion stack
    """

    visited = [False] * num_nodes      # node has been fully processed
    in_current_path = [False] * num_nodes  # node is in current DFS path

    def dfs(node):
        # Mark node as visited and part of current recursion path
        visited[node] = True
        in_current_path[node] = True

        # Explore neighbors
        for neighbor in graph[node]:

            # If neighbor not visited → go deeper
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True

            # If neighbor already in current path → BACK EDGE → cycle
            elif in_current_path[neighbor]:
                return True

        # Done exploring this node → remove from current path
        in_current_path[node] = False
        return False

    # Handle disconnected components
    for node in range(num_nodes):
        if not visited[node]:
            if dfs(node):
                return True

    return False


# -------------------------------
# RUN DIRECTED
# -------------------------------
graph, n = build_directed_graph()

if has_cycle_directed(graph, n):
    print("Cycle Detected (Directed)")
else:
    print("No Cycle (Directed)")

# CYCLES UNDIRECTED GRAPH

from collections import defaultdict

# -------------------------------
# BUILD UNDIRECTED GRAPH
# -------------------------------
def build_undirected_graph():
    """
    Example graph:
          0
         / \
        1—— 2
             \
              3 — 4
    """
    graph = defaultdict(list)
    edges = [
        (0, 1),
        (1, 2),
        (2, 0),  # 🔥 cycle here
        (2, 3),
        (3, 4)
    ]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # undirected → both directions

    return graph, 5

# -------------------------------
# UNDIRECTED CYCLE DETECTION
# -------------------------------
def has_cycle_undirected(graph, num_nodes):
    """
    Detect cycle in undirected graph using DFS + parent tracking
    """
    visited = [False] * num_nodes

    def dfs(node, parent):
        # Mark current node as visited
        visited[node] = True

        for neighbor in graph[node]:

            # If not visited → explore deeper
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True

            # If visited AND not parent → cycle detected
            elif neighbor != parent:
                return True

        return False

    # Handle disconnected components
    for node in range(num_nodes):
        if not visited[node]:
            if dfs(node, -1):   # -1 means no parent
                return True

    return False
# -------------------------------
# RUN UNDIRECTED
# -------------------------------
graph, n = build_undirected_graph()

if has_cycle_undirected(graph, n):
    print("Cycle Detected (Undirected)")
else:
    print("No Cycle (Undirected)")

from collections import defaultdict, deque
# -------------------------------
# BUILD DIRECTED GRAPH
# -------------------------------
def build_graph():
    """
    Example graph:
    a → b → c → a  (cycle)
    """
    edges = [
        ('a', 'b'),
        ('b', 'c'),
        ('c', 'a')   # 🔥 cycle
    ]

    graph = defaultdict(list)
    indegree = defaultdict(int)
    nodes = set()

    # Build graph + indegree
    for src, dest in edges:
        graph[src].append(dest)

        indegree[dest] += 1

        # IMPORTANT: track ALL nodes
        nodes.add(src)
        nodes.add(dest)

    # Ensure every node exists in indegree (even if 0)
    for node in nodes:
        indegree[node] = indegree.get(node, 0)

    return graph, indegree, nodes

# -------------------------------
# KAHN'S ALGORITHM (BFS)
# -------------------------------
def has_cycle_kahn(graph, indegree):
    """
    Detect cycle using topological sort (BFS)
    """

    # Step 1: Start with nodes having indegree 0
    queue = deque()
    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)

    processed_nodes = 0  # count how many nodes we process

    # Step 2: Process nodes
    while queue:
        current = queue.popleft()
        processed_nodes += 1

        # Reduce indegree of neighbors
        for neighbor in graph[current]:
            indegree[neighbor] -= 1

            # If indegree becomes 0 → ready to process
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Step 3: Check if all nodes were processed
    # If not → cycle exists
    return processed_nodes != len(indegree)

# -------------------------------
# RUN
# -------------------------------
graph, indegree, nodes = build_graph()

if has_cycle_kahn(graph, indegree):
    print("Cycle Detected (Kahn's Algo)")
else:
    print("No Cycle (Kahn's Algo)")


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
        # Store only non-zero values
        self.index_to_val = {i: num for i, num in enumerate(nums) if num != 0}

    def dot_product(self, vec: 'SparseVector') -> int:
        result = 0

        # Always iterate over the smaller dictionary (optimization)
        if len(self.index_to_val) > len(vec.index_to_val):
            return vec.dot_product(self)

        # Multiply only matching indices
        for i, val in self.index_to_val.items():
            result += val * vec.index_to_val.get(i, 0)

        return result
      
v1 = SparseVector([0, 3, 0, 4])
v2 = SparseVector([0, 2, 0, 1])

print(v1.dot_product(v2))
# https://chatgpt.com/c/69f859df-507c-8322-9230-b99ff36112b6

class SparseVector:
    def __init__(self, nums):
        self.index_to_val = {i: num for i, num in enumerate(nums) if num != 0}

    def __mul__(self, other: 'SparseVector') -> int:
        result = 0

        # Optimization: iterate over smaller dict
        if len(self.index_to_val) > len(other.index_to_val):
            return other * self   # reuse same logic

        for i, val in self.index_to_val.items():
            result += val * other.index_to_val.get(i, 0)

        return result

v1 = SparseVector([0, 3, 0, 4])
v2 = SparseVector([0, 2, 0, 1])
print(v1 * v2)

# KOSARAJU ALGO
# https://www.youtube.com/watch?v=QtdE7QPsWiU
from collections import defaultdict

def kosaraju(n, graph):
    visited = [False] * n
    stack = []

    # Step 1: DFS to fill stack
    def dfs(node):
        visited[node] = True
        for neigh in graph[node]:
            if not visited[neigh]:
                dfs(neigh)
        stack.append(node)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    # Step 2: Reverse graph
    rev_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            rev_graph[v].append(u)

    # Step 3: DFS on reversed graph
    visited = [False] * n
    sccs = []

    def dfs_rev(node, comp):
        visited[node] = True
        comp.append(node)
        for neigh in rev_graph[node]:
            if not visited[neigh]:
                dfs_rev(neigh, comp)

    while stack:
        node = stack.pop()
        if not visited[node]:
            comp = []
            dfs_rev(node, comp)
            sccs.append(comp)
    return sccs


# ARTICULATION POINTS
# https://www.youtube.com/watch?v=sAk4W8q0Rmw
from collections import defaultdict

class Solution:
    def articulationPoints(self, V, edges):

        # 🔹 Step 1: Build undirected graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 🔹 Arrays initialization
        parent = [-1] * V          # parent of each node in DFS tree
        disc = [-1] * V            # discovery time of node
        low = [-1] * V             # lowest reachable discovery time
        visited = [False] * V
        ap = [False] * V           # mark articulation points

        time = [0]  # global timer (list used for mutability)

        # 🔹 DFS function
        def dfs(u):
            visited[u] = True

            # set discovery and low time
            disc[u] = low[u] = time[0]
            time[0] += 1

            children = 0  # number of DFS children (for root case)

            for v in graph[u]:
                # 🔸 Ignore the edge to parent
                if v == parent[u]:
                    continue

                # 🔸 Case 1: Back edge (already visited node)
                if visited[v]:
                    # update low value using discovery time
                    low[u] = min(low[u], disc[v])
                else:
                    # 🔸 Case 2: Tree edge
                    parent[v] = u
                    children += 1
                    dfs(v)
                    # update low value after returning from DFS
                    low[u] = min(low[u], low[v])

                    # 🔥 Articulation condition (non-root)
                    # If child cannot reach above u
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True

            # 🔥 Root articulation condition
            if parent[u] == -1 and children > 1:
                ap[u] = True

        # 🔹 Run DFS for all components (graph may be disconnected)
        for i in range(V):
            if not visited[i]:
                dfs(i)

        # 🔹 Collect articulation points
        result = [i for i in range(V) if ap[i]]

        # 🔹 If none found, return [-1]
        return result if result else [-1]
    
# Core Difference
# Problem	Condition
# Articulation Point	low[v] >= disc[u]
# Bridge	low[v] > disc[u]
