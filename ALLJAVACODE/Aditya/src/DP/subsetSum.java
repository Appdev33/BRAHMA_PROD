package DP;

import java.util.Arrays;


// subset sum = subset diff two equations = target sum by pairing

public class subsetSum {

	static int memo[][];

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int ar[] = {3, 34, 4, 12, 5, 2};
		int sum = 38;
		int n = ar.length;
		memo = new int[n+1][sum+1];
		for(int i[]: memo)
			Arrays.fill(i, -1);
		
		System.out.println(subsetSumMemo(ar,sum,n));
		System.out.println(subsetSumRecursive(ar,sum,n));
		System.out.println(subsetSumDp(ar,sum,n));
	}

	private static int subsetSumDp(int arr[],int n, int sum) 
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

	private static int subsetSumMemo(int[] ar, int sum, int n) {
		// TODO Auto-generated method stub
		
		if(sum==0)
			return memo[n][sum]=1;
		
		if(n==0 || sum<0)
			return memo[n][sum]=0;
		

		
		if(memo[n][sum]!=-1)
			return memo[n][sum];
		
		if(ar[n-1]<=sum)
			return memo[n][sum] = (subsetSumMemo(ar,sum-ar[n-1],n-1) !=0 || subsetSumMemo(ar,sum,n-1) !=0  )? 1:0 ;
		else
			return memo[n][sum] = subsetSumMemo(ar,sum,n-1);
	}

	private static boolean subsetSumRecursive(int[] ar, int sum, int n) {
		// TODO Auto-generated method stub
		if(sum==0)
			return true;
		
		if(n==0 || sum<0)
			return false;

		if(ar[n-1]<=sum)
			return subsetSumRecursive(ar,sum-ar[n-1],n-1) ||  subsetSumRecursive(ar,sum,n-1) ;
		else
			return subsetSumRecursive(ar,sum,n-1);
		
	}

}
