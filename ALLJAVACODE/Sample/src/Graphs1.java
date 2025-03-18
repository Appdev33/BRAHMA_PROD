import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;



//DFS
//BFS
//TopoSort BFS
//TopoSort DFS
//Cycle Detection directed
//Cycle Detection undirected
//Set Union Find
//Bellman Ford
//Djikhstra
//Prims
//KrushKal



/*
7
8
0 1 10
1 2 10
2 3 10
0 3 10
3 4 10
4 5 10
5 6 10
4 6 10
2
 */

public class Graphs1 {
	
static int index = 0;
	
	static class Edge {
	      int src;
	      int nbr;
	      int wt;

	      Edge(int src, int nbr, int wt) {
	         this.src = src;
	         this.nbr = nbr;
	         this.wt = wt;
	      }
	   }

//	   static class Pair{
//	       int node;
//	       int wt;
//	       
//	       Pair(int node, int wt){
//	           this.node = node;
//	           this.wt = wt;
//	       }
//	   }
	
	static class UnionFind {
		
		int parent[];
		
		public UnionFind(int size) {
			parent = new int[size];
			
			for(int i=0; i<size; i++) {
				parent[i] = -1;
			}
			
		}
		
		public int find(int x) {
			while(parent[x]>=0)
				x = parent[x];
			return x;
		}
		
		public void Union(int x, int y) {
			int rootX = find(x); 
			int rootY = find(y);
			
			if(rootX != rootY)
				parent[rootY] = rootX;	
		}
		
	}
	
	
	static class UnionFindCompression {
		
		int parent[];
		int rank[];
		
		public UnionFindCompression(int size) {
			parent = new int[size];
			rank = new int[size];

			Arrays.fill(parent,-1);
			Arrays.fill(rank,1);
		}
		
		public int findCompression(int x) {
//			return find(parent[x]);
			
	        if (parent[x] < 0) {
	            return x;
	        }
	        // Path compression
	        parent[x] = findCompression(parent[x]);
	        return parent[x];
	    }
		
		public void Union(int x, int y) {
	        int rootX = findCompression(x);
	        int rootY = findCompression(y);

	        if (rootX != rootY) {
	            // Union by rank
	            if (rank[rootX] < rank[rootY]) {
	                parent[rootX] = rootY;
	            } else if (rank[rootX] > rank[rootY]) {
	                parent[rootY] = rootX;
	            } else {
	                parent[rootY] = rootX;
	                rank[rootX]++;
	            }
	        }
	    }
		
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int vtces = Integer.parseInt(br.readLine());
		ArrayList<Edge>[] graph = new ArrayList[vtces];
		ArrayList<Edge>[] graphDirected = new ArrayList[vtces];
		for (int i = 0; i < vtces; i++) {
			graph[i] = new ArrayList<>();
			graphDirected[i] = new ArrayList<>();
		}
		
		int edges = Integer.parseInt(br.readLine());
		
		int indegree[] = new int[vtces];
		
		for (int i = 0; i < edges; i++) {
			
		     String[] parts = br.readLine().split(" ");
		     int v1 = Integer.parseInt(parts[0]);
		     int v2 = Integer.parseInt(parts[1]);
		     int wt = Integer.parseInt(parts[2]);
		     
		     graph[v1].add(new Edge(v1, v2, wt));
		     graph[v2].add(new Edge(v2, v1, wt));  
		     
		     graphDirected[v1].add(new Edge(v1, v2, wt));  //Directed for directed algorithms
		     ++indegree[v2];
		}
		      
		int src = Integer.parseInt(br.readLine());	 
		
		boolean visited[] = new boolean[vtces];
		BFS(visited, src,graph);
		Arrays.fill(visited, false);
		
