package BinarySearch;

import java.util.*;

public class Solution {

	
	public static void main(String[] args) {
		String A = "barfoothefoobarman";
		String B[] = 	{"foo", "bar"}	;
		
		for(int i : findSubstring(A,B))
		System.out.print(i);
	}
	public static int[] findSubstring(String A, String[] B) {
		   int wordlength=B[0].length();
		        List<Integer> ans= new ArrayList<>();
		        Map<String,Integer> map= new HashMap<>();
		        for(String s:B)
		        {
		            map.put(s,map.getOrDefault(s,0)+1);
		        }
		        int words=B.length;
		        int wordslength=wordlength*words;
		        for(int i=0;i<=A.length()-wordslength;i++)
		        {
		         
		            String check=A.substring(i,i+wordlength);
		           
		            if(map.containsKey(check))
		            {
		                Map<String,Integer> freq= new HashMap<>();
		                for(int j=i;j<=A.length()-wordlength;j=j+wordlength)
		                {
		                    String nextcheck=A.substring(j,j+wordlength);
		                   
		                    if(map.containsKey(nextcheck))
		                    {
		                         freq.put(nextcheck,freq.getOrDefault(nextcheck,0)+1);
		                    }
		                    else
		                        break;
		                        
		                    if(freq.get(nextcheck)>map.get(nextcheck))
		                        break;
		                    // System.out.print(j+ "tttt" + i);    
		                    if((j-i+wordlength)==(wordslength))
		                    {
		                        ans.add(i);
		                        break;
		                    }
		                }
		            }
		        }
		        int n=ans.size();
		        int[] res= new int[n];
		        for(int i=0;i<n;i++){
		        res[i]=ans.get(i);
		        }
		        return res;
		       
		    }

}
