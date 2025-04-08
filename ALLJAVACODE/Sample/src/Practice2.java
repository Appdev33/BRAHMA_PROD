import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Practice2 {
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

    static class Pair {
        int node;
        int wt;

        Pair(int node, int wt) {
            this.node = node;
            this.wt = wt;
        }
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int vtces = Integer.parseInt(br.readLine());
        ArrayList<Edge>[] graph = new ArrayList[vtces];
        for (int i = 0; i < vtces; i++) {
            graph[i] = new ArrayList<>();
        }
        ArrayList<Edge>[] graphD = new ArrayList[vtces];
        for (int i = 0; i < vtces; i++) {
            graphD[i] = new ArrayList<>();
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

            graphD[v1].add(new Edge(v1, v2, wt));
            ++indegree[v2];
        }

        int src = Integer.parseInt(br.readLine());

        // DFS-based Topological Sort
        boolean visited[] = new boolean[vtces];
        Stack<Integer> stack = new Stack<>();
        for (int v = 0; v < vtces; v++) {
            if (!visited[v])
                TopoSortDfs(v, graphD, stack, visited);
        }

        System.out.println("********** DFS Topological Sort **********");
        while (!stack.isEmpty()) {
            System.out.println(stack.pop());
        }

        System.out.println("********** BFS (Kahn's Algorithm) **********");
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < vtces; i++) {
            if (indegree[i] == 0)
                queue.add(i);
        }

        int order[] = new int[vtces];
        TopoSortBfs(graphD, queue, order, indegree);
        for (int i : order)
            System.out.println(i);

        System.out.println("********** Dijkstra's Algorithm **********");
        DijkstraAlgo(src, graph);
    }

    private static void TopoSortBfs(ArrayList<Edge>[] graphD, Queue<Integer> queue, int[] order, int[] indegree) {
        int idx = 0;
        while (!queue.isEmpty()) {
            int pop = queue.poll();
            order[idx++] = pop;
            for (Edge e : graphD[pop]) {
                --indegree[e.nbr];
                if (indegree[e.nbr] == 0)
                    queue.add(e.nbr);
            }
        }
    }

    private static void TopoSortDfs(int src, ArrayList<Edge>[] graphD, Stack<Integer> stack, boolean[] visited) {
        visited[src] = true;
        for (Edge e : graphD[src]) {
            if (!visited[e.nbr])
                TopoSortDfs(e.nbr, graphD, stack, visited);
        }
        stack.push(src);
    }

    private static int PrimsAlgo(int src, ArrayList<Edge>[] graph, int MSTCost) {
        PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> a.wt - b.wt);
        int cost = 0;
        boolean[] taken = new boolean[graph.length];
        pq.add(new Pair(src, 0));

        while (!pq.isEmpty()) {
            Pair curr = pq.poll();
            
            if (taken[curr.node]) 
            		continue;

            taken[curr.node] = true;
            
            cost += curr.wt;
            System.out.println(curr.node + " ---> " + curr.wt);

            for (Edge e : graph[curr.node]) {
                if (!taken[e.nbr]) {
                    pq.add(new Pair(e.nbr, e.wt));
                }
            }
        }
        return cost;
    }

    private static void DijkstraAlgo(int src, ArrayList<Edge>[] graph) {
        PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> a.wt - b.wt);
        int[] dist = new int[graph.length];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;

        pq.offer(new Pair(src, 0));

        while (!pq.isEmpty()) {
            Pair current = pq.poll();
            int u = current.node;
            int w = current.wt;

            if (w > dist[u]) 
            		continue; // Lazy deletion

            for (Edge edge : graph[u]) {
                int v = edge.nbr;
                int weight = edge.wt;

                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.offer(new Pair(v, dist[v]));
                }
            }
        }

        System.out.println("\nFinal Distances from source node " + src + ":");
        for (int i = 0; i < dist.length; i++) {
            System.out.println("To node " + i + " = " + (dist[i] == Integer.MAX_VALUE ? "INF" : dist[i]));
        }
    }

}

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
