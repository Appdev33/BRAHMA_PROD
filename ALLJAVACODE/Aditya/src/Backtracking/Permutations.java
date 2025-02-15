package Backtracking;
import java.util.*;

public class Permutations {

	public static List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, new ArrayList<>(), result);
        return result;
    }
    
    private static void backtrack(int[] nums, List<Integer> tempList, List<List<Integer>> result) {
        if (tempList.size() == nums.length) {
            result.add(new ArrayList<>(tempList));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (tempList.contains(nums[i])) {
                continue;
            }
            tempList.add(nums[i]);
            backtrack(nums, tempList, result);
            tempList.remove(tempList.size() - 1);
        }
    }

    public static void main(String[] args) {

        int[] nums = {1, 2, 3};
        List<List<Integer>> permutations = permute(nums);
        for (List<Integer> permutation : permutations) {
            System.out.println(permutation);
        }
    }
}
