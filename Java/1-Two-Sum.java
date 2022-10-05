import java.util.*;
class Solution {

    /**
     * Refer to Two Sum II - Input Array Sorted for two pointer approach
     * HashMap Approach, since our Array nums is not sorted
     * TC: O(n), where n is the number of elements in nums
     * SC: O(n), we could potentially add n elements in our hashmap
     */
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seenNums = new HashMap<>();   // key: nums[index], value: index
        
        for (int i = 0; i < nums.length; i++) {
            if (seenNums.containsKey(target - nums[i])) {
                // return indices of the two numbers that add up to target
                return new int[] { seenNums.get(target - nums[i]), i };
            }
            seenNums.put(nums[i], i);
        }
        
        throw new IllegalArgumentException("No Two Sum solution");
    }
}
