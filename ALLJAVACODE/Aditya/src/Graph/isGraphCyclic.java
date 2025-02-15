package Graph;
import java.io.*;
import java.util.*;

public class isGraphCyclic {
	
	public static class Pair {
        int src;
        int par;

        Pair(int src, int par) {
            this.src = src;
            this.par = par;
        }
    }

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

	      // write your code here
	      boolean res= false;
	      boolean visited[] = new boolean[vtces];
	      for(int i=0; i<vtces; i++) {
	    	  if(visited[i]==false) {
	    		  res = BFS(i, graph, visited) ;
	    		  if(res)
	    			  break;	
	    	  }
	      }
	    	  
	      System.out.println(res);
	      
	   }



	private static boolean BFS(int src, ArrayList<Edge>[] adj, boolean[] vis) {
		
		Queue<Pair> q = new LinkedList<>();
		q.add(new Pair(src,-1));
		
		while(!q.isEmpty()) {
			
			Pair poll = q.poll();
			src = poll.src;
			int par = poll.par;
			
			if(vis[src]==true)
				return true;
			vis[src] = true;
			
			for(Edge nbr : adj[src]) {
				if(vis[nbr.nbr]==false)
					q.add(new Pair(nbr.nbr, src));
			}
		}
		
		return false;
	}
}
/*
7
6
0 1 10
1 2 10
2 3 10
3 4 10
4 5 10
5 6 10
*/
