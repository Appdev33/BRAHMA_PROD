package Graph;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;

public class BFS01 {

    static class Edge {
        int to, weight;

        public Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    public static int[] zeroOneBFS(ArrayList<ArrayList<Edge>> graph, int start) {
        int n = graph.size();
        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);

        // Using a deque for 0-1 BFS
        Deque<Integer> deque = new ArrayDeque<>();

        // Initialize distance for the starting vertex
        distance[start] = 0;
        deque.addFirst(start);

        while (!deque.isEmpty()) {
            int node = deque.pollFirst();

            for (Edge neighbor : graph.get(node)) {
                int to = neighbor.to;
                int weight = neighbor.weight;

                // Relaxation step
                if (distance[node] + weight < distance[to]) {
                    distance[to] = distance[node] + weight;

                    // If weight is 0, insert at the front; else, insert at the back
                    if (weight == 0) {
                        deque.addFirst(to);
                    } else {
                        deque.addLast(to);
                    }
                }
            }
        }

        return distance;
    }

    public static void main(String[] args) {
        int n = 6; // Number of vertices
        ArrayList<ArrayList<Edge>> graph = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        // Adding edges to the graph
        graph.get(0).add(new Edge(1, 0));
        graph.get(0).add(new Edge(2, 1));
        graph.get(1).add(new Edge(3, 1));
        graph.get(1).add(new Edge(4, 0));
        graph.get(2).add(new Edge(4, 1));
        graph.get(3).add(new Edge(5, 1));
        graph.get(4).add(new Edge(5, 0));

        int startNode = 0;
        int[] distances = zeroOneBFS(graph, startNode);

        System.out.println("Shortest distances from node " + startNode + ": " + Arrays.toString(distances));
    }
}
