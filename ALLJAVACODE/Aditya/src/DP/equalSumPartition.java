package DP;

import java.util.Arrays;

public class equalSumPartition {
	
	static int memo[][];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		int ar[] = {1, 2, 3, 5, 5};
		int sum = 0;
		int n = ar.length;
		memo = new int[n+1][sum+1];
		for(int i[]: memo)
			Arrays.fill(i, -1);
		
		for(int i : ar)
			sum+=i;
		
		if(sum%2!=0)
			System.out.println(false);
		else {
	//		System.out.println(equalSumPartitionMemo(ar,sum,n));
			System.out.println(equalSumPartitionRecursive(ar,sum/2,n));
//			System.out.println(equalSumPartitionDp(ar,sum,n));
		}
	}

	private static char[] equalSumPartitionDp(int[] ar, int sum, int n) {
		// TODO Auto-generated method stub
		return null;
	}

	private static boolean equalSumPartitionRecursive(int[] ar, int sum, int n) {
		if(sum==0)
			return true;
		
		if(sum<0 || n==0)
			return false;
		
		if(ar[n-1]<=sum)
			return equalSumPartitionRecursive(ar,sum-ar[n-1],n-1) ||  equalSumPartitionRecursive(ar,sum,n-1) ;
		else
			return equalSumPartitionRecursive(ar,sum,n-1);
	}

}
