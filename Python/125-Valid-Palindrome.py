class Solution:
  '''
  Two Pointer Approach
    * TC: O(n), where n is the length of string s
    * SC: O(1), no extra space is allocated
  '''
  def isPalindrome(self, s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
      while left < right and not alphanum(s[left]): # checking to see if character is alphanumeric 
        left += 1
      
      while left < right and not alphanum(s[right]):# checking to see if character is alphanumeric 
        right -= 1
      
      if s[left].lower() != s[right].lower(): # checking to see if left and right chars are the same
        return False  # string s is not a palindrome
      
      left += 1
      right -= 1

    return True # string s is a palindrome

# checks for alphanumeric character c
def alphanum(c):
  return (
    ord("A") <= ord(c) <= ord("Z")
    or ord("a") <= ord(c) <= ord("z")
    or ord("0") <= ord(c) <= ord("9")
  )