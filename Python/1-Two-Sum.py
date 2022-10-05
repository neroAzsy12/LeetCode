from typing import List

class Solution:

  '''
  HashMap Approach, since our Array nums is not sorted
    * TC: O(n), where n is the number of elements in nums
    * SC: O(n), we could potentially add n elements in our hashmap
  '''
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    seenNums = {} # key: nums[index], value: index

    for index, val in enumerate(nums):
      difference = target - val
      # checking if seenNums contains key (difference)
      if difference in seenNums:
        # return indices of the two numbers that add up to target
        return [seenNums[difference], index]
      seenNums[val] = index

    return [-1, -1]