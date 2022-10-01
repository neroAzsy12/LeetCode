from typing import List

class Solution:
  '''
  Given an (N x N) matrix representing an image, rotate the image by 90 degrees (clockwise) 
    * Time: O(n^2), where n is the total number of cells in our n x n matrix
    * Space: O(1), no extra space is allocated
  '''
  def rotate(self, matrix: List[List[int]]) -> None:
    # First, we want to transpose the matrix
    for row in range(len(matrix[0])):
      for column in range(row + 1, len(matrix)):
        tmp = matrix[row][column]
        
        matrix[row][column] = matrix[column][row]
        matrix[column][row] = tmp

    # Second, we reverse each row in the matrix
    for row in range(len(matrix)):
      left = 0
      right = len(matrix[row]) - 1

      while left < right:
        tmp = matrix[row][left]

        matrix[row][left] = matrix[row][right]
        matrix[row][right] = tmp

        left += 1
        right -= 1