package Graph;

import java.util.Arrays;

public class SetUnionFind {

    int parent[];
    int rank[];

    public SetUnionFind(int size) {
        parent = new int[size];
        rank = new int[size];
        Arrays.fill(parent, -1);
        Arrays.fill(rank, 1);
    }

    public int find(int x) {
        while (parent[x] >= 0) {
            x = parent[x];
        }
        return x;  // initial values of -1 return number itself hence == is false
    }
    
    public int findCompression(int x) {
    	if(parent[x]<0)
    		return x;
//    	Path compression
    	parent[x] = findCompression(parent[x]);
    	return parent[x];
    }

    
    public void unionCompression(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            parent[rootY] = rootX; // Attach rootY under rootX
        }
    }
    
    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            parent[rootY] = rootX; // Attach rootY under rootX
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

        SetUnionFind setUnionFind = new SetUnionFind(vertices);
        SetUnionFind.Graph graph = setUnionFind.new Graph(vertices, edges, edgeList);

        if (graph.hasCycle()) {
            System.out.println("The graph has a cycle.");
        } else {
            System.out.println("The graph does not have a cycle.");
        }
    }
}
