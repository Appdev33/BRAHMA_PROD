package DP;

import java.util.Arrays;

public class shortestCommonSuperSequence {

	static int memo[][];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String S1 = "AGGTAB";
        String S2 = "GXTXAYB";
        int m = S1.length();
        int n = S2.length();
        
        memo = new int[m+1][n+1];
        for(int i[] : memo)
        	Arrays.fill(i, -1);
        
        System.out.println(m+n -  LCSMemo(S1,m,S2,n));

        
    }
    
    
    private static int LCSMemo(String S1, int m, String S2, int n) {
		if(m==0 || n==0)
			return memo[m][n] = 0;
		
		
		if(memo[m][n]!=-1)
			return memo[m][n];
		
		
		if(S1.charAt(m-1)==S2.charAt(n-1))
			return memo[m][n] = 1+ LCSMemo(S1,m-1,S2,n-1);
		else
			return memo[m][n] = Math.max(LCSMemo(S1,m-1,S2,n), LCSMemo(S1,m,S2,n-1));
	}
}
