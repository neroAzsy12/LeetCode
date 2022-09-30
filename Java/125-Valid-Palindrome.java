class Solution {
  private boolean isAlphaNumeric(char c) {
    return ( 
      (c - 'a' >= 0 && c - 'a' <= 25) || // checks between a-z
      (c - 'A' >= 0 && c - 'A' <= 25) || // checks between A-Z
      (c - '0' >= 0 && c - '0' <= 9)
    );   // checks between 0-9
  }

  /**
   * Two Pointer Approach
   * TC: O(n), where n is the length of string s
   * SC: O(1), no extra space is allocated
   */
  public boolean isPalindrome(String s) {
    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
      while (left < right && !isAlphaNumeric(s.charAt(left))) {
        left++;
      }

      while (left < right && !isAlphaNumeric(s.charAt(right))) {
        right--;
      }
      
      if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
        return false;
      }
      left++;
      right--;
    }
    
    return true;
  }
}
