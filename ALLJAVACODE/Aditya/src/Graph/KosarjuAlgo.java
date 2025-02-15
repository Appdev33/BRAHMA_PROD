package Graph;


//Certainly! Kosaraju's algorithm can be broken down into three main steps:
//
//Perform DFS on the original graph and push vertices onto a stack in the order of their finishing times.
//Transpose the graph (reverse all edges).
//Perform DFS on the transposed graph while popping vertices from the stack and output the strongly connected components.
import java.util.*;

import java.util.*;

class KosarjuAlgo {
    private int V;
    private List<Integer>[] adj;

    public KosarjuAlgo(int v) {
        V = v;
        adj = new ArrayList[V];
        for (int i = 0; i < V; i++) {
            adj[i] = new ArrayList<>();
        }
    }

    public void addEdge(int v, int w) {
        adj[v].add(w);
    }

    public List<List<Integer>> getSCCs() {
        Stack<Integer> stack = new Stack<>();
        boolean[] visited = new boolean[V];

        // Step 1: Perform DFS and fill the stack
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                fillOrder(i, visited, stack);
            }
        }

        // Step 2: Transpose the graph
        KosarjuAlgo transposedGraph = getTranspose();

        // Step 3: Perform DFS on transposed graph and output SCCs
        Arrays.fill(visited, false);
        List<List<Integer>> sccList = new ArrayList<>();
        int sccCount = 0;

        while (!stack.isEmpty()) {
            int v = stack.pop();

            if (!visited[v]) {
                List<Integer> scc = new ArrayList<>();
                transposedGraph.DFSUtil(v, visited, scc);
                sccList.add(scc);
                sccCount++;
            }
        }

        System.out.println("Number of Strongly Connected Components: " + sccCount);
        return sccList;
    }

    private void fillOrder(int v, boolean[] visited, Stack<Integer> stack) {
        visited[v] = true;
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                fillOrder(neighbor, visited, stack);
            }
        }
        stack.push(v);
    }

    private KosarjuAlgo getTranspose() {
        KosarjuAlgo transpose = new KosarjuAlgo(V);
        for (int v = 0; v < V; v++) {
            for (int neighbor : adj[v]) {
                transpose.addEdge(neighbor, v);
            }
        }
        return transpose;
    }

    private void DFSUtil(int v, boolean[] visited, List<Integer> scc) {
        visited[v] = true;
        scc.add(v);
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                DFSUtil(neighbor, visited, scc);
            }
        }
    }

    public static void main(String[] args) {
        KosarjuAlgo g = new KosarjuAlgo(5);
        g.addEdge(0, 1);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(1, 3);
        g.addEdge(3, 4);

        List<List<Integer>> sccList = g.getSCCs();

        System.out.println("Strongly Connected Components:");
        for (List<Integer> scc : sccList) {
            System.out.println(scc);
        }
    }
}
