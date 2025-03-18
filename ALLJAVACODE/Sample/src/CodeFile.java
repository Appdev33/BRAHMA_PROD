import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class CodeFile {

    public static void main(String[] args) {
    	int power[] = {2,3,4,4,4,5,6};
    	
    	int[] nums = {3, 1, 2, 3, 3, 2, 2, 3};
        int k = 4;
    	// Step 1: Identify potential candidates
        int[] candidates = new int[k - 1];
        int[] votes = new int[k - 1];

        // Initialize candidates and votes
        Arrays.fill(candidates, Integer.MIN_VALUE);
        Arrays.fill(votes, 0);

        for (int num : nums) {
            boolean found = false;

            // Check if the current number matches an existing candidate
            for (int i = 0; i < k - 1; i++) {
                if (candidates[i] == num) {
                    votes[i]++;
                    found = true;
                    break;
                }
            }

            if (!found) {
                // Check for an empty slot to add the candidate
                for (int i = 0; i < k - 1; i++) {
                    if (votes[i] == 0) {
                        candidates[i] = num;
                        votes[i] = 1;
                        found = true;
                        break;
                    }
                }
            }

            if (!found) {
                // Decrement votes for all candidates
                for (int i = 0; i < k - 1; i++) {
                    votes[i]--;
                }
            }
        }

        // Step 2: Validate candidates
        int[] counts = new int[k - 1];
        for (int num : nums) {
            for (int i = 0; i < k - 1; i++) {
                if (candidates[i] == num) {
                    counts[i]++;
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < k - 1; i++) {
            if (counts[i] > n / k) {
                result.add(candidates[i]);
            }
        }
        
        System.out.println(result);

        

    	
//    	HashMap<Integer,Integer> map = new HashMap<>();
//    	
//    	for(int i: power) {
//    		map.put(i,map.getOrDefault(i, map.get(i)+1));
//    	}
//    	
//    	System.out.println(map);
//    }
//}
    
//    	        int ar[] = {2, 12, 6, 7, 8, 9, 10, 11, 5, 13};
//    	        
//    	        for(int i=1; i<ar.length; i++) {
//    	        	if(ar[i]%2==0) {
//    	        		int key = ar[i];
//    	        		int j = i-1;
//    	        	
//    	        	
//    	        	
//	    	        	while(j>=0 && ar[j]%2!=0) {
//	    	        		ar[j+1]=ar[j];
//	    	        		j--;
//	    	        	}
//	    	        	
//	    	        	ar[j+1] = key;
//    	        	}
//    	        }
//    	        
//    	        Arrays.stream(ar).forEach(i -> System.out.print(i + " "));
//    	        
//    	        System.out.println();
//    	        
//    	        int evenPointer = 0;  // Pointer for even numbers (start)
//    	        int oddPointer = ar.length - 1;  // Pointer for odd numbers (end)
//
//    	        while (evenPointer <= oddPointer) {
//    	            // If evenPointer points to an odd number and oddPointer points to an even number, swap them
//    	            if (ar[evenPointer] % 2 != 0 && ar[oddPointer] % 2 == 0) {
//    	                int temp = ar[evenPointer];
//    	                ar[evenPointer] = ar[oddPointer];
//    	                ar[oddPointer] = temp;
//    	            }
//    	            
//    	            // Move the pointers towards each other
//    	            if (ar[evenPointer] % 2 == 0) evenPointer++;  // Even numbers move forward
//    	            if (ar[oddPointer] % 2 != 0) oddPointer--;  // Odd numbers move backward
//    	        }
//
//    	        // Print the result
//    	        Arrays.stream(ar).forEach(num -> System.out.print(num + " "));
//    	        
//    	        System.out.println();
//    	        
//    	     // Using streams to partition evens and odds
//    	        // Using streams to partition evens and odds
//    	        ar = Arrays.stream(ar)
//    	                   .boxed()  // Convert int[] to Integer[]
//    	                   .collect(Collectors.partitioningBy(i -> i % 2 != 0)) // Partition by even and odd
//    	                   .values()  // Get partitioned values
//    	                   .stream()  // Create a stream of lists
//    	                   .flatMap(List::stream)  // Flatten the lists back into a single stream
//    	                   .mapToInt(Integer::intValue)  // Convert back to primitive int
//    	                   .toArray();  // Collect back to array
//
//    	        // Print the result
//    	        Arrays.stream(ar).forEach(num -> System.out.print(num + " "));
//    	        Collectors.		

//    	        int even = 0;
//    	        int odd = ar.length - 1;
//
//    	        while (even < odd) {
//    	            // If the current `even` index is already even, move to the next index
//    	            if (ar[even] % 2 == 0) {
//    	                even++;
//    	            }
//    	            // If the current `odd` index is already odd, move to the previous index
//    	            else if (ar[odd] % 2 != 0) {
//    	                odd--;
//    	            }
//    	            // If `even` points to an odd number and `odd` points to an even number, swap
//    	            else {
//    	                int temp = ar[even];
//    	                ar[even] = ar[odd];
//    	                ar[odd] = temp;
//
//    	                even++;
//    	                odd--;
//    	            }
//    	        }
//
//    	        Arrays.stream(ar).forEach(i -> System.out.print(i + " "));
    	    
    	

    	  
    	  
//        String ar[] = {"B2", "C1", "B1" ,"A12"};
//        
//        Arrays.sort(ar,(a,b)->{
//        	
//        	int letterCompare = a.charAt(0) - b.charAt(0);
//        	if(letterCompare==0) {
//        		
//        		int num1 = Integer.parseInt(a.substring(1));
//        	    int num2 = Integer.parseInt(b.substring(1));	
//        	    
//        	    return num1-num2;
//        	}
//        	return letterCompare;
//        });
//       Arrays.asList(ar).stream().forEach(System.out::println);;
    }
}
//        Arrays.sort(ar,(a,b)->{
//    	int num1 = Integer.parseInt(a.substring(1));
//  	    int num2 = Integer.parseInt(b.substring(1));  
//    	
//    	if(num1==num2) {
//    		int letterCompare = a.charAt(0) - b.charAt(0);	
//    	    return letterCompare;
//    	}
//    		return num1-num2;
//        });
//        
//        
//        Arrays.stream(ar).forEach(System.out::println);
//        
//        for(String i: ar)
//        System.out.println(i);
        
        

//    }
//}

//https://www.geeksforgeeks.org/problems/n-digit-numbers-with-digits-in-increasing-order5903/1
//class Solution {
//    
//    public static ArrayList<Integer> increasingNumbers(int n) {
//        ArrayList<Integer> result = new ArrayList<>();
//        ArrayList<Integer> temp = new ArrayList<>();
//        if (n == 1) {
//            result.add(0);
//        }
//        
//        solve(n, 1, temp, result);
//        return result;
//    }
//    
//    private static void solve(int n, int start, ArrayList<Integer> path, ArrayList<Integer> result) {
//        if (path.size() == n) {
//            int curr = 0;
//            for (int num : path) {
//                curr = curr * 10 + num;
//            }
//            result.add(curr);
//            return;
//        }
//        
//        for (int i = start; i <= 9; i++) {
//            path.add(i);
//            solve(n, i + 1, path, result);
//            path.remove(path.size() - 1);
//        }
//    }
//}
	
