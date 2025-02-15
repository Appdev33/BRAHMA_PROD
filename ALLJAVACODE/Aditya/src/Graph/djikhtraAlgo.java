package Graph;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.*;

public class djikhtraAlgo {

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

	   static class Pair{
	       int node;
	       int wt;
	       
	       Pair(int node, int wt){
	           this.node = node;
	           this.wt = wt;
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
	         int wt = Integer.parseInt(parts[2]);
	         
	         graph[v1].add(new Edge(v1, v2, wt));
	         graph[v2].add(new Edge(v2, v1, wt));
	      }
	      
	      int src = Integer.parseInt(br.readLine());
	      // write your code here  
	      PriorityQueue<Pair> q = new PriorityQueue<>((a,b) -> a.wt-b.wt);
	      boolean[] vis = new boolean[vtces];
	      
	      q.add(new Pair(src,0));
	      while(q.size() > 0){ 
	          // remove
	          Pair curr = q.poll();
	          
	          if(vis[curr.node] == true) 
	        	  continue;
	          
	          // mark*
	          vis[curr.node] = true;
	          
	          // work
	          
	          System.out.println(curr.node + "--->" + curr.wt );
	          
	          // add*
	          for(Edge e: graph[curr.node]){
	              if(vis[e.nbr] == false){
	                  q.add(new Pair(e.nbr, curr.wt + e.wt));
	              }
	          }
	      }
	   }

}


/*
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

