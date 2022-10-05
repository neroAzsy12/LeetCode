class Solution:
  '''
  Greedy approach
  TC: O(n), where n is the length of s, and we go through each char in s
  SC: O(1), since we do not allocate extra space
  '''
  def checkValidString(self, s: str) -> bool:
    leftMin = 0 # will keep track of min open left parenthesis we can have '('
    leftMax = 0 # will keep track of max open left parenthesis we can have '('

    for char in s:
      if char == '(':   # we want to increment both leftMin and leftMax since we are looking at an '('
        leftMin += 1
        leftMax += 1
      elif char == ')': # we want to decrement both leftMin and leftMax since we are looking at an ')'
        leftMin -= 1
        leftMax -= 1
      else:             # since '*' is a wildcard, we want leftMin to decrement, and we want leftMax to increment
        leftMin -= 1    # we want to assume best case of wildcard which is ')', refer to if
        leftMax += 1    # we want to assume worst case of wildcard which is '(', refer to else if
      
      if leftMax < 0:   
        return False    # in case we have more right parenthesis, and it doesn't correspond to a left parenthesis
      if leftMin < 0:   # needed since, we may get -1 due to a wildcard
        leftMin = 0
    
    return leftMin == 0 # return true if the minimum '(' we can have reaches 0