package Graph;

import java.util.Arrays;

class BellmanFord {

    static class Edge {
        int source, destination, weight;

        public Edge(int source, int destination, int weight) {
            this.source = source;
            this.destination = destination;
            this.weight = weight;
        }
    }

    static int INF = Integer.MAX_VALUE;

    static void bellmanFord(int vertices, int edges, Edge[] graph, int source) {
        int[] distance = new int[vertices];
        Arrays.fill(distance, INF);
        distance[source] = 0;
        
        // do v-1 iterations for each ege provided by user and o relaxation at i th iteration all i distance path resolved
        // Relax edges repeatedly
        for (int i = 0; i < vertices - 1; ++i) {
            for (int j = 0; j < edges; ++j) {
                int u = graph[j].source;
                int v = graph[j].destination;
                int w = graph[j].weight;

                if (distance[u] != INF && distance[u] + w < distance[v]) {
                    distance[v] = distance[u] + w;
                }
            }
        }

        // Check for negative weight cycles
        for (int j = 0; j < edges; ++j) {
            int u = graph[j].source;
            int v = graph[j].destination;
            int w = graph[j].weight;
            
            // If even after relaxation and travelling through edges we find an edge where distance[u] + w < distance[v] then negative edge cycle becauase we tried relaxing all
            if (distance[u] != INF && distance[u] + w < distance[v]) {
                System.out.println("Graph contains negative weight cycle!");
                return;
            }
        }
        
        // Disconnected graph also you can check if after relaxation any vertex still has infinite path
        
        
        // Print the distances
        System.out.println("Shortest distances from source " + source + ":");
        for (int i = 0; i < vertices; ++i) {
            System.out.println("Vertex " + i + ": " + distance[i]);
        }
    }

    public static void main(String[] args) {
        int vertices = 5;
        int edges = 8;
        Edge[] graph = new Edge[edges];

        graph[0] = new Edge(0, 1, -1);
        graph[1] = new Edge(0, 2, 4);
        graph[2] = new Edge(1, 2, 3);
        graph[3] = new Edge(1, 3, 2);
        graph[4] = new Edge(1, 4, 2);
        graph[5] = new Edge(3, 2, 5);
        graph[6] = new Edge(3, 1, 1);
        graph[7] = new Edge(4, 3, -3);

        int source = 0;
        bellmanFord(vertices, edges, graph, source);
    }
}
