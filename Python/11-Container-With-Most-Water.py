from typing import List

class Solution:
  '''
  Two Pointer Approach
    TC: O(n), we are iterating the entire height list
    SC: O(1), no extra space is allocated
  '''
  def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    result = 0

    while left < right:
      containerLength = right - left  # calculate length from right and left pointer
      area = containerLength * min(height[left], height[right]) # use min height to calculate the area
      result = max(result, area)      # keep track of the most water a container can store

      if height[left] < height[right]:
        left += 1   # increment left_pointer, if height[left] is smaller
      else:
        right -= 1  # incremeent right_pointer, if height[right] is smaller
    
    return result