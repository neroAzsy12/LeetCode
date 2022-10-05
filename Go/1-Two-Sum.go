package Go

/**
* HashMap Approach, since our Array nums is not sorted
* TC: O(n), where n is the number of elements in nums
* SC: O(n), we could potentially add n elements in our hashmap
 */
func twoSum(nums []int, target int) []int {
	seenNums := make(map[int]int) // key: nums[index], value: index

	for index, currentNum := range nums {
		// checking if seenNums contains key (target - currentNum)
		if value, found := seenNums[target-currentNum]; found {
			// return indices of the two numbers that add up to target
			return []int{value, index}
		}
		seenNums[currentNum] = index
	}
	return []int{-1, -1}
}
