package DP;

import java.util.Arrays;


public class MinimumSubsetSum {
	
	static int memo[][];
	public static void main(String[] args) {

		
		int ar[] = {1, 2, 4, 5, 9};
		int sum = 0;
		int n = ar.length;
//		memo = new int[n+1][sum+1];
//		for(int i[]: memo)
//			Arrays.fill(i, -1);
		
		for(int i : ar)
			sum+=i;
		memo = new int[n+1][sum+1];
		for(int i[]: memo)
			Arrays.fill(i, -1);
		
		System.out.println(MinimumSubsetSumRecursive(ar,n,0,sum));
		System.out.println(MinimumSubsetSumMemo(0, 0, ar, n, sum));
	}

	private static int MinimumSubsetSumMemo(int idx, int sum, int[] arr, int n,
            int totalSum) {
		
		if (idx == n) {
            // One subset sum is 'sum' and the other is
            // 'totalSum - sum'
            return Math.abs((totalSum - sum) - sum);
        }
 
        if (memo[idx][sum] != -1) {
            // If the result for the current index
            // and sum is already computed, return it
            return memo[idx][sum];
        }
 
        // Include the current element in the sum
        int pick = MinimumSubsetSumMemo(idx + 1, sum + arr[idx], arr, n,
                     totalSum);
 
        // Exclude the current element from the sum
        int notPick = MinimumSubsetSumMemo(idx + 1, sum, arr, n, totalSum);
 
        // Store the minimum result in the memoization table
        // and return it
        return memo[idx][sum] = Math.min(pick, notPick);
	}

	private static int MinimumSubsetSumRecursive(int[] ar, int n, int sumCalculated, int sumTotal) {
		
		if(n==0)
			return Math.abs(sumTotal- 2*sumCalculated);
		
		return Math.min(MinimumSubsetSumRecursive(ar,n-1,sumCalculated+ar[n-1],sumTotal),
				MinimumSubsetSumRecursive(ar,n-1,sumCalculated,sumTotal));
	}

}




//extension of subset sum  
// s1 , s2 two subsets
//// range s1,s2  - > ( 0 , sigma(arr[i]))
//// s1 , range - s1
//// range - s1 - s1
//// minimise  - > range - 2s1
//	public int minDifference(int arr[], int n) 
//	{ 
//	    // Your code goes here
//	    int sum = Arrays.stream(arr).sum();
//	   boolean [][] dp = new boolean[arr.length + 1][sum + 1];
//     List<Integer>ls=subset_sum(dp,sum,arr);
//     int min=Integer.MAX_VALUE;
//     for(int i=0;i<=ls.size()/2;i++){
//         min=Math.min(min,Math.abs(sum-2*ls.get(i)));
//     }
//     return min;
//	}
//	
//	 private static List<Integer> subset_sum(boolean[][] dp, int sum,int[] arr) {
//     List<Integer> ans=new ArrayList<>();
//     for(int i=0;i<dp.length;i++){
//         for(int j=0;j<dp[i].length;j++){
//             if(j==0){
//                 dp[i][j]=true;
//             }
//         }
//     }
//
//     for(int i=1;i<dp.length;i++){
//         for(int j=1;j<dp[i].length;j++){
//             if(arr[i-1]<=j)
//                 dp[i][j]=dp[i-1][j-arr[i-1]] || dp[i-1][j];
//             else dp[i][j]=dp[i-1][j];
//             }
//         }
//
//     for(int i=0;i<dp.length;i++){
//         for(int j=0;j<dp[i].length;j++){
//             if(i==dp.length-1){
//                 if(dp[i][j]==true)
//                     ans.add(j);
//             }
//         }
//     }
//
//     return ans;
//     }

