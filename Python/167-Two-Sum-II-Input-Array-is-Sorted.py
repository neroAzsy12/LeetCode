from typing import List

class Solution(object):
    '''
      Two pointer approach, since our array is sorted...
        * TC: O(n)
        * SC: O(1)
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      left_pointer = 0                 # our left pointer that starts at the 0th index
      right_pointer = len(numbers) - 1 # our right pointer that starts at the nth index

      while left_pointer < right_pointer: # while our pointers do not overlap
        sum = numbers[left_pointer] + numbers[right_pointer]  # calculate sum

        if sum > target:
          right_pointer -= 1  # move our right_pointer to the left to decrease sum
        elif sum < target:
          left_pointer += 1   # move our left_pointer to the right to increase sum
        else:
          return [left_pointer + 1, right_pointer + 1]  # return the indices as our answer

      return [-1, -1]   # in the event we do not find two numbers that add to the target value
