package DP;

import java.util.Arrays;

public class printSCS {

	static int memo[][];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String S1 = "AGGTABD";
        String S2 = "GXTXAY";
        int m = S1.length();
        int n = S2.length();
        
        memo = new int[m+1][n+1];
        for(int i[] : memo)
        	Arrays.fill(i, -1);
        
        System.out.println(SCSMemo(S1,m,S2,n));
        
        
        System.out.println(printingSCS(S1,S2,memo,n,m));
	}
	
	private static String printingSCS(String S1, String S2, int[][] memo,int n, int m) {

		StringBuilder sbr = new StringBuilder();
		int i = m;
		int j = n;
		while(i>0 && j>0) {
			
			if(S1.charAt(i-1)==S2.charAt(j-1)) {
				sbr.append(S1.charAt(i-1));
				i--;
				j--;
			}else if(memo[i-1][j] > memo[i][j-1]) {
				sbr.append(S1.charAt(i-1));
//				sbr.append(S2.charAt(j-1));
				i--;
			}else {
//				sbr.append(S1.charAt(i-1));
				sbr.append(S2.charAt(j-1));
				j--;
			}
		}
		
        while(i > 0) {
            sbr.append(S1.charAt(i-1));
            i--;
        }


        while(j > 0) {
            sbr.append(S2.charAt(j-1));
            j--;
        }

        return sbr.reverse().toString();
		
	}

	private static int SCSMemo(String S1, int m, String S2, int n) {
		if(m==0 || n==0)
			return memo[m][n] = 0;
		
		
		if(memo[m][n]!=-1)
			return memo[m][n];
		
		
		if(S1.charAt(m-1)==S2.charAt(n-1))
			return memo[m][n] = 1+ SCSMemo(S1,m-1,S2,n-1);
		else
			return memo[m][n] = Math.max(SCSMemo(S1,m-1,S2,n), SCSMemo(S1,m,S2,n-1));
	}

}