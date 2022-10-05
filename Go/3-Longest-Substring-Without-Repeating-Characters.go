package Go

/*
Sliding Window

	TC: O(n), where n is the length of s
	SC: O(n), allocate extra space with our set, can potentially hold n elements
*/
func lengthOfLongestSubstring(s string) int {
	charSet := make(map[byte]bool) // treating a map as a set
	result := 0                    // stores longest substring of s that does not repeat chars
	left_pointer := 0              // left pointer to keep track of our sliding window left side
	right_pointer := 0             // right pointer to keep track of our sliding window right side

	for right_pointer < len(s) {
		for charSet[s[right_pointer]] { // while the char of our right_pointer is in our charSet
			delete(charSet, s[left_pointer]) // remove chars using our left pointer, till we remove s[right_pointer]
			left_pointer++                   // increment left pointer by 1 to move our sliding window
		}

		charSet[s[right_pointer]] = true                   // add the char to our charSet
		result = max(result, right_pointer-left_pointer+1) // update our longest substring if needed
		right_pointer++
	}

	return result
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
