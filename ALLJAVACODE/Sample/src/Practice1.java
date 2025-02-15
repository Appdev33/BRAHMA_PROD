import java.util.*;

//import Graph.BFS01.Edge;

//Belman Ford
//Kosaraju Algo  - Minimum no of Count of Strongly Connected Algorithms
//Articulation Points and Bridges - 


public class Practice1 {
	
	
    static class Edge {
        int from, to, weight;

        public Edge(int from, int to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }
    }
       
 	private static void bellmanFord(ArrayList<ArrayList<Edge>> graph, int vertices, int source) {
 	    int[] distance = new int[vertices];
 	    Arrays.fill(distance, Integer.MAX_VALUE);
 	    distance[source] = 0;

 	    // Relax edges |V| - 1 times
 	    for (int i = 0; i < vertices - 1; i++) {
 	        System.out.println("Iteration " + (i + 1) + ":");
 	        for (int u = 0; u < vertices; u++) {
 	            for (Edge edge : graph.get(u)) {
 	                int v = edge.to;
 	                int weight = edge.weight;
 	                if (distance[u] != Integer.MAX_VALUE && distance[u] + weight < distance[v]) {
 	                    distance[v] = distance[u] + weight;
 	                }
 	            }
 	        }
 	        System.out.println("Distances: " + Arrays.toString(distance));
 	    }

 	    // Negative Cycle Detection
 	    for (int u = 0; u < vertices; u++) {
 	        for (Edge edge : graph.get(u)) {
 	            int v = edge.to;
 	            int weight = edge.weight;
 	            if (distance[u] != Integer.MAX_VALUE && distance[u] + weight < distance[v]) {
 	                System.out.println("Negative cycle detected at edge: " + u + " -> " + v + " with weight " + weight);
 	                return;
 	            }
 	        }
 	    }

 	    System.out.println("Shortest distances from source vertex " + source + ":");
 	    for (int i = 0; i < distance.length; i++) {
 	        System.out.println("Vertex " + i + " : " + distance[i]);
 	    }
 	}

 	public static void BFS(ArrayList<ArrayList<Edge>> graph, boolean[] visited, int src) {
 		Queue<Integer> queue = new LinkedList<>();
 		
 		queue.add(src);
 		
 		visited[src] = true;
 		
 		while(!queue.isEmpty()) {
 			Integer nbr = queue.poll();
 			System.out.println("Visited"+nbr);
 			
 			for(Edge nbr1 : graph.get(nbr)) {
 				if(!visited[nbr1.to]) {
 					visited[nbr1.to] = true;
 					queue.add(nbr1.to);
 				}
 			}
 			
 		}
 	}
 	
 	public static void DFS(ArrayList<ArrayList<Edge>> graph, boolean[] visited, int i) {
 		
 		visited[i] = true;
 		System.out.println("Visited"+i);
 		
 		for(Edge nbr : graph.get(i)) {
 			if(!visited[nbr.to]) {
 				DFS(graph,visited,nbr.to);
 			}
 		}
 		
 	}
    
   static class KrushkalAlgo{

    	
    	int parent[];
    	int rank[];
    	
    	
    	KrushkalAlgo(int vertices){
    		parent = new int[vertices];
    		rank = new int[vertices];
    		Arrays.fill(parent, -1);
    		Arrays.fill(rank, 0);
    	}	
    	
    	public int find(int x) {
    		
    		if(parent[x]<0)
    			return x;
    		
    		parent[x] = find(parent[x]);
    		
    		return parent[x];
    	}
    	
    	public void union(int x, int y) {
    		
    		int rootX = find(x);
    		int rootY = find(y);
    		
    		if (rootX != rootY) {
                // Union by rank: compare ranks to decide which tree to attach
                if (rank[rootX] < rank[rootY]) {
                    parent[rootX] = rootY;
                } else if (rank[rootX] > rank[rootY]) {
                    parent[rootY] = rootX;
                } else {
                    parent[rootY] = rootX;
                    rank[rootX]++; // Only increment the rank for rootX if ranks are equal
                }
            }
    	}
    }
   
   static class KosarajuAlgo{
	   private int vertices;
	   
	   KosarajuAlgo(int vertices){
		   this.vertices = vertices;
	   }
	   
