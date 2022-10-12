class Solution {
  /*
    Greedy approach
    TC: O(n), where n is the length of s, and we go through each char in s
    SC: O(1), since we do not allocate extra space
  */
  public boolean checkValidString(String s) {
    int leftMin = 0, leftMax = 0; // open parenthesis count in range [leftMin, leftMax]

    for (int index = 0; index < s.length(); index++) {
      if (s.charAt(index) == '(') {
        leftMin++;
        leftMax++;
      } else if (s.charAt(index) == ')') {
        leftMin--;  
        leftMax--;
      } else {      // if s[index] == '*'
        leftMin--;  // if `*` become `)` leftMin--
        leftMax++;  // if `*` become `(` then leftMax++
        // if '*' becomes '', nothing changes
        // open count becomes in a new range [leftMin - 1, leftMax + 1]
      }

      if (leftMax < 0) return false;  // Currently, don't have enough open parenthesis to match close parenthesis

      if (leftMin < 0) leftMin = 0;   // needed since, we may get -1 due to a wildcard, making it invalid count
    }

    return leftMin == 0;  // return true if the minimum '(' we can have can reach 0
  }
}
