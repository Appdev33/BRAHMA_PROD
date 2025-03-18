package DP;

import java.util.Arrays;

public class minInsertDeleteConvertAB {
	
	static int memo[][];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String S1 = "HEAP";
        String S2 = "PEA";
        int m = S1.length();
        int n = S2.length();
        
        memo = new int[m+1][n+1];
        for(int i[] : memo)
        	Arrays.fill(i, -1);
        
        int lcsLength = LCSMemo(S1,m,S2,n);
//        heap -> ea -> pea
//        2 deletion 1 insertion
/*
 * S1 = "heap" ,  S2 = "pea", lcs = "ea"

To convert S1 into S2,
  -> All other characters besides lcs, we have to delete from S1
  -> All other characters in S2 besides lcs, we have to insert into S1
Number of insertions = len( S2) - lcs
Number of deletions = len( S1) - lcs
 *   
 */
        
        System.out.println(m-lcsLength + n -lcsLength);

        
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
