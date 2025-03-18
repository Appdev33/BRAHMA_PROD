package DP;

import java.util.Arrays;

public class knapSack01 {
	
	static int[][] memo;
	static int[][] dp;
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int profit[] = new int[] { 600, 110, 120 }; 
        int weight[] = new int[] { 10, 20, 30 }; 
        int W = 50; 
        int n = profit.length; 
        
//        System.out.println(knapSackRecursive(W,weight,profit,n));
        memo = new int[n+1][W+1];
        for( int i[]: memo)
        Arrays.fill(i, -1);
        
//        System.out.println(knapSackMemo(W,weight,profit,n));
        System.out.println(knapSackTopDown(W,weight,profit,n));
	}

	private static int knapSackTopDown(int W, int[] weight, int[] profit, int n) {
		
		dp = new int[n+1][W+1];
		
		for(int i=0; i<=n ;i++) {
			for(int j=0; j<=W; j++ ) {
				
				if(i==0 || j==0)
					dp[i][j]=0;
				else if(weight[i-1]>j) {
					dp[i][j] = dp[i-1][j];
				}else
					dp[i][j] = Math.max(dp[i-1][j], profit[i-1]+dp[i-1][j-weight[i-1]]);
				
			}
		}
		
		return dp[n][W];
	}

	private static int knapSackMemo(int W, int[] weight, int[] profit, int n) {

		// TODO Auto-generated method stub
		if(n==0 || W==0)
			return memo[n][W]=0;
		
		if(memo[n][W]!=-1)
			return memo[n][W];
		
		if(weight[n-1]>W) {
			 return memo[n][W] = knapSackRecursive(W,weight,profit,n-1);
		}else
			return memo[n][W] = Math.max(profit[n-1] + knapSackRecursive(W-weight[n-1],weight,profit,n-1),  knapSackRecursive(W,weight,profit,n-1)    );
		
 	}

	private static int knapSackRecursive(int W, int[] weight, int[] profit,int n) {
		// TODO Auto-generated method stub
		
		if(n==0 || W==0)
			return 0;
		
		if(weight[n-1]>W) {
			 return knapSackRecursive(W,weight,profit,n-1);
		}else
			return Math.max(profit[n-1] + knapSackRecursive(W-weight[n-1],weight,profit,n-1),  knapSackRecursive(W,weight,profit,n-1)    );
		
	}

}
