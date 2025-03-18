package Graph;
//
//import java.io.*;
//import java.util.*;
//
//public class primsAlgorithm {
//
//	public static class Pair implements Comparable<Pair> {
//        int node;
//        int weight;
//
//        public Pair(int node, int weight) {
//            this.node = node;
//            this.weight = weight;
//        }
//
//        public int compareTo(Pair other) {
//            return (this.weight - other.weight);
//            // Min Priority Queue -> Negative for this < other
//        }
//    }
//	
//	
//
//    @SuppressWarnings("unchecked")
//    static int spanningTree(int n, ArrayList<ArrayList<ArrayList<Integer>>> g) {
//        ArrayList<Pair>[] adj = new ArrayList[n];
//        for (int i = 0; i < n; i++) {
//            adj[i] = new ArrayList<>();
//            for (ArrayList<Integer> pairs : g.get(i)) {
//                adj[i].add(new Pair(pairs.get(0), pairs.get(1)));
//            }
//        }
//
//        PriorityQueue<Pair> q = new PriorityQueue<>();
//        q.add(new Pair(0, 0));
//        boolean[] vis = new boolean[n];
//        int cost = 0;
//
//        while (q.size() > 0) {
//            Pair top = q.remove();
//            if (vis[top.node] == true)
//                continue; // CYCLE
//
//            vis[top.node] = true;
//            cost = cost + top.weight;
//
//            for (Pair nbr : adj[top.node]) {
//            	if(vis[nbr.node]==false)
//            		q.add(new Pair(nbr.node, nbr.weight));
//            }
//        }
//
//        return cost;
//    }
//    
////    public static void main(String[] args) {
////    	ArrayList<ArrayList<ArrayList<Integer>>> graph = new Arraylist<>();
////    	
////    	return spanningTree(graph);
////	}
//}
//
///*
//
//7
//8
//0 1 10
//1 2 10
//2 3 10
//0 3 10
//3 4 10
//4 5 10
//5 6 10
//4 6 10
//2
//*/


import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class primsAlgorithm {

    public static class Pair implements Comparable<Pair> {
        int node;
        int weight;

        public Pair(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }

        public int compareTo(Pair other) {
            return this.weight - other.weight;
            // Min Priority Queue -> Negative for this < other
        }
    }

    @SuppressWarnings("unchecked")
    static int spanningTree(int n, ArrayList<ArrayList<ArrayList<Integer>>> g) {
        ArrayList<Pair>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
            for (ArrayList<Integer> pairs : g.get(i)) {
                adj[i].add(new Pair(pairs.get(0), pairs.get(1)));
            }
        }

        PriorityQueue<Pair> q = new PriorityQueue<>();
        q.add(new Pair(0, 0));
        boolean[] vis = new boolean[n];
        int cost = 0;

        while (q.size() > 0) {
            Pair top = q.remove();
            if (vis[top.node])
                continue; // CYCLE

            vis[top.node] = true;
            cost = cost + top.weight;

            for (Pair nbr : adj[top.node]) {
                if (!vis[nbr.node])
                    q.add(new Pair(nbr.node, nbr.weight));
            }
        }

        return cost;
    }

    public static void main(String[] args) {
        // Input format: source destination weight
        ArrayList<ArrayList<ArrayList<Integer>>> graph = new ArrayList<>();
        for (int i = 0; i < 7; i++) {
            graph.add(new ArrayList<>());
        }

        // Adding edges to the graph
        int[][] edges = {{0, 1, 10}, {1, 2, 10}, {2, 3, 10}, {0, 3, 10}, {3, 4, 10}, {4, 5, 10}, {5, 6, 10}, {4, 6, 10}};
        for (int[] edge : edges) {
            int source = edge[0];
            int destination = edge[1];
            int weight = edge[2];
            graph.get(source).add(new ArrayList<>(List.of(destination, weight)));
            graph.get(destination).add(new ArrayList<>(List.of(source, weight)));
        }

        int numberOfNodes = 7; // Number of nodes in the graph
        int minimumCost = spanningTree(numberOfNodes, graph);

        System.out.println("Minimum Cost of Spanning Tree: " + minimumCost);
    }
}
