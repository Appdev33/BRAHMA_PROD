import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;


//DFS
//BFS
//TopoSort DFS
//TopoSort BFS
//Cycle Detection directed
//Cycle Detection undirected
//Set Union Find
//Trie
//KrushKal
//Prims
//Djikhstra 

//01 BFS 
//Belman Ford



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


public class Graphs2 {
	
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
	
//	1. With Path Compression and Union by Rank/Size (Optimized DSU):
//	Overall Time Complexity:
//	O(m × α(n)), where m is the number of operations and α(n) is the inverse Ackermann function.
//
//	Overall Space Complexity:
//	O(n).
//
//	2. Without Path Compression (Uncompressed DSU):
//	Overall Time Complexity:
//	O(m × n), where m is the number of operations and n is the number of elements.
//
//	Overall Space Complexity:
//	O(n).
	static class UnionFind{
		
		int parent[];
		
		public UnionFind(int size) {
			parent = new int[size];
			
			for(int i=0; i<size; i++)
				parent[i] = -1;
		}
		
		public int find(int x) {
		    if (parent[x] < 0) {
		        return x; // x is the root
		    }
		    int leader = find(parent[x]);
		    return leader;
		}
		
		public void Union(int x, int y) {
			int rootX = find(x);
			int rootY = find(y);
			
			if(rootX != rootY) {
				parent[rootX] = rootY;
			}
		}
	}
	
	static class UnionFindCompressed{
		int parent[];
		int rank[];
		
		public UnionFindCompressed(int size) {
			parent = new int[size];
			rank = new int[size];
			
			Arrays.fill(parent,-1);
			Arrays.fill(rank,1);
		}
		
		public int findCompressed(int x) {
			if(parent[x]<0)
				return x;
			
	        // Path compression
			int leader = findCompressed(parent[x]);
	        parent[x] = leader;
	        return leader;
		}
		
