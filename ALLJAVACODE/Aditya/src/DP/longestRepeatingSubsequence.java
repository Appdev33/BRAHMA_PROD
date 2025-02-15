package DP;

import java.util.Arrays;

public class longestRepeatingSubsequence {

	static int memo[][];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String S1 = "AABHBIDED";
        String S2 = "AABHBIDED";
        int m = S1.length();
        int n = S2.length();
        
        System.out.println(longestRepeatingSubsequenceRecursive(S1,m,S2,n));
        memo = new int[m+1][n+1];
        for(int i[] : memo)
        	Arrays.fill(i, -1);
        
        System.out.println(longestRepeatingSubsequenceMemo(S1,m,S2,n));
        
        System.out.println(longestRepeatingSubsequenceDP(S1,m,S2,n));

	}

	private static int longestRepeatingSubsequenceDP(String X, int m, String Y, int n) {
		int L[][] = new int[m + 1][n + 1];
		 
        // Following steps build L[m+1][n+1] in bottom up
        // fashion. Note that L[i][j] contains length of LCS
        // of X[0..i-1] and Y[0..j-1]
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0)
                    L[i][j] = 0;
                else if (X.charAt(i - 1) == Y.charAt(j - 1) && i!=j)
                    L[i][j] = L[i - 1][j - 1] + 1;
                else
                    L[i][j] = max(L[i - 1][j], L[i][j - 1]);
            }
        }
        return L[m][n];
	
	}
	
	public static int max(int a, int b) { return (a > b) ? a : b; }

	private static int longestRepeatingSubsequenceMemo(String S1, int m, String S2, int n) {
		if(m==0 || n==0)
			return memo[m][n] = 0;
		
		
		if(memo[m][n]!=-1)
			return memo[m][n];
		
		
		if(S1.charAt(m-1)==S2.charAt(n-1) && m!=n)
			return memo[m][n] = 1+ longestRepeatingSubsequenceMemo(S1,m-1,S2,n-1);
		else
			return memo[m][n] = Math.max(longestRepeatingSubsequenceMemo(S1,m-1,S2,n), longestRepeatingSubsequenceMemo(S1,m,S2,n-1));
	}

	private static int longestRepeatingSubsequenceRecursive(String S1, int m, String S2, int n) {

		if(m==0 || n==0)
			return 0;
		
		
		if(S1.charAt(m-1)==S2.charAt(n-1) && m!=n)
			return 1+ longestRepeatingSubsequenceRecursive(S1,m-1,S2,n-1);
		else
			return Math.max(longestRepeatingSubsequenceRecursive(S1,m-1,S2,n), longestRepeatingSubsequenceRecursive(S1,m,S2,n-1));
	}

}
