package DP;

public class CoinChange {
	
	private static final int INVALID_COMBINATION = -1;
	static int[][] memo ;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int coins[] = {1,2,5};
		int amount = 11;
		//Recursive
	       int n = coins.length;
	        
	       if(amount ==0)
	           System.out.println(0); 
	        if(coins.length==0)
	            System.out.println(0); 
	        
	       int ways =  CoinChangeRecursive(coins,amount,0);
	        
	        System.out.println( (ways == Integer.MAX_VALUE-1)?-1:ways);
	        
	        int waysMemo =  CoinChangeRecursiveMemo(coins,amount,0);
	        memo = new int[coins.length][amount + 1];
	        System.out.println( (ways == Integer.MAX_VALUE-1)?-1:ways);
		
	}

	private static int CoinChangeRecursiveMemo(int[] coins, int currIndex, int remainingAmount) {
	      
		if (currIndex >= coins.length || remainingAmount < 0) 
	      return INVALID_COMBINATION;
	 
		  if (remainingAmount == 0) 
		      return 0;
		 
		  if (memo[currIndex][remainingAmount] != 0) 
		      return memo[currIndex][remainingAmount];
		 
		  int min = Integer.MAX_VALUE;
		 
		  // Take the current coin
		  int withCurrent = CoinChangeRecursiveMemo(coins, currIndex, remainingAmount - coins[currIndex]);
		 
		  if (withCurrent != INVALID_COMBINATION) 
		      min = Math.min(min, withCurrent + 1);
		
		//  // Do not take the current coin
		  int withoutCurrent = CoinChangeRecursiveMemo(coins, currIndex + 1, remainingAmount);
		 
		  if (withoutCurrent != INVALID_COMBINATION) 
		      min = Math.min(min, withoutCurrent);
		 
		  if (min == Integer.MAX_VALUE) 
		      min = INVALID_COMBINATION;
		 
		  return memo[currIndex][remainingAmount] = min;
		
		  
	}

	private static int CoinChangeRecursive(int coins[],int amount, int index) {
		
		if(coins.length==index || amount==0) // if we reached end of array and amount is zero
        {
            if(amount==0)
                return 0;
            return Integer.MAX_VALUE-1;
        }
        
        int ways=0;
        
        if(coins[index]<=amount)
        {
          ways=Math.min(1+CoinChangeRecursive(coins,amount-coins[index],index),  // we are return 1+MAX it will overlap
        		  CoinChangeRecursive(coins,amount,index+1));   //Take or not take
        }
        else
        {
            ways=CoinChangeRecursive(coins,amount,index+1);
        }        
        return ways;
	}
	
	
/*	
	import java.util.Arrays;

	public class CoinChange {
	    // Memoization table to store the results of subproblems
	    private static int[][] memo;

	    private static int CoinChangeRecursive(int coins[], int amount, int index) {
	        // Base Case: If the amount is zero, return 0 (no coins needed)
	        if (amount == 0) {
	            return 0;
	        }

	        // Base Case: If no coins are left and amount is not zero, return a large number
	        if (index == coins.length) {
	            return Integer.MAX_VALUE - 1;
	        }

	        // If the result has already been computed, return it
	        if (memo[index][amount] != -1) {
	            return memo[index][amount];
	        }

	        int ways;

	        if (coins[index] <= amount) {
	            // Compute the minimum coins needed if including or excluding the current coin
	            ways = Math.min(1 + CoinChangeRecursive(coins, amount - coins[index], index),
	                            CoinChangeRecursive(coins, amount, index + 1));
	        } else {
	            // Exclude the current coin and move to the next one
	            ways = CoinChangeRecursive(coins, amount, index + 1);
	        }

	        // Store the result in the memoization table
	        memo[index][amount] = ways;
	        return ways;
	    }

	    public static int coinChange(int[] coins, int amount) {
	        // Initialize the memoization table with -1 (indicating uncomputed subproblems)
	        memo = new int[coins.length][amount + 1];
	        for (int[] row : memo) {
	            Arrays.fill(row, -1);
	        }

	        int result = CoinChangeRecursive(coins, amount, 0);
	        return (result == Integer.MAX_VALUE - 1) ? -1 : result;
	    }

	    public static void main(String[] args) {
	        int[] coins = {1, 2, 5};
	        int amount = 11;
	        int result = coinChange(coins, amount);
	        System.out.println("Minimum coins required: " + result);
	    }
	}

	
	*/
	
	/*
    public int coinChange(int[] coins, int amount)
    {
        if(amount<1) 
            return 0;
        
        int[] dp = new int[amount+1];
        int sum = 0;

        while(++sum<=amount)
        {
            int min = -1;
            for(int coin : coins) 
            {
                if(sum >= coin && dp[sum-coin]!=-1)
                {
                    int temp = dp[sum-coin]+1;
                    
                    if (min < 0 || temp < min)
                        min = temp;
                }
            }
            
            dp[sum] = min;
        }
        
        return dp[amount];
    }*/

}


//class Solution {
//    public int coinChange(int[] coins, int sum) {
//        int m=coins.length;
//       int[][] dp = new  int[m+1][sum+1];
//       for(int i=0 ;i<m+1;i++){
//           for(int j=0 ;j<sum+1 ;j++){
//               if(i==0){
//			   //here we are storing Integer.MAX_VALUE -1 because if we store Integer.MAX_VALUE and we add +1 then it exceeds the max storage
//                   dp[i][j]=Integer.MAX_VALUE -1;
//               }
//               else if(i==1){
//                   if(j%coins[0]==0)
//                       dp[i][j]=j/coins[0];
//                   else
//                       dp[i][j]=Integer.MAX_VALUE-1;
//               }
//               
//               else if(coins[i-1]<=j){
//                   dp[i][j]= Math.min(1 + dp[i][j-coins[i-1]] , dp[i-1][j]);
//               }
//               else{
//                   dp[i][j]= dp[i-1][j];
//               }
//           }
//       }
//       if(dp[m][sum] == Integer.MAX_VALUE-1)
//    {
//        return -1;
//    }
//    else
//    {
//        return dp[m][sum];
//    }
//     }
//
//}

//1. if (amount == 0) return 0;
//What it means: If the amount becomes 0, it indicates that the remaining amount can be formed exactly using the coins chosen so far.
//Why return 0?:
//Since no more coins are needed to form the rest of the amount (0), the function returns 0, representing no additional coins.
//This result will propagate back through the recursion as a valid solution.
//2. return Integer.MAX_VALUE - 1;
//What it means: If the function reaches the end of the coins array (coins.length == index) and the amount is still greater than 0, it indicates that it's not possible to form the remaining amount with the given coins.
//Why Integer.MAX_VALUE - 1?:
//Returning a large value (Integer.MAX_VALUE - 1) signifies an invalid solution. The -1 ensures that arithmetic operations (like +1 during recursion) do not cause integer overflow.
//This ensures that during recursion, the invalid path will not be chosen when comparing results (since we're looking for the minimum number of coins).
//Role of These Return Values in the Algorithm:
//0: Represents a valid solution with no additional coins needed.
//Integer.MAX_VALUE - 1: Represents an invalid solution, ensuring that paths that cannot form the target amount are ignored when finding the minimum.
//
