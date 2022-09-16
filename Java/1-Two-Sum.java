import java.util.*;
class Solution {

    /**
     * Refer to Two Sum II - Input Array Sorted for two pointer approach
     * HashMap Approach, since our Array nums is not sorted
     * TC: O(n), where n is the number of elements in nums
     * SC: O(n), we could potentially add n elements in our hashmap
     */
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> compliment = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (compliment.containsKey(target - nums[i])) {
                return new int[] { compliment.get(target - nums[i]), i };   // stores the pair: difference from target and nums[i], and the ith index
            }
            compliment.put(nums[i], i);
        }
        
        throw new IllegalArgumentException("No Two Sum solution");
    }
}