	   public void dfs(int src, List<List<Integer>> graph2, Stack<Integer> stack, boolean visited[]) {
		   
		   visited[src] = true;
		   
		   for(int neigh: graph2.get(src)) {
			   if(!visited[neigh])
				   dfs(neigh , graph2, stack, visited);
		   }
		   stack.push(src);
		   
	   }
	   
	   public void dfsKosaraju(int src, Map<Integer, List<Integer>> graphInverted, boolean visited[], List<Integer> component) {
		   
		   visited[src] = true;
		   component.add(src);

		   for(int neigh: graphInverted.get(src)) {
			   if(!visited[neigh]) {
				   dfsKosaraju(neigh , graphInverted,  visited, component);
			   }
		   }
	   }
   }
//   https://www.youtube.com/watch?v=sAk4W8q0Rmw&list=PL-Jc9J83PIiEuHrjpZ9m94Nag4fwAvtPQ&index=23
   static List<List<Integer>> articulationBrideges = new ArrayList<>();
   static class ArticulationPoints {
       static int lowestDiscovery[];
       static int discovery[];
       static int time;
       static int articulationPoint[];
       static int parent[];
       static boolean visited[];

       ArticulationPoints(int n) {
           lowestDiscovery = new int[n];
           discovery = new int[n];
           articulationPoint = new int[n];
           parent = new int[n];
           visited = new boolean[n];
           Arrays.fill(parent, -1); // Initialize parent as -1
           time = 0;
       }

       public void dfs(Map<Integer, List<Integer>> graph, int src) {
           visited[src] = true;
           discovery[src] = lowestDiscovery[src] = ++time;
           int children = 0;

           for (int neighbor : graph.getOrDefault(src, Collections.emptyList())) {
        	   
        	   if(parent[src] == neighbor)
        		   continue;
        	   else if(visited[neighbor]== true) {  // Back edge exits with lower reach?
        		   lowestDiscovery[src] = Math.min(lowestDiscovery[src], discovery[neighbor]);
        	   }else {
        		     parent[neighbor] = src;
	                 children++;
	
	                 // Recursive DFS call
	                 dfs(graph, neighbor);
	
	                 // Update lowestDiscovery[src] based on the child
	                 lowestDiscovery[src] = Math.min(lowestDiscovery[src], lowestDiscovery[neighbor]);  // check seperately for 
	                 																		//	                 root node as >= valid always for source
	
	                 // Articulation point conditions
	                 if (parent[src] == -1 && children > 1) { // Case 1: Root node
	                     articulationPoint[src] = 1;
	                 }
	                 if (parent[src] != -1 && lowestDiscovery[neighbor] >= discovery[src]) { // Case 2: Non-root node
	                     articulationPoint[src] = 1;
	                 }
	                 
//	                 lowestDiscovery[neighbor] >= discovery[src]) this condtion for articulation point
//	                 lowestDiscovery[neighbor] > discovery[src]) this condtion for articulation bridge
	                 
        	   }
//        	   Key Insight:
//        		   For a root node to be an articulation point, it must have at least two independent subtrees in the DFS spanning tree. 
//        		   Each subtree would be disconnected from the rest of the graph if the root is removed.
        	   
//        	   Why This Works:
//        		   This condition applies to non-root nodes and checks if the node acts as a bridge between its subtree and the rest of the graph.
//        		   lowestDiscovery[neighbor] is the smallest discovery time reachable from the neighbor’s subtree.
//        		   If lowestDiscovery[neighbor] >= discovery[src], it means:
//        		   The neighbor’s subtree cannot reach any ancestor of src in the DFS tree.
//        		   Removing src would disconnect this subtree from the rest of the graph.
//        		   Key Insight:
//        		   For a non-root node to be an articulation point, it must separate a part of the graph into an isolated component.
//        		   This happens when none of the nodes in the neighbor’s subtree can reconnect to the graph through a back edge.
        	   
//               if (!visited[neighbor]) {
//                   parent[neighbor] = src;
//                   children++;
//
//                   // Recursive DFS call
//                   dfs(graph, neighbor);
//
//                   // Update lowestDiscovery[src] based on the child
//                   lowestDiscovery[src] = Math.min(lowestDiscovery[src], lowestDiscovery[neighbor]);
//
//                   // Articulation point conditions
//                   if (parent[src] == -1 && children > 1) { // Case 1: Root node
//                       articulationPoint[src] = 1;
//                   }
//                   if (parent[src] != -1 && lowestDiscovery[neighbor] >= discovery[src]) { // Case 2: Non-root node
//                       articulationPoint[src] = 1;
//                   }
//               } 
//               else if (neighbor != parent[src]) { // Back edge
//                   lowestDiscovery[src] = Math.min(lowestDiscovery[src], discovery[neighbor]);
//               }
        	   
           }
       }
       public void dfsBridges(Map<Integer, List<Integer>> graph, int src) {
    	    visited[src] = true;
    	    discovery[src] = lowestDiscovery[src] = ++time;

    	    for (int neighbor : graph.getOrDefault(src, Collections.emptyList())) {
    	        if (parent[src] == neighbor) {
    	            // Ignore the edge to the parent node
    	            continue;
    	        } else if (visited[neighbor]) {
    	            // Back edge exists, update the lowest discovery time
    	            lowestDiscovery[src] = Math.min(lowestDiscovery[src], discovery[neighbor]);
    	        } else {
    	            // Recursive DFS for unvisited neighbor
    	            parent[neighbor] = src;
    	            dfsBridges(graph, neighbor);

    	            // Update the lowest discovery time after visiting the child
    	            lowestDiscovery[src] = Math.min(lowestDiscovery[src], lowestDiscovery[neighbor]);

    	            // Check if the edge (src -> neighbor) is a bridge
    	            if (lowestDiscovery[neighbor] > discovery[src]) {
    	            	articulationBrideges.add(Arrays.asList(src, neighbor));
    	            }
    	        }
    	    }
    	}

       
       public void printPoints() {
    	   for(int ap: articulationPoint) {
    		   System.out.print(ap+" ");
    	   }
    	   System.out.println("Articulation Bridges");
    	   System.out.println(articulationBrideges);
       }
       
   }

