package Graph;

import java.io.*;

public class countIslands {
	
	static int[][] directions = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
    // down, up, right, left

	public static void main(String[] args) throws Exception {
	      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	      int m = Integer.parseInt(br.readLine());
	      int n = Integer.parseInt(br.readLine());
	      int[][] arr = new int[m][n];

	      for (int i = 0; i < arr.length; i++) {
	         String parts = br.readLine();
	         for (int j = 0; j < arr[0].length; j++) {
	            arr[i][j] = Integer.parseInt(parts.split(" ")[j]);
	         }
	      }

	      // write your code here
	      System.out.println(numIslands(arr));
	   }

	
    public static void DFS(int r, int c, int[][] grid) {
        // Out of Matrix, Water Cell, Visited Land
        if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length
                || grid[r][c] == 1 || grid[r][c] == -1)
            return;

        grid[r][c] = -1; // Visited Land
        for (int[] direction : directions) {
            DFS(r + direction[0], c + direction[1], grid);
        }
    }

    public static int numIslands(int[][] grid) {
        int islands = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                // Unvisited Land
                if (grid[i][j] == 0) {
                    DFS(i, j, grid);
                    islands++;
                }
            }
        }
        return islands;
    }

}
