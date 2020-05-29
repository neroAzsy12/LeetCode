/**
 * @author azsy
 * 
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 */
import java.util.*;
public class Two_Sum {
	public static void main(String[] args) {
		ArrayList<int[]> tests = new ArrayList<>();
		
		tests.add(twoSum(new int[] {2, 7, 11, 15}, 9));		// prints [0, 1]
		tests.add(twoSum(new int[] {1, 5, 9, 11, 30}, 39)); // prints [2, 4]
		tests.add(twoSum(new int[] {-10, 0, 1, 3, 10}, 0)); // prints [0, 4]
		for(int[] t : tests) {
			for(int val : t) {
				System.out.print(val + " ");
			}
			System.out.println();
		}
	}
	
	public static int[] twoSum(int[] nums, int target) {
		HashMap<Integer, Integer> map = new HashMap<>();	// HashMap will hold (complement, index)
		
		for(int i = 0; i < nums.length; i++) {
			int complement = target - nums[i];				// complement is the difference between the target and nums[i]
			
			if(map.containsKey(complement)) {
				return new int[] {map.get(complement), i};	// returns the indices that makes up the target
			}
			map.put(nums[i], i);							// adds (nums[i], and its index) to the map
		}
		throw new IllegalArgumentException("No solution");	// throws exception if no solution is found
	}
}
