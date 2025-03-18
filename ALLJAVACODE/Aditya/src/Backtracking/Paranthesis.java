package Backtracking;

import java.util.ArrayList;

public class Paranthesis {

	static ArrayList<String> res;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		res = new ArrayList<>();
		int n = 3;
		
		solveP(n,n,new StringBuilder());
		
		System.out.println(res);

	}
	
	public static void solveP(int open, int close, StringBuilder temp) 
	{   
		if(open>close)  
			return;
		
		if(open==0 && close ==0) {
			res.add(temp.toString());
		}
		
		if(open>0) {
			temp.append('(');
			solveP(open-1,close,temp);
			temp.deleteCharAt(temp.length()-1);
		}
		
		if(close>0) {
			temp.append(')');
			solveP(open,close-1,temp);
			temp.deleteCharAt(temp.length()-1);
		}
		
	}

}


