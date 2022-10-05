#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
  public:
    /*
     * TC: O(n), where n is the number of elements in nums
     * SC: O(n), we could potentially add n elements in our hashmap
     */
    vector<int> twoSum(vector<int>& nums, int target) {
      unordered_map<int, int> seenNums; // key: nums[index], value: index

      for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        // checking if seenNums contains key (compliment)
        if (seenNums.find(complement) != seenNums.end()) {
          // return indices of the two numbers that add up to target
          return {seenNums[complement], i};
        }
        seenNums.insert({nums[i], i});
      }

      return {-1, -1};
    }
};