package Recursion;

import java.util.ArrayList;

public class Subsets {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			String input ="123";
			String output="";
			
//			solve(input,output);
			ArrayList<String> ar = new ArrayList<String>();
			int n = 3;
			solve("",n,n,ar);
			
//			System.out.println(ar);

	}

	private static void solve(String output, int open, int close, ArrayList temp) {
		// TODO Auto-generated method stub
		if(open==0 && close==0 ) {
			temp.add(output);
			return ;
		}

		
		if(open!=0) {
			String op1 = output+"(";
			solve(op1,open-1,close,temp);
		}
		
		if(open<close) {
			String op2 = output+")";
			solve(op2,open,close-1,temp);
		}
		
	}
}

//	private static void solve(String input, String output) {
//		// TODO Auto-generated method stub
//		if(input.length()==0) {
//			System.out.println(output);
//			return ;
//		}
//		
//		String op1 = output;
//		String op2 = output;
//		
//		op2+= input.charAt(0);
//		input =input.substring(1);
//		
//		solve(input,op1);
//		solve(input,op2);
//		
//	}
//
//}
