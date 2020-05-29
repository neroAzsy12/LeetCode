/**
 * @author azsy
 *
 * Given a sorted array and a target value, 
 * return the index if the target is found. 
 * If not, return the index where it would be if it were inserted in order.
 * You may assume no duplicates in the array.
 */
public class Search_Insert_Position {
	public static void main(String[] args) {
		System.out.println(searchInsert1(new int[] {1, 3, 5, 6}, 5));	// prints 2
		System.out.println(searchInsert1(new int[] {1, 3, 5, 6}, 2));	// prints 1
		System.out.println(searchInsert1(new int[] {1, 3, 5, 6}, 7));	// prints 4
		System.out.println(searchInsert1(new int[] {1, 3, 5, 6}, 0));	// prints 0
		System.out.println(searchInsert1(new int[] {1, 3, 5, 6}, 6));	// prints 3
	}
	
	// solution #1
	public static int searchInsert(int[] nums, int target) {
		int index = 0;
		while(index < nums.length && target > nums[index]) {
			index++;
		}
		
		return index;
	}
	
	// solution #2
	public static int searchInsert1(int[] nums, int target) {
		for(int i = 0; i < nums.length; i++) {
			if(target <= nums[i]) {
				return i;
			}
		}
		return nums.length;
	}
}