		System.out.println("*********DFS***********");
		DFS(visited, src,graph);
		Arrays.fill(visited, false);
		
		
		System.out.println("*********Topo BFS***********");
		Queue<Integer> queue = new LinkedList<>();
		for(int i=0; i<indegree.length; i++) {
				if(indegree[i]==0)
					queue.add(i);
//			System.out.println("indegree" + i);
		}
		int order[] = new int[vtces];
		TopoSortBfs(src,graphDirected, queue,order,indegree);
	    for(int i: order)
	    	System.out.println("visited Topo BFS:===>" + i);
		Arrays.fill(visited, false);
		
		
		System.out.println("*********Topo DFS***********");
        Stack<Integer> st = new Stack<>();
        for (int v = 0; v < vtces; v++) {              //Remember this loop in TopoDfs
            if (!visited[v]) {
            	TopoSortDFS(v, graphDirected, st, visited);
            }
        }
		while(!st.isEmpty()) {
			System.out.println("visited Topo DFS:===>" + st.pop());
		}
		
		
		System.out.println("*********Cycle Directed Graph ***********");
		Arrays.fill(visited, false);
        boolean[] recStack = new boolean[vtces];
        boolean cycleExists = false;
        for (int i = 0; i < vtces; i++) {
            if (CycleDetectDirected(i, graphDirected, visited, recStack)) {
                cycleExists = true;
                break;
            }
        }

        // Using a lambda expression to print the result
        Runnable printCycleResult = cycleExists ? 
            () -> System.out.println("Cycle Exists in directed ") : 
            () -> System.out.println("No cycle in directed");
        printCycleResult.run();
        
        
		System.out.println("*********Cycle UnDirected Graph ***********");
		
		
		Arrays.fill(visited, false);
        for (int i = 0; i < vtces; i++) {
            if (CycleDetectUnDirected(i, graph, visited, -1)) {
                cycleExists = true;
                break;
            }
        }

        // Using a lambda expression to print the result
        Runnable printCycleResult2 = cycleExists ? 
            () -> System.out.println("Cycle Exists in undirected ") : 
            () -> System.out.println("No cycle in undirected");
        printCycleResult2.run();
        
        
		System.out.println("*********Union Find  ***********");
		UnionFind uf = new UnionFind(vtces);
		// Union operations based on edges (for demonstration):
        for (int i = 0; i < vtces; i++) {
            for (Edge e : graph[i]) {
                uf.Union(e.src, e.nbr);
            }
        }
        // Find operation (for demonstration):
        for (int i = 0; i < vtces; i++) {
            System.out.println("Parent of node " + i + ": " + uf.find(i));
        }
        
        System.out.println("*********Compressed Union Find  ***********");
        UnionFindCompression cuf = new UnionFindCompression(vtces);
		// Union operations based on edges (for demonstration):
        for (int i = 0; i < vtces; i++) {
            for (Edge e : graph[i]) {
            	cuf.Union(e.src, e.nbr);
            }
        }
        // Find operation (for demonstration):
        for (int i = 0; i < vtces; i++) {
            System.out.println("Parent of node " + i + ": " + cuf.findCompression(i));
        }
	}
	
	private static boolean CycleDetectUnDirected(int i, ArrayList<Edge>[] graph, boolean[] visited, int parent) {
	// TODO Auto-generated method stub
		visited[i] = true;
		
        for (Edge neigh : graph[i]) {
            if (!visited[neigh.nbr]) {
                if (CycleDetectUnDirected(neigh.nbr, graph, visited, i)) {
                    return true;
                }
            } else if (neigh.nbr != parent) {
                return true;
            }
        }

        return false;
}

	private static boolean CycleDetectDirected(int i, ArrayList<Edge>[] graphDirected, boolean[] visited,
		boolean[] recStack) {
	// TODO Auto-generated method stub
		visited[i] = true;
		recStack[i] = true;
		
		for(Edge neigh: graphDirected[i]) {
			
			if(!visited[neigh.nbr] && CycleDetectDirected(neigh.nbr, graphDirected, visited,recStack))
				return true;
			else if(recStack[neigh.nbr])
				return true;
		}
		
        recStack[i] = false;
        return false;
        
	}

	private static void TopoSortDFS(int src, ArrayList<Edge>[] graphDirected, Stack<Integer> stack, boolean[] visited) {
		// TODO Auto-generated method stub
		visited[src] = true;
		
		for(Edge neigh: graphDirected[src]) {
			if(!visited[neigh.nbr]) {
				TopoSortDFS(neigh.nbr,graphDirected, stack,visited);
			}
		}
		stack.push(src);
		
	}

