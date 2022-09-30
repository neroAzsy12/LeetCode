from typing import List
class Solution:
  def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
      middle = left + ((right - left) // 2)

      # check if target is located in the middle
      if (nums[middle] == target): return middle

      # if target is greater, ingnore left half
      elif (nums[middle] < target): left = middle + 1
      
      # if target is smaller, ignore right half
      else: right = middle - 1

    # if we reach here, then the target element was not present
    return -1