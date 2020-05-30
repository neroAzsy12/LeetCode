/**
 * @author azsy
 *
 * Implement strStr(). 
 * Return the index of the first occurrence of needle in haystack,
 * or -1 if needle is not part of haystack.
 */
public class Implement_strStr {
	
	public static void main(String[] args) {
		System.out.println(strStr("hello", "ll"));	// prints 2
		System.out.println(strStr("aaaaa", "bba")); // prints -1
		System.out.println(strStr("teheusn", ""));  // prints 0
		System.out.println(strStr("a", "a"));		// prints 0
		
	}
	
	public static int strStr(String haystack, String needle) {
		if(needle.equals("")) {
			return 0;	// for this problem, if needle is length of 0, it returns 0
		}else {
			for(int i = 0; i <= haystack.length() - needle.length(); i++) {
				if(haystack.substring(i, i + needle.length()).equals(needle)) {
					return i;	// returns the index of the first occurence of needle in the haystack
				}
			}
			return -1;			// returns -1 if not found in the haystack
		}
	}
}
