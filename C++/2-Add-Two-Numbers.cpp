#include <iostream>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    // TC: O(max(m, n)), where m is the number of nodes in l1, and n is the number of nodes in l2
    // SC: O(max(m,n))
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      ListNode* head = new ListNode();
      ListNode* tmp = head;

      int carry = 0;

      while (l1 != NULL || l2 != NULL || carry != 0) {
        int sum = carry;                        // sum will start off with either 0 or 1
        sum = l1 != NULL ? sum + l1->val : sum; // if the node l1 is not null, then add l1.val to sum
        sum = l2 != NULL ? sum + l2->val : sum; // if the node 12 is not null, then add l2.val to sum

        if (sum >= 10) {  // if sum from (carry + l1.val + l2.val) >= 10
          sum -= 10;      // decrement sum by 10 so it can be < 10
          carry = 1;      // carry is equal to 1, to represent the carry over digit
        } else {
          carry = 0;      // carry is 0 since the sum < 10
        }

        tmp->next = new ListNode(sum);  // set tmp.next to a new node that will contain sum as its val
        tmp = tmp->next;                // move to the next node which is the new node that was created

        l1 = l1 != NULL ? l1->next : NULL;  // move to the next node in l1 if there is a node after
        l2 = l2 != NULL ? l2->next : NULL;  // move to the next node in l2 if there is a node after
      }
      return head->next;
    }
};