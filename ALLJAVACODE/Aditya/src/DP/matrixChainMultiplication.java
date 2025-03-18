package DP;

import java.util.Arrays;

public class matrixChainMultiplication {

	static int memo[][];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = new int[] { 1, 2, 3, 4, 3 };
        int N = arr.length;
        
        
        System.out.println(MCM_Recursive(arr,1,arr.length-1));
        memo = new int[N+1][N+1];
        
        for(int i[]: memo)
        	Arrays.fill(i, -1);
        
        System.out.println(MCM_DP(arr,1,arr.length-1));
	}

	private static int MCM_DP(int[] arr, int i, int j) {
		if(i>=j)
			return memo[i][j] = 0;
		
		
		if(memo[i][j]!=-1)
			return memo[i][j];
		
		int ans = Integer.MAX_VALUE;
		
		for(int k = i; k<=j-1 ;k++) {
			
			int temp = MCM_Recursive(arr,i,k)+MCM_Recursive(arr,k+1,j) + arr[i-1]*arr[j]*arr[k];
			
			ans = Math.min(ans,temp);
		}
		
		return memo[i][j] = ans;
		
	}

	private static int MCM_Recursive(int[] arr, int i, int j) {
		
		if(i>=j)
			return 0;
		
		int ans = Integer.MAX_VALUE;
		
		for(int k = i; k<=j-1 ;k++) {
			
			int temp = MCM_Recursive(arr,i,k)+MCM_Recursive(arr,k+1,j) + arr[i-1]*arr[j]*arr[k];
			
			ans = Math.min(ans,temp);
		}
		
		return ans;
	}

}
