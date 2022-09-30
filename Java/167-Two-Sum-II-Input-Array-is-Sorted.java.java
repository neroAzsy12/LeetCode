class Solution {
    /**
     * Two pointer approach
     * TC: O(n), where n is the size of numbers
     * SC: O(1), no extra space is allocated
     */
    public int[] twoSumDifferent(int[] numbers, int target) {
        int left_pointer = 0;                   // our left pointer that starts at the 0th index
        int right_pointer = numbers.length - 1; // our right pointer that starts at the nth index

        int[] result = new int[]{-1, -1};

        while (left_pointer < right_pointer) {  // while our pointers do not overlap
            if (numbers[left_pointer] + numbers[right_pointer] > target) {
                right_pointer--;// move our right_pointer to the left to decrease sum
            } else if (numbers[left_pointer] + numbers[right_pointer] < target) {
                left_pointer++; // move our left_pointer to the right to increase sum
            } else {
                result[0] = left_pointer + 1;
                result[1] = right_pointer + 1;
                break;
            }
        }

        return result;  // return the indices as our answer
    }
}
