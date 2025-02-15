package Recursion;
import java.util.*;

public class SortStack {

	public static void main(String[] args) {
//	    Stack<Integer> st = new Stack<>();
//	    int ar[] = {5,1,0,2,5,6,9,21};
//			
//		for(int i: ar) 
//			st.push(i);
//		
//
//	    System.out.println("\nStack after sorting:");
//	    Stack<Integer> sorted = sortStack(st);
//	    for (Integer i : sorted) {
//	      System.out.print(i + " ");
//	    }
	    
//	    Stack<Integer> st = new Stack<>();
//	    int ar[] = {5,1,2,5,6,9,21};
//			
//		for(int i: ar) 
//			st.push(i);
//		
//		MidDel(st,st.size()/2+1);
//		System.out.println(st);
	    
		
		Stack<Integer> st = new Stack<>();
	    int ar[] = {5,1,2,5,6,9,21};
			
		for(int i: ar) 
			st.push(i);
		
		reverse(st);
		System.out.println(st);
	    
	  }

	private static Stack<Integer> reverse(Stack<Integer> st) {
		// TODO Auto-generated method stub
		
		if(st.size()<=1)
			return st;
		
		int val = st.pop();
		reverse(st);
		
		insert(st,val);
		
		return st;
	}

	private static Stack<Integer> insert(Stack<Integer> st, int val) {
		// TODO Auto-generated method stub
		if(st.size()==0) {
			st.push(val);
			return st;
		}
		
		int pop = st.pop();
		insert(st,val);
		st.push(pop);
		
		return st;
	}

	private static Stack<Integer> MidDel(Stack<Integer> st, int len) {
		// TODO Auto-generated method stub
		
		if(st.size()==1 || st.size()==len) {
			st.pop();
			return st;
		}
		
		int val = st.pop();
		MidDel(st,len);
		
		st.add(val);
		
		return st;
	}

	private static Stack<Integer> sortStack(Stack<Integer> st) {
		
		if(st.size()==1)
			return st;
		
		int pop = st.pop();
		sortStack(st);
		
		insertElementAtStack(st, pop);
		
		
		
		return st;
	}
	
	
	public static Stack<Integer> insertElementAtStack(Stack<Integer> st, int temp){
	    // Base Condition
	    if(st.size() == 0 || temp >= st.peek()){ // checking if let say we have 6 in temp & 6 is greater then 5
	      st.push(temp); // we will simply add it into our stack
	      return st;
	    }
	    // Hypothesis
	    int val = st.pop(); // getting 5 out stack becomes -> [0,1]
	    insertElementAtStack(st, temp); // inserting 2 to [0,1] which becomes -> [0,1,2]
	    // Induction
	    st.push(val); // adding 5 to [0,1,2] which becomes -> [0,1,2,5]
	    return st;
	  }
	

}
