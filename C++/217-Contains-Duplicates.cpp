#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
  public:
    /*
    TC: O(n), where n is the number of elements in nums
    SC: O(n), since we need to allocate a set that can be nums.size()
    */
    bool containsDuplicate(vector<int>& nums) {
      unordered_set<int> unique;

      for (int i = 0; i < nums.size(); i++) {
        if (unique.find(nums[i]) != unique.end()) { // if nums[i] is in unique
          return true;
        }

        unique.insert(nums[i]);
      }

      return false;
    }
};