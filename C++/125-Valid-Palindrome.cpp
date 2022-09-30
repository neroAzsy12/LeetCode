#include <iostream>
#include <cctype>
#include <string>
using namespace std;

class Solution {
  public:
    /**
     * Two Pointer Approach
     * TC: O(n), where n is the length of string s
     * SC: O(1), no extra space is allocated
     */
    bool isPalindrome(string s) {
      int left = 0;             // left pointer
      int right = s.size() - 1; // right pointer

      while (left < right) {
        while (!isalnum(s[left]) && left < right) { // checking to see if character is alphanumeric 
          left++;
        }
        while (!isalnum(s[right]) && left < right) {// checking to see if character is alphanumeric 
          right--;
        }
        if (tolower(s[left]) != tolower(s[right])) {// checking to see if left and right chars are the same
          return false; // string s is not a palindrome
        }
        left++;
        right--;
      }

      return true;  // string s is a palindrome
    }
};