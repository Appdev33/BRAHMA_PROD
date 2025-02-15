package Graph;

import java.io.*;
import java.util.*;


/*
7
5
0 1 10
2 3 10
4 5 10
5 6 10
4 6 10
 */
public class connectedComponents {
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
    
  // DFS on 1 component will take O(n + e) Time where n = vertices in that component, and e = edges in that component.
  // Hence, getting all connected components will take O(N + E) time where N = total vertices, E = total edges
  
   public static void dfs(ArrayList<Edge>[] graph, int src, ArrayList<Integer> comp, boolean[] vis){
        vis[src] = true;
        comp.add(src);
        
        for(Edge e: graph[src]){
            if(vis[e.nbr] == false){
                dfs(graph, e.nbr, comp, vis);
            }
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

      ArrayList<ArrayList<Integer>> comps = new ArrayList<>();
      boolean[] vis = new boolean[vtces];
      
      for(int i=0; i<vtces; i++){
          if(vis[i] == false){
              ArrayList<Integer> comp = new ArrayList<>();
              dfs(graph, i, comp, vis);
              comps.add(comp);
          }
      }
      
      System.out.println(comps);
   }
}