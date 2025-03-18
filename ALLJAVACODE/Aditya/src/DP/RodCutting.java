package DP;

import java.util.Arrays;

public class RodCutting {

	static int memo[][];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int arr[] = { 1, 5, 8, 9, 10, 17, 17, 20 };
		int wt[] = {1,2,3,4,5,6,7,8};
        int n = arr.length;
        int len = 20;
        
        
        System.out.println(RodCuttingRecursive(len,wt,arr,n));
        memo = new int[n+1][len+1];
        for(int i[] : memo)
        	Arrays.fill(i, -1);
        
        System.out.println(RodCuttingMemo(len,wt,arr,n));
//        System.out.println(RodCuttingdp(len,wt,arr,n));
	}
	
	
	private static int RodCuttingMemo(int len, int[] weight, int[] profit, int n) {
		if(n==0 || len==0)
			return memo[n][len]=0;
		
		if(memo[n][len]!=-1)
			return memo[n][len];
		
		if(weight[n-1]>len) {
			 return memo[n][len]= RodCuttingRecursive(len,weight,profit,n-1);
		}
			return memo[n][len]= Math.max(profit[n-1] + RodCuttingRecursive(len-weight[n-1],weight,profit,n),  RodCuttingRecursive(len,weight,profit,n-1)    );
		
	}


	private static int RodCuttingRecursive(int len, int[] weight, int[] profit,int n) {
		// TODO Auto-generated method stub
		
		if(n==0 || len==0)
			return 0;
		
		if(weight[n-1]>len) {
			 return RodCuttingRecursive(len,weight,profit,n-1);
		}
			return Math.max(profit[n-1] + RodCuttingRecursive(len-weight[n-1],weight,profit,n),  RodCuttingRecursive(len,weight,profit,n-1)    );
		
	}
	
	
//	public static int cutRod(int price[], int n) {
//	        
//	        int[] len = new int[n];
//	        
//	        // making the length array
//	        
//	        for(int i = 0 ; i < n ; i++){
//	            len[i] = i+ 1;
//	        }
//	        
//	        //code here
//	        int[][] dp = new int[n+1][n+1];
//	        
//	        for(int i = 0 ; i < n + 1; i++){
//	            for(int j = 0 ; j< n+1 ; j++){
//	                if(i == 0 || j ==0){
//	                    dp[i][j]  = 0;
//	                }
//	            }
//	        }
//	        for(int i = 1 ; i < n + 1; i++){
//	            for(int j = 1 ; j< n+1 ; j++){
//	                if(len[i-1] <=j){
//	                    dp[i][j] = Math.max(price[i-1] + dp[i][j-len[i-1]],dp[i-1][j]);
//	                }
//	                else{
//	                    dp[i][j] = dp[i-1][j];
//	                }
//	        
//	        }
//	    }
//	    return dp[n][n];
//	}
}
