from typing import List

class Solution:
  '''
  Two level Binary Search
   * TC: O(log m + log n), where m is the number of rows, and n is the number of elements per row
   * SC: O(1)
  '''
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # first perform binary search on the rows to find the designated row that target value may be in
    top = 0                   # top row
    bottom = len(matrix) - 1  # bottom row

    while top <= bottom:
      row = (top + bottom) // 2 # top + ((bottom - top) // 2)

      if target > matrix[row][-1]:
        top = row + 1     # if target is greater than the last element in matrix[row], ignore top rows
      elif target < matrix[row][0]:
        bottom = row - 1  # if target is less than the first element in matrix[row], ignore bottom rows
      else:
        break             # if target is between the first and last elements in matrix[row]
    
    if top > bottom:  # check if the top overlaps bottom
      return False
    
    # perform binary search on the designated matrix[row]
    row = (top + bottom) // 2  # recalculate the row that the target value may appear in 
    left = 0
    right = len(matrix[row]) - 1

    while left <= right:
      middle = (left + right) // 2  # left + (right - top) // 2

      if target > matrix[row][middle]:
        left = middle + 1
      elif target < matrix[row][middle]:
        right = middle - 1
      else:
        return True

    return False