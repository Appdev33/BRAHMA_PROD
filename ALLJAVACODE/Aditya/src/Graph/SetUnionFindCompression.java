package Graph;

import java.util.Arrays;

public class SetUnionFindCompression {

    int parent[];
    int rank[];

    public SetUnionFindCompression(int size) {
        parent = new int[size];
        rank = new int[size];
        Arrays.fill(parent, -1);
        Arrays.fill(rank, 1); // Initialize rank to 1 for each element
    }
    

//In your code, you're initializing the rank array elements to 0, which is not standard for the union-find data structure. 
//Typically, when using the union-by-rank optimization, you initialize the rank of each element to 1, not 0.
//This is because the rank represents the height (or depth) of the tree, and in the beginning, 
//each element is considered as a tree with only one node, so its rank is 1.

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

    class Graph {
        private int vertices;
        private int edges;
        private int[][] edgeList;

        public Graph(int vertices, int edges, int[][] edgeList) {
            this.vertices = vertices;
            this.edges = edges;
            this.edgeList = edgeList;
        }

        public boolean hasCycle() {
            for (int i = 0; i < edges; i++) {
                int u = edgeList[i][0];
                int v = edgeList[i][1];

                if (isConnected(u, v)) {
                    // If the two vertices are already connected, there is a cycle
                    return true;
                }
                union(u, v);
            }
            return false;
        }
    }

    public static void main(String[] args) {
        int vertices = 4;
        int edges = 4;
        int[][] edgeList = {
                {0, 1},
                {1, 2},
                {2, 3},
                {3, 0}
        };

        SetUnionFindCompression setUnionFind = new SetUnionFindCompression(vertices);
        SetUnionFindCompression.Graph graph = setUnionFind.new Graph(vertices, edges, edgeList);

        if (graph.hasCycle()) {
            System.out.println("The graph has a cycle.");
        } else {
            System.out.println("The graph does not have a cycle.");
        }
    }
}
