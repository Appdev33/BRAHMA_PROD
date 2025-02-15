package Graph;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import Graph.breadFirstTraversal.Edge;
import java.util.*;

public class TopologicalSortDFS {

	static class Edge {
	      int src;
	      int nbr;

	      Edge(int src, int nbr) {
	         this.src = src;
	         this.nbr = nbr;
	      }
	   }
	
	   static class Pair{
	       int node;
	       String pathSofar;
	       
	       Pair(int node, String pathSofar){
	           this.node = node;
	           this.pathSofar = pathSofar;
	       }
	   }
	   
	   public static void main(String[] args) throws Exception {
	      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	      int vtces = Integer.parseInt(br.readLine());
	      ArrayList<Edge>[] graph = new ArrayList[vtces];
	      for (int i = 0; i < vtces; i++) {
	         graph[i] = new ArrayList<>();
	      }

	      int edges = Integer.parseInt(br.readLine());
	      for (int i = 0; i < edges; i++) {
	         String[] parts = br.readLine().split(" ");
	         int v1 = Integer.parseInt(parts[0]);
	         int v2 = Integer.parseInt(parts[1]);
	         graph[v1].add(new Edge(v1, v2));
//	         graph[v2].add(new Edge(v2, v1)); Notice this carefully only directed graph
	      }
	      
	      int src = Integer.parseInt(br.readLine());
	      
	      boolean visited[] = new boolean[vtces];
	      Stack<Integer> st = new Stack<>();
	      for(int v=0; v<vtces; v++) {
	    	  if(visited[v]==false)
	    		  topologicalSort(graph,v,visited,st);
	      }
	      
	     System.out.println(st.size());
	      while(st.size()>0)
	    	  System.out.println(st.pop());
	   }
	   
		private static void topologicalSort(ArrayList<Edge>[] graph, int src, boolean[] visited, Stack<Integer> st) {
			// TODO Auto-generated method stub
			visited[src] = true;
			for(Edge e : graph[src]) {
				if(visited[e.nbr]==false)
					topologicalSort(graph,e.nbr,visited,st);
			}
			st.push(src);
		}
}


/*
6
6
5 2 1
5 0 1
4 0 1
4 1 1
2 3 1
3 1 1
2
*/
