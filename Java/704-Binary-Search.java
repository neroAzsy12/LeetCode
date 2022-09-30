class Solution {
  /**
   * Binary Search Algorithm
   * TC: O(log n), where n is the number of elements in nums
   * SC: O(1), no extra space is allocated
   */
  public int search(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;

    while (left <= right) {
      int middle = (left + right) / 2;  // int middle = left + (right - left) / 2;

      // check if target is located in the middle
      if (nums[middle] == target) return middle;

      // if target is greater, ingnore left half
      else if (nums[middle] < target) left = middle + 1;
      
      // if target is smaller, ignore right half
      else right = middle - 1;
    }

    // if we reach here, then the target element was not present
    return -1;
  }
}
