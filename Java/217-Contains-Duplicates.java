import java.util.*;

public class Solution {
  /*
   * TC: O(n), where n is the number of elements in nums
   * SC: O(n), since we need to allocate a set that can be nums.size()
   */
  public boolean containsDuplicate(int[] nums) {
    Set<Integer> unique = new HashSet<>();
        
    for (int num : nums) {
      if (unique.contains(num)) {
        return true;
      }
      unique.add(num);
    }

    return false;
  }
}
