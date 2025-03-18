import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

//6
//A B
//C D
//E F
//B C
//G H
//I J


public class SolutionCode {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		int size = Integer.parseInt(br.readLine());
//		List<List<String>> input = new ArrayList<>();
//		List<String> temp;
//		while(size-->0) {
//			temp = new ArrayList<>();
//			String inp[] =  br.readLine().split(" ");
//			temp.add(inp[0]);
//			temp.add(inp[1]);
//			
//			input.add(new ArrayList<>(temp));
//		}
		List<List<String>> input = Arrays.asList(
			    Arrays.asList("A", "B"),
			    Arrays.asList("C", "D"),
			    Arrays.asList("B", "D"),
			    Arrays.asList("C", "E"),
			    Arrays.asList("E", "A")
			);
		
		System.out.println(input);
		int len = input.size();
		HashMap<String,Integer> indegree = new HashMap<>();
		int dp[] = new int[len+1];
		
		HashMap<String, List<String>> graph = new HashMap<>();
		HashMap<String, Integer> longestPath = new HashMap<>();
		
		for(List<String> node: input) {
			String from = node.get(0);
			String to = node.get(1);
			
			 indegree.putIfAbsent(from, 0);
			 indegree.putIfAbsent(to, 0);
			
			
			graph.computeIfAbsent(from, k->new ArrayList<>()).add(to);
			indegree.put(to, indegree.getOrDefault(to, 0)+1);
		}
		
		System.out.println(findLongestPath(graph));
		System.out.println(findLongestPathTopo(input));
	}
	
	public static int dfs(String node, Map<String, List<String>> graph, Set<String> visited, int pathLength) {
        visited.add(node);
        int maxLength = pathLength;

        // Explore all neighbors (friends that can receive the joke)
        for (String neighbor : graph.getOrDefault(node, new ArrayList<>())) {
            if (!visited.contains(neighbor)) {
                maxLength = Math.max(maxLength, dfs(neighbor, graph, visited, pathLength + 1));
            }
        }

        visited.remove(node); // Backtrack
        return maxLength;
    }

    // Function to find the longest joke path in the graph
    public static int findLongestPath(Map<String, List<String>> graph) {
        int longestPath = 0;
        Set<String> visited = new HashSet<>();

        // Run DFS from each node to find the longest path starting from that node
        for (String startNode : graph.keySet()) {
            longestPath = Math.max(longestPath, dfs(startNode, graph, visited, 0));
        }

        return longestPath;
    }
     
    
    public static int findLongestPathTopo(List<List<String>> input) {
        // Step 1: Convert input to a graph (adjacency list) and compute in-degrees
        Map<String, List<String>> graph = new HashMap<>();
        Map<String, Integer> inDegree = new HashMap<>();
        
        // Initialize graph and in-degree map
        for (List<String> edge : input) {
            String u = edge.get(0);
            String v = edge.get(1);
            
            graph.putIfAbsent(u, new ArrayList<>());
            graph.get(u).add(v);
            
            inDegree.putIfAbsent(u, 0);
            inDegree.putIfAbsent(v, 0);
            inDegree.put(v, inDegree.get(v) + 1);
        }

        // Step 2: Perform topological sort (Kahn's algorithm)
        Queue<String> queue = new LinkedList<>();
        List<String> topoOrder = new ArrayList<>();
        
        // Start with nodes that have no incoming edges (in-degree 0)
        for (String node : inDegree.keySet()) {
            if (inDegree.get(node) == 0) {
                queue.add(node);
            }
        }
        
        while (!queue.isEmpty()) {
            String node = queue.poll();
            topoOrder.add(node);
            for (String neighbor : graph.getOrDefault(node, new ArrayList<>())) {
                inDegree.put(neighbor, inDegree.get(neighbor) - 1);
                if (inDegree.get(neighbor) == 0) {
                    queue.add(neighbor);
                }
            }
        }

        // Step 3: Initialize distances and apply dynamic programming to find the longest path
        Map<String, Integer> dist = new HashMap<>();
        for (String node : topoOrder) {
            dist.put(node, Integer.MIN_VALUE); // Initialize distance as -Infinity
        }
        
        // Start the longest path calculation for all nodes in topo order
        int longestPath = 0;
        for (String node : topoOrder) {
            if (dist.get(node) == Integer.MIN_VALUE) {
                dist.put(node, 0);  // Start node has distance 0
            }
            for (String neighbor : graph.getOrDefault(node, new ArrayList<>())) {
                dist.put(neighbor, Math.max(dist.get(neighbor), dist.get(node) + 1));
            }
        }

        // Step 4: Find the longest path in the graph
        for (int length : dist.values()) {
            longestPath = Math.max(longestPath, length);
        }

        return longestPath;
    }

}