		public void UnionCompressed(int x, int y) {
			int rootX = findCompressed(x);
			int rootY = findCompressed(y);

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
		
	private static void BFS(boolean[] visited, int src, ArrayList<Edge>[] graph) {
	    Queue<Integer> queue = new LinkedList<>();
	    
	    queue.add(src);
	    visited[src] = true; // Mark the source as visited when enqueuing it
	    
	    while(!queue.isEmpty()) {
	        
	        int poll = queue.poll();
	        System.out.println("visited BFS:===>" + poll);
	        
	        for(Edge neigh: graph[poll]) {
	            if(!visited[neigh.nbr]) {
	                visited[neigh.nbr] = true; // Mark as visited when enqueuing
	                queue.add(neigh.nbr);
	            }
	        }
	    }
	}
	
	public static void DFS(boolean[] visited, int src, ArrayList<Edge>[] graph) {
		
		visited[src] = true;
		System.out.println("visited DFS:===>" + src);
		for(Edge edg: graph[src]){
			if(!visited[edg.nbr])
				DFS(visited, edg.nbr, graph);
		}
		
	}
	
	public static void TopoBFS(Queue<Integer> queue, ArrayList<Edge>[] graphDirected, int[] order, int indegree[]) {
		
		while(!queue.isEmpty()) {
			
			int poll = queue.poll();
			order[index++] = poll;
			
			for(Edge e: graphDirected[poll]) {
				--indegree[e.nbr];
				
				if(indegree[e.nbr]==0)
					queue.add(e.nbr);
			}
		}
	}
	
	public static void TopoDFS(boolean[] visited, int src, ArrayList<Edge>[] graphDirected, Stack<Integer> stack) {
		
		visited[src] = true;
		
		for(Edge e : graphDirected[src]) {
			if(!visited[e.nbr])
				TopoDFS(visited,e.nbr,graphDirected,stack);
		}
		stack.push(src);
	}
	
	public static boolean LoopDirectedGraph(int v, ArrayList<Edge>[] graphDirected, boolean[] visited,
			boolean[] recStack) {
		
		visited[v] = true;
		recStack[v] = true;
		
		for(Edge e : graphDirected[v]) {
			if(!visited[e.nbr] && LoopDirectedGraph(e.nbr, graphDirected, visited, recStack))
				return true;
			else if(recStack[e.nbr])  // if already visited encountered again and also in same path of recStack visited then true
				return true;
		}
		recStack[v] = false;
		return false;
	}

	private static boolean CycleDetectUnDirected(int i, ArrayList<Edge>[] graph, boolean[] visited, int parent) {
		
		visited[i] = true;
		
		for(Edge e : graph[i]) {
			if(!visited[e.nbr] && CycleDetectUnDirected(e.nbr, graph, visited, i))
				return true;
			else if(e.nbr != parent)  // if already visited encountered again and it is Not a back edge to parent where you started
				return true;
		}
		return false;
	}
	
	
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int vtces = Integer.parseInt(br.readLine());
		ArrayList<Edge>[] graph = new ArrayList[vtces];
		ArrayList<Edge>[] graphDirected = new ArrayList[vtces];
		for (int i = 0; i < vtces; i++) {
			graph[i] = new ArrayList<>();
			graphDirected[i] = new ArrayList<>();
		}
		
		int edges = Integer.parseInt(br.readLine());
		
		int indegree[] = new int[vtces];  //Topo Sort
		
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
		
									System.out.println("*********BFS***********");
		BFS(visited,src,graph);
		Arrays.fill(visited, false);
		
									System.out.println("*********DFS***********");
		DFS(visited,src,graph);
		
								    System.out.println("*********Topo DFS***********");
		Arrays.fill(visited, false);
		Stack<Integer> stack = new Stack<>();
//		TopoDFS(visited,src,graphDirected,stack);

        for (int v = 0; v < vtces; v++) {              //Remember this loop in TopoDfs
            if (!visited[v]) {
            	TopoDFS(visited, v, graphDirected, stack);
            }
        }
		while(!stack.isEmpty()) {
			System.out.println("visited Topo DFS:===>" + stack.pop());
		}
		
									System.out.println("*********Topo BFS***********");
		Arrays.fill(visited, false);
		Queue<Integer> queue = new LinkedList<>();
		int order[] = new int[vtces];
		
		for(int v=0; v<vtces; v++) {
			if(indegree[v]==0)
				queue.add(v);
		}
		
		TopoBFS(queue, graphDirected, order, indegree);
	    for(int i: order)
	    	System.out.println("visited Topo BFS:===>" + i);
	    
	    						     System.out.println("*********Loop Directed***********");  //https://www.youtube.com/watch?v=9twcmtQj4DU
	    Arrays.fill(visited, false);
	    boolean recStack[] = new boolean[vtces];
	    boolean cycleExists = false;
	    for(int v=0; v<vtces; v++) {
	    	if (LoopDirectedGraph(v, graphDirected, visited, recStack)) {
                cycleExists = true;
                break;
            }
	    }
       Runnable printCycleResult = cycleExists ? 
               () -> System.out.println("Cycle Exists in directed ") : 
               () -> System.out.println("No cycle in directed");
           printCycleResult.run();
	    
           							 System.out.println("*********Loop UnDirected***********");   //https://www.youtube.com/watch?v=zQ3zgFypzX4
	    cycleExists = false;
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
		for(int i=0; i<vtces; i++) {
			for(Edge e: graph[i])
				uf.Union(e.src, e.nbr);
		}
		
        // Find operation (for demonstration):
        for (int i = 0; i < vtces; i++) {
            System.out.println("Parent of node " + i + ": " + uf.parent[i]);
        }
        
        						     System.out.println("*********Compressed Union Find  ***********");
        UnionFindCompressed uf2 = new UnionFindCompressed(vtces);
		for(int i=0; i<vtces; i++) {
			for(Edge e: graph[i])
				uf2.UnionCompressed(e.src, e.nbr);
		}
		
        // Find operation (for demonstration):
        for (int i = 0; i < vtces; i++) {
            System.out.println("Parent of node " + i + ": " + uf2.parent[i]);
        }
		
	}
}
