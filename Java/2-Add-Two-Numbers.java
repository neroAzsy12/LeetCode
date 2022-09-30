// Definition for singly-linked list.
class ListNode {
  int val;
  ListNode next;
  ListNode() {}
  ListNode(int val) { this.val = val; }
  ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
  // TC: O(max(m, n)), where m is the number of nodes in l1, and n is the number of nodes in l2
  // SC: O(max(m, n))
  public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
      ListNode head = new ListNode(-1);   // the node that will be returned
      ListNode tmp = head;                // tmp node that references head but will be traversed

      int carry = 0;                      // the carry digit, ex) 9 + 2 = 11, carry = 1 since 9 + 2 >= 10

      while (l1 != null || l2 != null || carry != 0) {
          int sum = carry;                        // sum will start off with either 0 or 1
          sum = l1 != null ? sum + l1.val : sum;  // if the node l1 is not null, then add l1.val to sum
          sum = l2 != null ? sum + l2.val : sum;  // if the node 12 is not null, then add l2.val to sum

          if (sum >= 10) {    // if sum from (carry + l1.val + l2.val) >= 10
              sum -= 10;      // decrement sum by 10 so it can be < 10
              carry = 1;      // carry is equal to 1, to represent the carry over digit
          } else {
              carry = 0;      // carry is 0 since the sum < 10
          }

          tmp.next = new ListNode(sum);   // set tmp.next to a new node that will contain sum as its val
          tmp = tmp.next;                 // move to the next node which is the new node that was created

          l1 = l1 != null ? l1.next : null;   // move to the next node in l1 if there is a node after
          l2 = l2 != null ? l2.next : null;   // move to the next node in l2 if there is a node after
      }
      return head.next;
  }
}
