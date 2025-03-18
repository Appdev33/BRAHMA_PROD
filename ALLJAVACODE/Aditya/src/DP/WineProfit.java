package DP;

import java.util.Arrays;

public class WineProfit {
	
	static int N = 1001;
	static int memo[][];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	       int price[] = {2, 4, 6, 2, 5};
	       int n = price.length;
	       int ans = maxProfitR(price, n);
	       
	       System.out.println(ans);
	}

	     
	// Function to maximize profit
	static int maxProfitUtil(int price[], int begin, int end, int year) {
		if (begin == end) {
			return price[begin] * year;
		}

		// x = maximum profit on selling the
		// wine from the front this year
		int x = price[begin] * year + maxProfitUtil(price, begin + 1, end, year + 1);

		// y = maximum profit on selling the
		// wine from the end this year
		int y = price[end] * year + maxProfitUtil(price, begin, end - 1, year + 1);

		return Math.max(x, y);
	}

	// Util Function to calculate maxProfit
	static int maxProfitR(int price[], int n) {
		int ans = maxProfitUtil(price, 0, n - 1, 1);
		System.out.println(ans);
		memo = new int[N][N];
		for(int i[]: memo)
		Arrays.fill(i, -1);
		
		
		
		int dp[][] = new int[n+1][n+1];
		
		System.out.println(maxProfitBottomUp(price));		
		ans = maxProfitUtilMemo(price, 0, n - 1, 1);
		return ans;
	}


	private static int maxProfitUtilMemo(int[] price, int begin, int end, int year) {
		if (begin == end) {
			return memo[begin][end] = price[begin] * year;
		}
		
		if(memo[begin][end]!=-1)
			return memo[begin][end];

		// x = maximum profit on selling the
		// wine from the front this year
		
		
		int x = price[begin] * year + maxProfitUtil(price, begin + 1, end, year + 1);
		int y = price[end] * year + maxProfitUtil(price, begin, end - 1, year + 1);

		return memo[begin+1][end] = Math.max(x, y);
	}
	    
	private static int maxProfitBottomUp(int[] price) {
	    int n = price.length;
	    int[][] dp = new int[n][n];

	    // Initialize the base cases (when there's only one wine)
	    for (int i = 0; i < n; i++) {
	        dp[i][i] = price[i] * n;
	    }

	    // Build the solution bottom-up, starting from subproblems of size 2 and increasing
	    for (int len = 2; len <= n; len++) {
	        for (int begin = 0; begin <= n - len; begin++) {
	            int end = begin + len - 1;
	            int year = n - (end - begin);

	            // Calculate the maximum profit for the current subproblem
	            int x = price[begin] * year + dp[begin + 1][end];
	            int y = price[end] * year + dp[begin][end - 1];

	            dp[begin][end] = Math.max(x, y);
	        }
	    }

	    // The final result is stored in the top-right corner of the DP table
	    return dp[0][n - 1];
	}

}


