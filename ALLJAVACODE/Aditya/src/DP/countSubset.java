package DP;

import java.util.Arrays;

public class countSubset {
	
	static int memo[][];
	public static void main(String[] args) {
		
		int ar[] = {1, 1, 1, 1, 1, 1};
		int sum = 5;
		int n = ar.length;
		memo = new int[n+1][sum+1];
		for(int i[]: memo)
			Arrays.fill(i, -1);
		
		System.out.println(subsetSumMemo(ar,n,sum));
		System.out.println(countSubsetRecursive(ar,sum,n));
//		System.out.println(subsetSumDp(ar,sum,n));
	}
	
	
		private static int subsetSumMemo(int arr[],int n, int sum) 
		{ 
		    
		    int[][] dp = new int[n+1][sum+1];
		    
		      dp[0][0]=1;
	           for(int j=1;j<sum+1;j++)
	           {
	                   dp[0][j]=0;
	               
	           }
	      for(int i=1;i<n+1;i++) 
	          {
	           for(int j=0;j<sum+1;j++)
	           {
	               if(arr[i-1]<=j)
	               {
	                   dp[i][j]=dp[i-1][j]%1000000007 + dp[i-1][j-arr[i-1]]%1000000007;
	               }
	               else{
	                  dp[i][j]=dp[i-1][j]%1000000007; 
	               }
	           }
	       }
	       return dp[n][sum]%1000000007;
		}

	private static int countSubsetRecursive(int[] ar, int sum, int n) {
		// TODO Auto-generated method stub
		if(sum==0)
			return 1;
		
		if(n<=0 || sum<0)
			return 0;

		if(ar[n-1]<=sum)
			return countSubsetRecursive(ar,sum-ar[n-1],n-1) +  countSubsetRecursive(ar,sum,n-1) ;
		else
			return countSubsetRecursive(ar,sum,n-1);
		
	}

}
