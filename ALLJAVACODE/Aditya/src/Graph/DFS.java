package Graph;

import java.util.*;

public class DFS {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int n = 4;
		int edges[][] = {{0,1},{0,2},{1,2},{2,0},{2,3},{3,3}};
		
		Map<Integer,List<Integer>> graph = new HashMap();
        boolean[] visited = new boolean[n];
        
        for(int i = 0 ; i < n ; i++) graph.put(i, new ArrayList());
         //construct graph, add bidirectional vertex
        
        for(int edge[] : edges){
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        int start =1;
        int end = 3;
 
        System.out.println( dfs(graph,visited,start,end));
    }
    
    private static boolean dfs(Map<Integer,List<Integer>> graph,boolean[] visited, int start, int end){
        
        if(start == end){
            return true;
        }
        visited[start] = true;
        
        for(int nei: graph.get(start)){
            
            if(!visited[nei]){
              boolean hasPath =  dfs(graph,visited,nei,end); 
              if(hasPath == true)
                  return  true;
            }
        }
        return false;
    }

}
