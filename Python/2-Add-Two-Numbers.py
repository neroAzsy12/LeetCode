# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution(object):
  """
  TC: O(max(m, n)), where m is the number of nodes in l1, and n is the number of nodes in l2
  SC: O(max(m, n))
  
  :type l1: ListNode
  :type l2: ListNode
  :rtype: ListNode
  """
  def addTwoNumbers(self, l1, l2):
    head = ListNode()
    tmp = head

    carry = 0

    while l1 or l2 or carry:
      sum = carry;                      # sum will start off with either 0 or 1
      sum = sum + l1.val if l1 else sum # if the node l1 is not null, then add l1.val to sum
      sum = sum + l2.val if l2 else sum # if the node 12 is not null, then add l2.val to sum

      if (sum >= 10):   # if sum from (carry + l1.val + l2.val) >= 10
        sum -= 10;      # decrement sum by 10 so it can be < 10
        carry = 1;      # carry is equal to 1, to represent the carry over digit
      else:
        carry = 0;      # carry is 0 since the sum < 10
      
      tmp.next = ListNode(sum)  # set tmp.next to a new node that will contain sum as its val
      tmp = tmp.next;           # move to the next node which is the new node that was created

      l1 = l1.next if l1 else None  # move to the next node in l1 if there is a node after
      l2 = l2.next if l2 else None  # move to the next node in l2 if there is a node after
    
    return head.next