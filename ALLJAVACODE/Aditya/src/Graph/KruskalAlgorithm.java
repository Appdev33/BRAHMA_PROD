package Graph;

import java.util.Arrays;

public class KruskalAlgorithm {

    static class Edge implements Comparable<Edge> {
        int src, dest, weight;

        public Edge(int src, int dest, int weight) {
            this.src = src;
            this.dest = dest;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge compareEdge) {
            return this.weight - compareEdge.weight;
        }
    }

    static class SetUnionFind {
        int parent[];
        int rank[];

        public SetUnionFind(int size) {
            parent = new int[size];
            rank = new int[size];
            Arrays.fill(parent, -1);
            Arrays.fill(rank, 1); // Initialize rank to 1 for each element
        }

        public int find(int x) {
            if (parent[x] < 0) {
                return x;
            }
            // Path compression
            parent[x] = find(parent[x]);
            return parent[x];
        }

        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);

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

        public boolean isConnected(int x, int y) {
            return find(x) == find(y);
        }
    }

    static class Graph {
        int vertices, edges;
        Edge edgeList[];

        public Graph(int vertices, int edges) {
            this.vertices = vertices;
            this.edges = edges;
            edgeList = new Edge[edges];
            for (int i = 0; i < edges; ++i) {
                edgeList[i] = new Edge(0, 0, 0);
            }
        }

        public void addEdge(int index, int src, int dest, int weight) {
            edgeList[index].src = src;
            edgeList[index].dest = dest;
            edgeList[index].weight = weight;
        }

        public void kruskalMST() {
            Arrays.sort(edgeList);

            SetUnionFind dsu = new SetUnionFind(vertices);

            for (int i = 0, e = 0; e < vertices - 1 && i < edges; ++i) {
                int src = edgeList[i].src;
                int dest = edgeList[i].dest;

                if (!dsu.isConnected(src, dest)) {
                    dsu.union(src, dest);
                    System.out.println("Edge added: " + src + " - " + dest);
                    e++;
                }
            }
        }
    }

    public static void main(String[] args) {
        int vertices = 4;
        int edges = 5;

        Graph graph = new Graph(vertices, edges);

        graph.addEdge(0, 0, 1, 10);
        graph.addEdge(1, 0, 2, 6);
        graph.addEdge(2, 0, 3, 5);
        graph.addEdge(3, 1, 3, 15);
        graph.addEdge(4, 2, 3, 4);

        graph.kruskalMST();
    }
}





//
//
//
//package Graph;
//
//import java.util.Arrays;
//
//public class KruskalAlgorithm {
//
//    static class Edge implements Comparable<Edge> {
//        int src, dest, weight;
//
//        public Edge(int src, int dest, int weight) {
//            this.src = src;
//            this.dest = dest;
//            this.weight = weight;
//        }
//
//        @Override
//        public int compareTo(Edge compareEdge) {
//            return this.weight - compareEdge.weight;
//        }
//    }
//
//    static class SetUnionFind {
//        int parent[];
//        int rank[];
//
//        public SetUnionFind(int size) {
//            parent = new int[size];
//            rank = new int[size];
//            Arrays.fill(parent, -1);
//            Arrays.fill(rank, 1); // Initialize rank to 1 for each element
//        }
//
//        public int find(int x) {
//            if (parent[x] < 0) {
//                return x;
//            }
//            // Path compression
//            parent[x] = find(parent[x]);
//            return parent[x];
//        }
//
//        public void union(int x, int y) {
//            int rootX = find(x);
//            int rootY = find(y);
//
//            if (rootX != rootY) {
//                // Union by rank
//                if (rank[rootX] < rank[rootY]) {
//                    parent[rootX] = rootY;
//                } else if (rank[rootX] > rank[rootY]) {
//                    parent[rootY] = rootX;
//                } else {
//                    parent[rootY] = rootX;
//                    rank[rootX]++;
//                }
//            }
//        }
//
//        public boolean isConnected(int x, int y) {
//            return find(x) == find(y);
//        }
//    }
//
//    static class Graph {
//        int vertices, edges;
//        Edge edgeList[];
//
//        public Graph(int vertices, int edges) {
//            this.vertices = vertices;
//            this.edges = edges;
//            edgeList = new Edge[edges];
//            for (int i = 0; i < edges; ++i) {
//                edgeList[i] = new Edge(0, 0, 0);
//            }
//        }
//
//        public void addEdge(int index, int src, int dest, int weight) {
//            edgeList[index].src = src;
//            edgeList[index].dest = dest;
//            edgeList[index].weight = weight;
//        }
//
//        public int kruskalMST() {
//            Arrays.sort(edgeList);
//
//            SetUnionFind dsu = new SetUnionFind(vertices);
//            int minWeight = 0;
//
//            for (int i = 0, e = 0; e < vertices - 1 && i < edges; ++i) {
//                int src = edgeList[i].src;
//                int dest = edgeList[i].dest;
//
//                if (!dsu.isConnected(src, dest)) {
//                    dsu.union(src, dest);
//                    minWeight += edgeList[i].weight;
//                    e++;
//                }
//            }
//
//            return minWeight;
//        }
//    }
//
//    public static void main(String[] args) {
//        int vertices = 4;
//        int edges = 5;
//
//        Graph graph = new Graph(vertices, edges);
//
//        graph.addEdge(0, 0, 1, 10);
//        graph.addEdge(1, 0, 2, 6);
//        graph.addEdge(2, 0, 3, 5);
//        graph.addEdge(3, 1, 3, 15);
//        graph.addEdge(4, 2, 3, 4);
//
//        int minWeight = graph.kruskalMST();
//        System.out.println("Minimum Weight of Minimum Spanning Tree: " + minWeight);
//    }
//}
//