   public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int n = 6; // Number of vertices
		
        ArrayList<ArrayList<Edge>> graph = new ArrayList<>();
        List<Edge> edges = new ArrayList<>();
        

        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        // Adding edges to the graph
//        graph.get(0).add(new Edge(0, 1, 0));
//        graph.get(0).add(new Edge(0, 2, 1));
//        graph.get(1).add(new Edge(1,3, 1));
//        graph.get(1).add(new Edge(1, 4, 0));
//        graph.get(2).add(new Edge(2, 4, 1));
//        graph.get(3).add(new Edge(3, 5, 1));
//        graph.get(4).add(new Edge(4, 5, 0));
        
        edges.add(new Edge(0, 1, 10));
        edges.add(new Edge(0, 2, 6));
        edges.add(new Edge(0, 3, 5));
        edges.add(new Edge(1, 3, 15));
        edges.add(new Edge(2, 3, 4));
        edges.add(new Edge(2, 1, 7));  // This creates a cycle
        edges.add(new Edge(3, 4, 3));  // This creates a cycle
        edges.add(new Edge(4, 0, 2));  // This creates a cycle

        boolean visited[] = new boolean[n];
//		BFS(graph,visited,0);
//		System.out.println("DFS");
//		Arrays.fill(visited, false);
//		DFS(graph,visited,0);
        
        //BELMAN FORD
        System.out.println("###################### BELMANN FORD ALGO###############");
        
        graph.get(0).add(new Edge(0, 1, 2));
        graph.get(0).add(new Edge(0, 2, 4));
        graph.get(1).add(new Edge(1, 2, -3));
        graph.get(1).add(new Edge(1, 3, 2));
        graph.get(2).add(new Edge(2, 4, 2));
        graph.get(3).add(new Edge(3, 5, 1)); 
        graph.get(4).add(new Edge(4, 3, -2));
        graph.get(5).add(new Edge(5, 4, 1));

        
        // Step 2: Apply Bellman-Ford Algorithm
        int source = 0; // Starting vertex
        int verticesB = graph.size();
        bellmanFord(graph, verticesB, source);

        
        //KRUSHKAL MST
       
        int vertices = edges.size();
        Collections.sort(edges, (a,b)->a.weight-b.weight);
        
        KrushkalAlgo uf = new KrushkalAlgo(vertices);
        List<Edge> mst = new ArrayList<>();
        int mstWeight = 0;
        
