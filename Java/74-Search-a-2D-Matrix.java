public class Solution {

    /**
     * TC: O(log (mn)), where m is the number of rows, and n is the number of elements per row
     * @param matrix, integer matrix of m x n
     * @param target, value target
     * @return if the target value exists in the matrix
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // first perform binary search on the rows to find the designated row that target value may be in
        int top = 0;                        // top row
        int bottom = matrix.length - 1;     // bottom row

        while (top <= bottom) {
            int row = (top + bottom) / 2;   // middle row between top and bottom rows, top + (bottom - top) / 2

            if (target > matrix[row][matrix[0].length - 1]) {
                top = row + 1;              // if target is greater than the last element in matrix[row], ignore top rows
            } else if (target < matrix[row][0]) {
                bottom = row - 1;           // if target is less than the first element in matrix[row], ignore bottom rows
            } else {
                break;                      // if target is between the first and last elements in matrix[row], 
            }
        }
        
        // check if the top is smaller than bottom
        if (top > bottom) {
            return false;
        }

        // perform binary search on the designated matrix[row]
        int row = (top + bottom) / 2;       // recalculate the row that the target value may appear in, top + (bottom - top) / 2

        int left = 0;
        int right = matrix[row].length;

        while (left <= right) {
            int middle = (left + right) / 2;// left + (right - top) / 2

            if (target > matrix[row][middle]) {
                left = middle + 1;
            } else if (target < matrix[row][middle]) {
                right = middle - 1;
            } else {
                return true;
            }
        }

        return false;
    }
}