	private static void TopoSortBfs(int src, ArrayList<Edge>[] graphD, Queue<Integer> queue, int[] order, int[] indegree) {
		
		while(!queue.isEmpty()) {
			int pop = queue.poll();
			
			order[index++]= pop;
			
			for(Edge e: graphD[pop]) {
				--indegree[e.nbr];
				
	    		  if(indegree[e.nbr]==0)
	    			  queue.add(e.nbr);
	    	  }
			}
	}

	private static void DFS(boolean[] visited, int src, ArrayList<Edge>[] graph) {

			// TODO Auto-generated method stub
					
			visited[src]=true;

			System.out.println("visited DFS:===>" + src);
			
			for(Edge neigh : graph[src]) {
				if(visited[neigh.nbr])
					continue;
				else {
					visited[neigh.nbr]=true;
					DFS(visited, neigh.nbr, graph);
				}
			}
	}
	
	private static void BFS(boolean[] visited, int src, ArrayList<Edge>[] graph) {
		// TODO Auto-generated method stub
		System.out.println("*********BFS***********");
		Queue<Integer> queue = new LinkedList<>();
		
		queue.add(src);
		
		while(!queue.isEmpty()) {
			
			int poll = queue.poll();
			visited[poll]=true;
			System.out.println("visited BFS:===>" + poll);
			
			for(Edge neigh: graph[poll]) {
				if(visited[neigh.nbr])
					continue;
				else {
					visited[neigh.nbr]=true;
					queue.add(neigh.nbr);
				}
			}
		}
	}
}

//Map<Integer, ArrayList<Edge>> graph = new HashMap<>();
//
//for(int i=0 ; i<n ; i++){
//    
//    graph.computeIfAbsent(flights[i][0], p->new ArrayList<>()).add(new Edge(flights[i][0], flights[i][2], flights[i][2]));
//}



/*
 In the provided code snippet, the logic checks for cycles in a directed graph using Depth-First Search (DFS) with recursion. The purpose of the if condition in the code is to detect whether there is a cycle in the directed graph. Let's break down the logic:

Initialization:

visited[i] is marked as true to indicate that the node i has been visited.
recStack[i] is also marked as true to indicate that the node i is currently in the recursion stack.
DFS Traversal:

The loop iterates through all the neighbors (neigh) of the current node i.
if (!visited[neigh.nbr] && CycleDetectDirected(neigh.nbr, graphDirected, visited, recStack)):
This checks if the neighbor neigh.nbr has not been visited yet.
If neigh.nbr has not been visited, the CycleDetectDirected function is called recursively for this neighbor.
If this recursive call returns true, it means a cycle has been detected, so the function immediately returns true.
else if (recStack[neigh.nbr]):
If the neighbor neigh.nbr has already been visited and is currently in the recursion stack (recStack), it means we have encountered a back edge, indicating a cycle.
Therefore, the function returns true.
Backtracking:

If no cycle is detected among the neighbors, the current node i is removed from the recursion stack by setting recStack[i] to false.
No Cycle Found:

If the function completes the for loop without finding a cycle, it returns false, indicating no cycle has been detected from the current node i.

 */


/*
 Certainly! The parent parameter is crucial in distinguishing between legitimate backtracking to a parent node (which does not indicate a cycle) and encountering a previously visited node that is not the parent (which does indicate a cycle).

Explanation of the parent Parameter
In an undirected graph, when you traverse from a node to one of its neighbors, you are essentially moving along an edge that can be traveled in both directions. When you backtrack to the node from which you came, it's not considered a cycle. The parent parameter helps to identify this backtracking.

Here's a detailed breakdown:

Parent Parameter Usage:

When you call the recursive function CycleDetectUnDirected, you pass the current node as the parent parameter for the next call.
This way, the function knows the node from which it came (i.e., the parent node).
Avoiding False Cycle Detection:

When the function encounters a visited neighbor, it needs to check if this neighbor is the parent.
If the visited neighbor is the parent, it means you are simply backtracking to the previous node, which is expected in an undirected graph traversal.
If the visited neighbor is not the parent, it means there is an additional path to a previously visited node, indicating a cycle.
 */
 