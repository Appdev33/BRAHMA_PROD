package DP;

import java.util.Arrays;

public class PalindromePartitioning {
	
	
	static int memo[][];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "nitoin";
		
		System.out.println(palindromePartition(str,0,str.length()));
		
		memo = new int[str.length()+1][str.length()+1];
		
		for(int i[] : memo)
			Arrays.fill(i,-1);
		
		System.out.println(palindromePartitionMemo(str,0,str.length()));
		
		
		System.out.println(palindromePartitionMemoOptimised(str,0,str.length()));
		
		
	}
	
	private static int palindromePartitionMemoOptimised(String str, int i, int j) {
		if(i>=j)
			return memo[i][j]=0;
		
		if(isPalindrome(str,i,j))
			return memo[i][j]=0;
		
		if(memo[i][j]!=-1)
			return memo[i][j];
		
		int ans = Integer.MAX_VALUE;
		
		int left = 0;
		int right = 0;
		for(int k=i; k<j ; k++) {
			
			
			if(memo[i][k]!=-1)
				left = palindromePartitionMemoOptimised(str,i,k);
			if(memo[k+1][j]!=-1)
				right = palindromePartitionMemoOptimised(str,k+1,j);
			
			int temp = left + right + 1;
			
			ans = Math.min(ans, temp);
		}
		
		return memo[i][j]=ans;
		
	}
	/*
	 public int solveRecursionMemo(String s, int i, int j) {
    if (i >= j || isPalindrome(s, i, j)) {
        return 0;
    }
    
    if (memo[i][j] != -1) {
        return memo[i][j];
    }
    
    int ans = Integer.MAX_VALUE;

    for (int k = i; k < j; k++) {
        int left, right;

        // Compute left subproblem if not memoized
        if (memo[i][k] != -1) {
            left = memo[i][k];
        } else {
            left = solveRecursionMemo(s, i, k);
            memo[i][k] = left;
        }

        // Compute right subproblem if not memoized
        if (memo[k + 1][j] != -1) {
            right = memo[k + 1][j];
        } else {
            right = solveRecursionMemo(s, k + 1, j);
            memo[k + 1][j] = right;
        }

        int temp = left + right + 1;
        ans = Math.min(ans, temp);
    }

    return memo[i][j] = ans;
}

	 */
	

	private static int palindromePartitionMemo(String str, int i, int j) {
		if(i>=j)
			return memo[i][j]=0;
		
		if(isPalindrome(str,i,j))
			return memo[i][j]=0;
		
		if(memo[i][j]!=-1)
			return memo[i][j];
		
		int ans = Integer.MAX_VALUE;
		
		for(int k=i; k<j ; k++) {
			
			int temp = palindromePartitionMemo(str,i,k) + palindromePartitionMemo(str,k+1,j) + 1;
			
			ans = Math.min(ans, temp);
		}
		
		return memo[i][j]=ans;
		
	}

	private static int palindromePartition(String str, int i, int j) {
		
		if(i>=j)
			return 0;
		
		if(isPalindrome(str,i,j))
			return 0;
		
		int ans = Integer.MAX_VALUE;
		
		for(int k=i; k<j ; k++) {
			
			int temp = palindromePartition(str,i,k) + palindromePartition(str,k+1,j) + 1;
			
			ans = Math.min(ans, temp);
		}
		
		return ans;
		
	}

	private static boolean isPalindrome(String str, int i, int j) {
		while(i<=j) {
			if(str.charAt(i++)!=str.charAt(--j))
				return false;
		}
		return true;
	}
}
