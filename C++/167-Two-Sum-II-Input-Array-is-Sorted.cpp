#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    /*
     * Two pointer approach, since our array is sorted...
     * TC: O(n), where n is the size of numbers
     * SC: O(1), no extra space is allocated
     */
    vector<int> twoSum(vector<int>& numbers, int target) {
      vector<int> results;

      int left_pointer = 0;                   // our left pointer that starts at the 0th index
      int right_pointer = numbers.size() - 1; // our right pointer that starts at the nth index

      while (left_pointer < right_pointer) {  // while our pointers do not overlap
        int sum = numbers[left_pointer] + numbers[right_pointer]; // calculate sum

        if (sum > target) {
          right_pointer -= 1; // move our right_pointer to the left to decrease sum
        } else if (sum < target) {
          left_pointer += 1;  // move our left_pointer to the right to increase sum
        } else {
          results.push_back(left_pointer + 1);
          results.push_back(right_pointer + 1);
          break;
        }
      }
      return results;
    }
};