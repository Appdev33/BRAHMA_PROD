package DP;

import java.util.Arrays;

public class EggDropping {

	static int memo[][];
	public static void main(String[] args) {
		
		int n = 2, k = 10;
		
		System.out.println(EggDroppingRecurse(n,k));
		
		memo = new int[n+1][k+1];
		for(int i[] : memo)
		Arrays.fill(i, -1);
		
		System.out.println(EggDroppingMemo(n,k));
	}

	private static int EggDroppingMemo(int e, int f) {
		
		if(f==0 || f==1 )
			return memo[e][f] =f;
		
		if(e==1)
			return memo[e][f] =f;
		
		if(memo[e][f]!=-1)
			return memo[e][f];
		
		int min = Integer.MAX_VALUE;
		
		for(int k=1; k<=f; k++) {
			
			int temp = 1+ Math.max(EggDroppingMemo(e-1,k-1), EggDroppingMemo(e,f-k));
			
			min = Math.min(temp, min);
		}
		
		return memo[e][f] = min;
	}

	private static int EggDroppingRecurse(int e, int f) {
	
		if(f==0 || f==1 )
			return f;
		
		if(e==1)
			return f;
		
		int min = Integer.MAX_VALUE;
		
		for(int k=1; k<=f; k++) {
			
			int temp = 1+ Math.max(EggDroppingRecurse(e-1,k-1), EggDroppingRecurse(e,f-k));
			
			min = Math.min(temp, min);
		}
		
		return min;
	}
	
	
	private static int EggDroppingBottomUp(int e, int f) {
	    // Create a 2D table to store results of subproblems
	    int[][] dp = new int[e + 1][f + 1];

	    // Initialize the table for base cases
	    for (int i = 1; i <= e; i++) {
	        dp[i][0] = 0;   // Zero trials for zero floors
	        dp[i][1] = 1;   // One trial for one floor
	    }

	    for (int j = 1; j <= f; j++) {
	        dp[1][j] = j;   // One egg, j trials for j floors
	    }

	    // Fill the rest of the table using bottom-up approach
	    for (int i = 2; i <= e; i++) {
	        for (int j = 2; j <= f; j++) {
	            dp[i][j] = Integer.MAX_VALUE;

	            for (int k = 1; k <= j; k++) {
	                int temp = 1 + Math.max(dp[i - 1][k - 1], dp[i][j - k]);
	                dp[i][j] = Math.min(dp[i][j], temp);
	            }
	        }
	    }

	    // The bottom-right cell contains the result
	    return dp[e][f];
	}


}
