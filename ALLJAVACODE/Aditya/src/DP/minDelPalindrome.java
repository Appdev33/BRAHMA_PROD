package DP;

import java.util.Arrays;

public class minDelPalindrome {

	static int memo[][];
	public static void main(String[] args) {

		String S1 = "AGGTAB";
		StringBuilder sb = new StringBuilder(S1);
        String S2 = sb.reverse().toString();
        int m = S1.length();
        int n = S2.length();
        
        System.out.println(m-LPSRecursive(S1,m,S2,n));
        memo = new int[m+1][n+1];
        for(int i[] : memo)
        	Arrays.fill(i, -1);
        System.out.println(m - LPSRecursive(S1,m,S2,n));
	}
	
	
	private static int LPSMemo(String S1, int m, String S2, int n) {
		if(m==0 || n==0)
			return memo[m][n] = 0;
		
		
		if(memo[m][n]!=-1)
			return memo[m][n];
		
		
		if(S1.charAt(m-1)==S2.charAt(n-1))
			return memo[m][n] = 1+ LPSMemo(S1,m-1,S2,n-1);
		else
			return memo[m][n] = Math.max(LPSMemo(S1,m-1,S2,n), LPSMemo(S1,m,S2,n-1));
	}

	private static int LPSRecursive(String S1, int m, String S2, int n) {

		if(m==0 || n==0)
			return 0;
		
		
		if(S1.charAt(m-1)==S2.charAt(n-1))
			return 1+ LPSRecursive(S1,m-1,S2,n-1);
		else
			return Math.max(LPSRecursive(S1,m-1,S2,n), LPSRecursive(S1,m,S2,n-1));
	}

}
