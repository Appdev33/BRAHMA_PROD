import java.util.*;

public class CodingTest {

    static class Pair {
        int src;
        int wt;

        Pair(int src, int wt) {
            this.src = src;
            this.wt = wt;
        }
    }

    public static void main(String[] args) {
        int n = 6;
        Map<Integer, List<int[]>> graph = new HashMap<>();

        // Initialize adjacency list
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }

        // Add edges
        graph.get(0).add(new int[]{1, 4});
        graph.get(0).add(new int[]{2, 2});
        graph.get(1).add(new int[]{2, 5});
        graph.get(1).add(new int[]{3, 10});
        graph.get(2).add(new int[]{4, 3});
        graph.get(4).add(new int[]{3, 4});
        graph.get(3).add(new int[]{5, 11});

        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);

        PriorityQueue<Pair> minheap = new PriorityQueue<>((a, b) -> a.wt - b.wt);

        int src = 0;
        distance[src] = 0;
        minheap.add(new Pair(src, 0));

        while (!minheap.isEmpty()) {
            Pair current = minheap.poll();
            int u = current.src;
            int w = current.wt;

            if (w > distance[u]) 
            		continue; // Already visited with shorter path

            for (int[] neigh : graph.getOrDefault(u, new ArrayList<>())) {
                int v = neigh[0];
                int wt = neigh[1];

                if (distance[u] + wt < distance[v]) {
                    distance[v] = distance[u] + wt;
                    minheap.add(new Pair(v, distance[v]));
                }
            }
        }

        // Print distances
        System.out.println("Shortest distances from source " + src + ": " + Arrays.toString(distance));
    }
}
