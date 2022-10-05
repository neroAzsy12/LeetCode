package Go

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// TC: O(max(m, n)), where m is the number of nodes in l1, and n is the number of nodes in l2
// SC: O(max(m,n))
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	head := new(ListNode)
	var carry = 0 // carry will contain only either 0 or 1, at the end of each iteration

	for tmp := head; l1 != nil || l2 != nil || carry != 0; tmp = tmp.Next {
		if l1 != nil {
			carry += l1.Val // if the node l1 is not null, then add l1.Val to carry
			l1 = l1.Next    // if the node l1 is not null, move to the next node in l1
		}

		if l2 != nil {
			carry += l2.Val // if the node l2 is not null, then add l2.Val to carry
			l2 = l2.Next    // if the node l2 is not null, move to the next node in l2
		}

		tmp.Next = &ListNode{Val: carry % 10} // set tmp.Next to a new node that will contain carry % 10 as its val
		carry /= 10                           // decrement sum by 10 so it can be < 10
	}

	return head.Next
}
