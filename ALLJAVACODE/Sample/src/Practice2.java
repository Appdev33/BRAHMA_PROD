import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Practice2 {
	static int index = 0;
	
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

	   static class Pair{         //New node for prims krushkal
	       int node;
	       int wt;
	       
	       Pair(int node, int wt){
	           this.node = node;
	           this.wt = wt;
	       }
	   }
	  
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	      int vtces = Integer.parseInt(br.readLine());
	      ArrayList<Edge>[] graph = new ArrayList[vtces];
	      for (int i = 0; i < vtces; i++) {
	         graph[i] = new ArrayList<>();
	      }
	      ArrayList<Edge>[] graphD = new ArrayList[vtces];
	      for (int i = 0; i < vtces; i++) {
	         graphD[i] = new ArrayList<>();
	      }

	      int edges = Integer.parseInt(br.readLine());
	      int indegree[] = new int[vtces];
	      
	      for (int i = 0; i < edges; i++) {
	         String[] parts = br.readLine().split(" ");
	         int v1 = Integer.parseInt(parts[0]);
	         int v2 = Integer.parseInt(parts[1]);
	         int wt = Integer.parseInt(parts[2]);
	         
	         graph[v1].add(new Edge(v1, v2, wt));
	         graph[v2].add(new Edge(v2, v1, wt));
	         
	         graphD[v1].add(new Edge(v1, v2, wt));
	         ++indegree[v2];
	      }
	      
	      int src = Integer.parseInt(br.readLine());
//	      DjikhstraAlgo(src, graph);
//	      System.out.println(PrimsAlgo(src,graph,0));


	      
	  	  boolean visited[] = new boolean[vtces];
	      Stack<Integer> stack = new Stack<>();
	      for(int v=0; v<vtces; v++) {
	    	  if(visited[v]==false)
	    	  TopoSortDfs(v,graphD, stack,visited);
	      }
	      
	      System.out.println("size" +stack.size());
	      while(stack.size()>0)
	    	  System.out.println(stack.pop());
     
	      System.out.println("***********************************");
	   
	      Queue<Integer> queue = new LinkedList<>();
	      for(int i=0; i<vtces; i++) {
	    	  if(indegree[i]==0)
	    		  queue.add(i);
	      }

	      int order[] = new int[graphD.length];
	      TopoSortBfs(src,graphD,queue,order,indegree);
	      for(int i: order)
	    	  System.out.println(i);
	      
	}

	private static void TopoSortBfs(int src, ArrayList<Edge>[] graphD, Queue<Integer> queue, int[] order, int[] indegree) {
		
		while(!queue.isEmpty()) {
			int pop = queue.poll();
			
			order[index++]= pop;
			
			for(Edge e: graphD[pop]) {
				--indegree[e.nbr];
				
	    		  if(indegree[e.nbr]==0)
	    			  queue.add(e.nbr);
	    	  }
			}
	}

	private static void TopoSortDfs(int src, ArrayList<Edge>[] graphD, Stack<Integer> stack, boolean[] visited) {
		// TODO Auto-generated method stub
		visited[src] = true;
		
		for(Edge e: graphD[src]) {
			if(visited[e.nbr]==false)
				TopoSortDfs(e.nbr,graphD, stack,visited);
		}
		stack.push(src);
	}

	private static int PrimsAlgo(int src, ArrayList<Edge>[] graph, int MSTCost) {
		PriorityQueue<Pair> pq = new PriorityQueue<>((a,b) -> a.wt-b.wt);
		boolean visited[] = new boolean[graph.length];
		
		pq.add(new Pair(src,0));
		while(!pq.isEmpty()) {
			
			Pair poll = pq.poll();
			
			if(visited[poll.node])
				continue;
			visited[poll.node] = true;
			
			System.out.println(poll.node + "--->" + poll.wt );
			MSTCost+=poll.wt;
			System.out.println(MSTCost);
			
			for(Edge e: graph[poll.node]) {
				if(!visited[e.nbr]) {
					pq.add(new Pair(e.nbr,  e.wt));
				}
			}
		}
		return MSTCost;
	}

	private static void DjikhstraAlgo(int src, ArrayList<Edge>[] graph) {
		
		PriorityQueue<Pair> pq = new PriorityQueue<>((a,b) -> a.wt-b.wt);
		boolean visited[] = new boolean[graph.length];
		
		pq.add(new Pair(src,0));
		while(!pq.isEmpty()) {
			
			Pair poll = pq.poll();
			
			if(visited[poll.node])
				continue;
			visited[poll.node] = true;
			System.out.println(poll.node + "--->" + poll.wt );
			
			for(Edge e: graph[poll.node]) {
				if(!visited[e.nbr]) {
					pq.add(new Pair(e.nbr, poll.wt + e.wt));
				}
			}
		}
		
	}


    private static void Union() {}
    
    private static void Find() {}

}
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
