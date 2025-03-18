package Recursion;

import java.util.*;

public class Print1toN {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int N = 10;
//		helper(N);
//		helper1(N);
		
		ArrayList arr = new ArrayList(Arrays.asList(5,1,0,2,5,6,9,21));
        arr = sort(arr);
        System.out.println(arr);
	}
	
	
	public static ArrayList sort(ArrayList<Integer> arr){
		
		
		if(arr.size()<=1)
			return arr;
		
		int temp = arr.get(arr.size()-1);
		arr.remove(arr.size()-1);
		sort(arr);
		
		insert(arr,temp);
        return arr;
		
	}
	
	
	public static ArrayList<Integer> insert(ArrayList<Integer> arr, int temp) {
		
		if(arr.size()==0 || temp>= arr.get(arr.size()-1)) {
			arr.add(temp);
			return arr;
		}
		
		int val  = arr.get(arr.size()-1);
		arr.remove(arr.size()-1);
		insert(arr,temp);
		
		
		arr.add(val);
		return arr;
		
	}
	
	
	public static void helper1(int N) {
			
			if(N==0)
			   return;
			
			System.out.print(N + " ");
			
			helper1(N-1);
			
			
		}

}
