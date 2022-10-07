from typing import List

class Solution:
  '''
  Hashset, Array
  TC: O(n), where n is the number of elements in nums
  SC: O(n), since we need to allocate a set that can be nums.size()
  '''
  def containsDuplicate(self, nums: List[int]) -> bool:
    unique = set()  # our hashset

    for num in nums:
      if num in unique:
        return True
      unique.add(num)
    
    return False