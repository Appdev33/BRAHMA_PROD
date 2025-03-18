import java.util.*;
import java.util.HashMap;

public class Debugging {
	
	public static int longestJokeChain(List<List<String>> edges) {
        // Build the graph and calculate in-degrees
        Map<String, List<String>> graph = new HashMap<>();
        Map<String, Integer> inDegree = new HashMap<>();
        
        for (List<String> edge : edges) {
            String u = edge.get(0);
            String v = edge.get(1);
            
            graph.putIfAbsent(u, new ArrayList<>());
            graph.putIfAbsent(v, new ArrayList<>());
            graph.get(u).add(v);
            
            inDegree.put(v, inDegree.getOrDefault(v, 0) + 1);
            inDegree.putIfAbsent(u, 0);
        }
        
        // Topological Sort using Kahn's Algorithm
        Queue<String> queue = new LinkedList<>();
        Map<String, Integer> dp = new HashMap<>(); // dp[node]: longest chain ending at node
        
        // Add nodes with no incoming edges (sources) to the queue
        for (String node : inDegree.keySet()) {
            if (inDegree.get(node) == 0) {
                queue.add(node);
                dp.put(node, 1); // Chain length is 1 for sources
            }
        }
        
        int maxLength = 0;
        
        while (!queue.isEmpty()) {
            String current = queue.poll();
            int currentLength = dp.get(current);
            
            for (String neighbor : graph.get(current)) {
                dp.put(neighbor, Math.max(dp.getOrDefault(neighbor, 0), currentLength + 1));
                inDegree.put(neighbor, inDegree.get(neighbor) - 1);
                if (inDegree.get(neighbor) == 0) {
                    queue.add(neighbor);
                }
            }
            
            maxLength = Math.max(maxLength, currentLength);
        }
        
        return maxLength;
    }

    public static void main(String[] args) {
        // Example input: Edges representing who tells the joke to whom
        List<List<String>> edges = Arrays.asList(
            Arrays.asList("A", "B"),
            Arrays.asList("B", "C"),
            Arrays.asList("C", "D"),
            Arrays.asList("E", "F"),
            Arrays.asList("F", "C")
        );
        
        int result = longestJokeChain(edges);
        System.out.println("Length of the longest joke chain: " + result); // Output: 4
    }

	

//	    public static List<Integer> findKings(int[] powers) {
//	        int totalPower = 0;
//	        Map<Integer, Integer> powerCount = new HashMap<>();
//
//	        // Calculate total power and populate the frequency map
//	        for (int power : powers) {
//	            totalPower += power;
//	            powerCount.put(power, powerCount.getOrDefault(power, 0) + 1);
//	        }
//	        
//	        System.out.println(powerCount);
//	        List<Integer> kings = new ArrayList<>();
//
//	        // Iterate through each power in the array
//	        for (int power : powers) {
//	            double requiredPower = (totalPower - power) / 2.0;
//
//	            // Temporarily reduce the count of the current power
//	            powerCount.put(power, powerCount.get(power) - 1);
//	            
//	            System.out.println(requiredPower);
//
//	            // Check if required power exists in the map and has sufficient count
//	            if (requiredPower == (int) requiredPower && 
//	                powerCount.getOrDefault((int) requiredPower, 0) > 0) {
//	                kings.add(power);  // Add to kings list if condition is satisfied
//	            }
//
//	            // Restore the count of the current power
//	            powerCount.put(power, powerCount.get(power) + 1);
//	        }
//
//	        return kings;
//	    }
//
//	    public static void main(String[] args) {
//	        int[] powers = {1,2,3,4};
//
//	        List<Integer> kings = findKings(powers);
//	        System.out.println("Kings: " + kings);
//	    }
	}


//	int parent[]; 
//	int rank[];
//	
//	public Debugging(int size) {
//		parent = new int[size];
//		rank = new int[size];
//		Arrays.fill(parent, -1);
//        Arrays.fill(rank, 1); // Initialize rank to 1 for each element
//	}
//	
//	public int find(int x) {
//		while(parent[x]>=0)
//			x = parent[x];
//		return x;
//	}
//	
//	public void union(int x, int y) {
//        int rootX = find(x);
//        int rootY = find(y);
//
//        if (rootX != rootY) {
//            parent[rootY] = rootX; // Attach rootY under rootX
//        }
//    }
//	
//    public int findCompression(int x) {
//    	if(parent[x]<0)
//    		return x;
////    	Path compression
//    	parent[x] = findCompression(parent[x]);
//    	return parent[x];
//    }
//
//    
//    public void unionCompression(int x, int y) {
//        int rootX = find(x);
//        int rootY = find(y);
//
//        if (rootX != rootY) {
//            // Union by rank
//            if (rank[rootX] < rank[rootY]) {
//                parent[rootX] = rootY;
//            } else if (rank[rootX] > rank[rootY]) {
//                parent[rootY] = rootX;
//            } else {
//                parent[rootY] = rootX;
//                rank[rootX]++;
//            }
//        }
//    }
//	
//	public boolean isConnected(int x, int y) {
////		return find(x)==find(y);
//		return findCompression(x)==findCompression(y);
//	}
//	
//	class Graph {
//        private int vertices;
//        private int edges;
//        private int[][] edgeList;
//
//        public Graph(int vertices, int edges, int[][] edgeList) {
//            this.vertices = vertices;
//            this.edges = edges;
//            this.edgeList = edgeList;
//        }
//
//        public boolean hasCycle() {
//            for (int i = 0; i < edges; i++) {
//                int u = edgeList[i][0];
//                int v = edgeList[i][1];
//
//                if (isConnected(u, v)) {
//                    // If the two vertices are already connected, there is a cycle
//                    return true;
//                }
//                union(u, v);
//            }
//            return false;
//        }
//    }
//	
//	public static void main(String[] args) {
//        int vertices = 4;
//        int edges = 4;
//        int[][] edgeList = {
//                {0, 1},
//                {1, 2},
//                {2, 3},
//                {3, 0},
//        };
//
//        Debugging setUnionFind = new Debugging(vertices);
//        Debugging.Graph graph = setUnionFind.new Graph(vertices, edges, edgeList);
//
//        if (graph.hasCycle()) {
//            System.out.println("The graph has a cycle.");
//        } else {
//            System.out.println("The graph does not have a cycle.");
//        }
//    }
//}
