package Graph;

import java.util.ArrayList;

public class DirectedCycle {
	
	 // Function to detect cycle in an undirected graph.
    public boolean isCycle(int V, ArrayList<ArrayList<Integer>> adj) {
        boolean[] visited = new boolean[V];
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (dfs(i, adj, visited, -1))
                    return true;
            }
        }
        return false;
    }

    public boolean dfs(int u, ArrayList<ArrayList<Integer>> adj, boolean[] visited, int parent) {
        visited[u] = true;
        for (int j : adj.get(u)) {
            if (!visited[j]) {
                if (dfs(j, adj, visited, u))
                    return true;
            } else if (parent != j) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
    	DirectedCycle solution = new DirectedCycle();
        int V = 4;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++)
            adj.add(new ArrayList<>());

        // Add edges
        adj.get(0).add(1);
        adj.get(1).add(0);

        adj.get(0).add(2);
        adj.get(2).add(0);

        adj.get(1).add(2);
        adj.get(2).add(1);

        adj.get(2).add(3);
        adj.get(3).add(2);

        boolean hasCycle = solution.isCycle(V, adj);
        if (hasCycle)
            System.out.println("Graph contains cycle");
        else
            System.out.println("Graph doesn't contain cycle");
    }


}



