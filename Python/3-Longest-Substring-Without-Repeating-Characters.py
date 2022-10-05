class Solution:
  '''
  Sliding Window
    TC: O(n), where n is the length of s
    SC: O(n), allocate extra space with our set, can potentially hold n elements
  '''
  def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()   # set to keep track of chars that are visited in our sliding window
    left_pointer = 0  # left pointer to keep track of our sliding window left side
    result = 0        # stores longest substring of s that does not repeat chars

    for right_pointer in range(len(s)):
      while s[right_pointer] in charSet:# while the char of our right_pointer is in our charSet
        charSet.remove(s[left_pointer]) # remove chars using our left pointer, till we remove s[right_pointer]
        left_pointer += 1               # increment left pointer by 1 to move our sliding window

      charSet.add(s[right_pointer])     # add the char to our charSet
      result = max(result, right_pointer - left_pointer + 1)  # update our longest substring if needed

    return result