
/*
 * In an e-com website, there are some discounts going on for mobile phones, but it is available only for a limited set of phones. The website allows users to sort the discounted items by price. There is an option to do the sorting for the phones without any offers as well.  

A user should be allowed to see a combined list of both the categories, select a phone & see other options in the nearby price points. Devise an algorithm for the same, which takes the following inputs from the user 
two catalogues – both are sorted in ascending order of cost 
the selected phone 
how many items to be displayed in the proximity 

 */

import java.util.*;



public class KClosest {
	
	public static class Pair{
		int diff;
		int number;
		Pair(int diff,int number){
			this.diff=diff;
			this.number=number;
		}
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		int discount[] = {2,4,6,7,8,10};
		int nonDiscount[] = {1,3,5,7,8,10};
		
		int targetPrice = 10;
		int k = 5;
		
//		PriorityQueue<Pair> maxHeap = new PriorityQueue<>( (a, b) -> Integer.compare(b.diff, a.diff));
		PriorityQueue<Pair> maxHeap = new PriorityQueue<>( (a, b) -> b.diff - a.diff);



		for (int i : discount) {
		    maxHeap.add(new Pair(Math.abs(targetPrice - i), i));
		    if (maxHeap.size() > k) {
		        maxHeap.poll(); // Remove the element with the maximum difference if size exceeds k
		    }
		}
		for (int i : nonDiscount) {
		    maxHeap.add(new Pair(Math.abs(targetPrice - i), i));
		    if (maxHeap.size() > k) {
		        maxHeap.poll(); // Remove the element with the maximum difference if size exceeds k
		    }
		}
		
		List<Integer> res = new ArrayList();
		
		System.out.println(maxHeap.size());
		
		while(!maxHeap.isEmpty())
			res.add(maxHeap.poll().number);
		
		
		System.out.println(res);

	}

}


//import java.util.ArrayList;
//import java.util.List;
//
//public class MobileCatalog {
//
//    public static List<Integer> displayProximityItems(int[] discountedCatalog, int[] nonDiscountedCatalog, int selectedPhone, int proximityCount) {
//        List<Integer> result = new ArrayList<>();
//
//        // Find the index of the selected phone in the discounted catalog
//        int discountedIndex = binarySearch(discountedCatalog, selectedPhone);
//
//        // Find the index of the selected phone in the non-discounted catalog
//        int nonDiscountedIndex = binarySearch(nonDiscountedCatalog, selectedPhone);
//
//        // Display nearby items based on proximity in the discounted catalog
//        int i = discountedIndex - 1;
//        while (i >= 0 && discountedIndex - i <= proximityCount) {
//            result.add(discountedCatalog[i]);
//            i--;
//        }
//
//        i = discountedIndex;
//        while (i < discountedCatalog.length && i - discountedIndex < proximityCount) {
//            result.add(discountedCatalog[i]);
//            i++;
//        }
//
//        // Display nearby items based on proximity in the non-discounted catalog
//        i = nonDiscountedIndex - 1;
//        while (i >= 0 && nonDiscountedIndex - i <= proximityCount) {
//            result.add(nonDiscountedCatalog[i]);
//            i--;
//        }
//
//        i = nonDiscountedIndex;
//        while (i < nonDiscountedCatalog.length && i - nonDiscountedIndex < proximityCount) {
//            result.add(nonDiscountedCatalog[i]);
//            i++;
//        }
//
//        return result;
//    }
//
//    // Binary search to find the index of the selected phone in the catalog
//    private static int binarySearch(int[] catalog, int target) {
//        int low = 0, high = catalog.length - 1;
//
//        while (low <= high) {
//            int mid = low + (high - low) / 2;
//
//            if (catalog[mid] == target) {
//                return mid;
//            } else if (catalog[mid] < target) {
//                low = mid + 1;
//            } else {
//                high = mid - 1;
//            }
//        }
//
//        return -1; // If the target is not found
//    }
//
//    public static void main(String[] args) {
//        int[] discountedCatalog = {100, 200, 300, 400, 500};
//        int[] nonDiscountedCatalog = {150, 250, 350, 450, 550};
//        int selectedPhone = 300;
//        int proximityCount = 2;
//
//        List<Integer> result = displayProximityItems(discountedCatalog, nonDiscountedCatalog, selectedPhone, proximityCount);
//
//        System.out.println(result);
//    }
//}

