package Graph;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import Graph.breadFirstTraversal.Edge;
import java.util.*;

public class TopologicalSortBFS {

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
//	         graph[v2].add(new Edge(v2, v1));  Notice this carefully only directed graph
	      }
	      
	      int src = Integer.parseInt(br.readLine());
	      
	      boolean visited[] = new boolean[vtces];
	      Queue<Integer> q = new LinkedList<>();
	      int incoming[] = new int[vtces];
	      
	      
	      for(int i=0; i<vtces; i++) {
	    	  for(Edge e : graph[i]) {
	    		  incoming[e.nbr]++;
	    	  }
	      }
	      
	      
	      for(int i=0; i<vtces; i++) {
	    	  if(incoming[i]==0)
	    		  q.add(i);
	      }
        int[] order = new int[vtces];
        int idx = 0;
	      
	      while(!q.isEmpty()) {
	    	  int pop = q.remove();
	    	  
	    	  order[idx++] = pop;
	    	  
	    	  for(Edge e : graph[pop]) {
	    		  incoming[e.nbr]--;
	    		  
	    		  if(incoming[e.nbr]==0)
	    			  q.add(e.nbr);
	    	  }
	    	  
	      }
	      
	      for(int i : order)
	    	  System.out.println(i);
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