        for (Edge edge : edges) {
            int u = edge.from;
            int v = edge.to;

            if (uf.find(u) != uf.find(v)) {
                uf.union(u, v);
                mst.add(edge);
                mstWeight += edge.weight;
            }

            // Stop once we have V-1 edges in the MST
            if (mst.size() == vertices - 1) {
                break;
            }
        }
        
        // Output the MST
        System.out.println("Edges in the Minimum Spanning Tree:");
        for (Edge edge : mst) {
            System.out.println(edge.from + " -- " + edge.to + " : " + edge.weight);
        }
        System.out.println("Total weight of MST: " + mstWeight);
        
        
//        ########### KOSARAJU ALGO
        System.out.println("###################### KOSARAJU ALGO###############");
        
	        List<List<Integer>> graph2 = new ArrayList<>();
	        
	        List<List<Integer>> scss = new ArrayList<>();
	
	        int nodes = 13; // Total number of nodes (0 to 12)
	
	        // Initialize adjacency list
	        for (int i = 0; i < nodes; i++) {
	            graph2.add(new ArrayList<>());
	        }
        	
	        graph2.get(0).add(1);
	        graph2.get(1).add(2);
	        graph2.get(2).add(0);
	        graph2.get(1).add(3);
	        graph2.get(3).add(4);
	        graph2.get(4).add(5);
	        graph2.get(5).add(3);
	        graph2.get(2).add(6);
	        graph2.get(6).add(7);
	        graph2.get(7).add(8);
	        graph2.get(8).add(6);
	        graph2.get(7).add(9);
	        graph2.get(8).add(9);
	        graph2.get(9).add(10);
	        graph2.get(10).add(11);
	        graph2.get(11).add(12);
	        graph2.get(12).add(10);
	        
	        KosarajuAlgo obj =new KosarajuAlgo(nodes);
	        int countStrongComponents = 0;
	        
	        //STEP 1
	        
	        visited = new boolean[nodes];
	        Stack<Integer> stack = new Stack<>();
	        
	        for(int v=0; v<graph2.size(); v++) {
	        	if(!visited[v])
	        		obj.dfs(v , graph2, stack, visited);
	        }
	         
	        //STEP 2
	        Map<Integer, List<Integer> >  graphInverted = new HashMap<>();
	        
	        for (int i = 0; i < nodes; i++) {
	            for (int neigh : graph2.get(i)) {
	                graphInverted.computeIfAbsent(neigh, k -> new ArrayList<>()).add(i);
	            }
	        }
	        
//	        obj.invertGraph(graph2,);
	        //STEP 3
	        Arrays.fill(visited, false);
	        while(!stack.isEmpty()) {
	        	int curr = stack.pop(); 
	        	if(!visited[curr]) {
	        		List<Integer> component = new ArrayList<>();
	        		obj.dfsKosaraju(curr , graphInverted, visited, component); 
	        		countStrongComponents++;
	        		scss.add(component);
	        	}
	        }
	       System.out.println("Number of Connected Components "+ countStrongComponents);
	       System.out.println(scss);
	       
	       
	       System.out.println("###################### ARTICULATION POINT AND BRIDGES CUT VERTEX ###############");
	       int n2 = 7; // Number of vertices
	       Map<Integer, List<Integer>> Agraph2 = new HashMap<>();

	       // Initialize adjacency list for all vertices
	       for (int i = 0; i < n2; i++) {
	           Agraph2.put(i, new ArrayList<>());
	       }

	       // Add edges (example graph)
	       Agraph2.get(0).add(1);
	       Agraph2.get(1).add(0);

	       Agraph2.get(0).add(3);
	       Agraph2.get(3).add(0);

	       Agraph2.get(1).add(2);
	       Agraph2.get(2).add(1);

	       Agraph2.get(2).add(3);
	       Agraph2.get(3).add(2);

	       Agraph2.get(3).add(4);
	       Agraph2.get(4).add(3);

	       Agraph2.get(4).add(5);
	       Agraph2.get(5).add(4);

	       Agraph2.get(4).add(6);
	       Agraph2.get(6).add(4);

	       ArticulationPoints ap = new ArticulationPoints(n2);
	       ap.dfs(Agraph2, n2-1);
	       ap.printPoints();
	       ap.dfs(Agraph2, source);
	       
	       
	       
   }

}
   
