package DP;

import java.util.HashMap;

public class ScrabledString {
	
	static HashMap<String,Boolean> map =new HashMap<>();
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String a = "great";
		String b = "rgtae";
		
		
		if(a.length()==b.length())
			System.out.println(ScrabledStringRecursive(a,b));
		else
			System.out.println(false);
		
		System.out.println(solveMemo(a,b));
	}

	private static boolean ScrabledStringRecursive(String a, String b) {

		if(a.equals(b))
			return true;
		
		if(a.length()<=1) return false;
		
		int n = a.length();
		
		boolean flag = false;
		
		for(int k=1; k<=n-1; k++) {
			
			
			if( ScrabledStringRecursive(a.substring(0,k)  , b.substring(a.length()-k))==true  && ScrabledStringRecursive(a.substring(a.length()-k),b.substring(0,k))==true ) {
//				System.out.println(a.substring(0,k) + b.substring(a.length()-k));    great eatgr swapped hence  b.substring(a.length()-k) 3 letters ahead of eat since gr shifted
				flag = true;
				break;
			}
			if( ScrabledStringRecursive(a.substring(0,k)  , b.substring(0,k))==true  && ScrabledStringRecursive(a.substring(k),b.substring(k))==true ) {
				flag = true;
				break;
			}
			
		}
		
		return flag;
	
	}
	
		public static boolean solveMemo(String a, String b){
	        //Base Case ::
	        int n=a.length();
	        if(a.equals(b)) return true;
	        if(a.length()<=1) return false;
	        String key =a+" "+b;
	        if(map.containsKey(key)){
	            return (boolean)map.get(key);
	        }
	        //k loop
	        boolean flag=false;
	        for(int k=1;k<=n-1;k++){
	            boolean test1=false,test2=false;
	            test1 =((solveMemo(a.substring(0,k),b.substring(n-k,n)))&& (solveMemo(a.substring(k,n),b.substring(0,n-k))));
	            test2 =((solveMemo(a.substring(0,k),b.substring(0,k))) && (solveMemo(a.substring(k,n),b.substring(k,n))));
	            if(test1 || test2){
	                flag=true;
	                break;
	            }
	            
	        }
	        map.put(key,flag);
	        return flag;
	    }
}


