import java.util.HashMap;
import java.util.Map;

public class TestingJava {

	    public static void main(String[] args) {
	    	
//	    	https://leetcode.com/problems/binary-search/solutions/423162/binary-search-101-by-aminick-kkch/
	    	
//	    	String s = "helper";
//	    	
//	        for (int i = 1; i <= s.length(); i++) 
//	            // Check for every possible substring that ends at i
//	            for (int j = 0; j < i; j++) 
//	    			System.out.println(s.substring(j,i));
	    				
	        // Example array
//	        int[] array = {2, 3, 2, 4, 5, 5, 5, 4, 3, 2,7,8,9,10,7};
//
//	        // Step 1: Count frequencies of elements
//	        Map<Integer, Integer> frequencyMap = new HashMap<>();
//	        for (int num : array) {
//	            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
//	        }
//	        
//	        System.out.println(frequencyMap);
//
//	        // Step 2: Count the frequencies of the frequencies
//	        Map<Integer, Integer> frequencyOfFrequencies = new HashMap<>();
//	        for (int freq : frequencyMap.values()) {
//	            frequencyOfFrequencies.put(freq, frequencyOfFrequencies.getOrDefault(freq, 0) + 1);
//	        }
//
//	        // Display the result
//	        System.out.println("Frequency of frequencies:");
//	        for (Map.Entry<Integer, Integer> entry : frequencyOfFrequencies.entrySet()) {
//	            System.out.println("Frequency: " + entry.getKey() + ", Count: " + entry.getValue());
//	        }
	    	
	    	
//	    	int[] nums = {2, 3, 2, 4, 5, 5, 5, 4, 3, 2,7,8,9,10,7};
//	    	
//	    	int maxNumber = 0;
//	        
//	        // Find the maximum number in the array to set the frequency array size
//	        for(int i: nums) {
//	            maxNumber = Math.max(i, maxNumber);
//	        }
//
//	        int n = nums.length;
//	        int frequency[] = new int[maxNumber + 1]; // element -> frequency
//	        int countFrequency[] = new int[n + 1]; // frequency -> count of frequency
//	        
//	        int resMax = 0;
//	        int countUniqueFrequency = 0; // Count of unique frequencies
//	        
//	        int minFreq = Integer.MAX_VALUE;
//	        int maxFreq = 0;
//	        
//	        // Initialize resMax as 1 (since any array can have at least one element with equal frequency)
//	        resMax = 1;
//	        
//	        // Loop through the array to calculate frequencies
//	        for(int i = 0; i < n; i++) {
//	            int currFrequency = ++frequency[nums[i]]; // Update frequency of current number
//	            
//	            // If this frequency was not seen before, increment the unique frequency count
//	            if(countFrequency[currFrequency]++ == 0) {
//	                countUniqueFrequency++;
//	            }
//
//	            // If the current frequency becomes greater than 1, decrement the previous frequency
//	            if(currFrequency > 1 && countFrequency[currFrequency - 1]-- == 1) {
//	                countUniqueFrequency--;
//	                if(minFreq == currFrequency - 1) {
//	                    minFreq++;
//	                }
//	            }
//
//	            maxFreq = Math.max(maxFreq, currFrequency); // Update max frequency
//	            minFreq = Math.min(minFreq, currFrequency); // Update min frequency
//	            
//	            // Case 1: All elements have the same frequency (valid subarray)
//	            if(countUniqueFrequency == 1 && (maxFreq == 1 || countFrequency[maxFreq] == 1)) {
//	                resMax = Math.max(resMax, i + 1); // Update result with current subarray length
//	            }
//	            
//	            // Case 2: Two unique frequencies
//	            if(countUniqueFrequency == 2) {
//	                // Case 2.1: One frequency is 1 (element can be removed), or the other frequency is 1 less than maxFreq
//	                if(countFrequency[1] == 1 || (countFrequency[maxFreq] == 1 && maxFreq == minFreq + 1)) {
//	                    resMax = Math.max(resMax, i + 1); // Update result with current subarray length
//	                }
//	            }
//	        }
//
//	        System.out.println(resMax);
	    	
	    	

	    }
	}
