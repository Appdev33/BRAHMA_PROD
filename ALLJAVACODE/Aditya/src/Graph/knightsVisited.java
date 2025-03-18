package Graph;

import java.util.Arrays;
import java.util.Scanner;

public class knightsVisited {
	
		static int xMove[] = { 2, 1, -1, -2, -2, -1, 1, 2 }; 
	    static int yMove[] = { 1, 2, 2, 1, -1, -2, -2, -1 }; 
	    static int[][] chess;
	    
		 public static void main(String[] args) throws Exception {
		        Scanner sc =  new Scanner(System.in);
		        int n =sc.nextInt();
		        int r = sc.nextInt();
		        int c = sc.nextInt();
//		        System.out.println(r + "" +c);
		        chess = new int[n][n]; 
		        
//		        for(int i[] : chess)
//		        	Arrays.fill(i, -1);
//		        displayBoard(chess);
		        
		   
		        printKnightsTour(chess,r,c,1);
//		        System.out.println("hello");
		    }

	    public static void printKnightsTour(int[][] chess, int r, int c, int upcomingMove) {
//	    	System.out.println("bye");
	    	if(r<0 || c<0 || r>= chess.length || c>=chess[0].length || chess[r][c]>0)
	    		return ;
	    	else if(upcomingMove == chess.length*chess.length) {
	    		chess[r][c] =upcomingMove;
	    		displayBoard(chess);
	    		chess[r][c] = 0;
	    		return ;
	    	}
	    	

	    	chess[r][c] = upcomingMove;

	    	printKnightsTour(chess,r-2,c+1,upcomingMove+1);
	    	printKnightsTour(chess,r-1,c+2,upcomingMove+1);
	    	printKnightsTour(chess,r+1,c+2,upcomingMove+1);
	    	printKnightsTour(chess,r+2,c+1,upcomingMove+1);
	    	printKnightsTour(chess,r+2,c-1,upcomingMove+1);
	    	printKnightsTour(chess,r+1,c-2,upcomingMove+1);
	    	printKnightsTour(chess,r-1,c-2,upcomingMove+1);
	    	printKnightsTour(chess,r-2,c-1,upcomingMove+1);
	    	chess[r][c] = 0;

	    }

	    public static void displayBoard(int[][] chess){
//	    	System.out.println("byeD");
	        for(int i = 0; i < chess.length; i++){
	            for(int j = 0; j < chess[0].length; j++){
	                System.out.print(chess[i][j] + " ");
	            }
	            System.out.println();
	        }
	        System.out.println();
	        
//	        System.out.println("**************");
	    }

}
