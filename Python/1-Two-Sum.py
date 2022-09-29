from typing import List

class Solution:

  '''
  HashMap Approach, since our Array nums is not sorted
    * TC: O(n), where n is the number of elements in nums
    * SC: O(n), we could potentially add n elements in our hashmap
  '''
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    previousMap = {}  # key: val, value: index

    for index, val in enumerate(nums):
      difference = target - val

      if difference in previousMap:
        return [previousMap[difference], index]
      previousMap[val] = index

    return [-1, -1]