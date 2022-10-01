class Solution {
  /**
   * Given an (N x N) matrix representing an image, rotate the image by 90 degrees (clockwise)
   * 
   * Time: O(n^2), where n is the total number of cells in our n x n matrix
   * Space: O(1), no extra space is allocated
   */
  public void rotate(int[][] matrix) {
    // First, we want to transpose the matrix
    for (int row = 0; row < matrix[0].length; row++) {
      for (int column = row + 1; column < matrix.length; column++) {
        int tmp = matrix[row][column];
        
        matrix[row][column] = matrix[column][row];
        matrix[column][row] = tmp;
      }
    }

    // Second, we reverse each row in the matrix
    for (int row = 0; row < matrix.length; row++) {
      int left = 0;
      int right = matrix[row].length - 1;

      while (left < right) {
        int tmp = matrix[row][left];
        matrix[row][left] = matrix[row][right];
        matrix[row][right] = tmp;

        left++;
        right--;
      }
    }
  }
}
