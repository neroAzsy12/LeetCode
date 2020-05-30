/**
 * @author azsy
 *
 * Given a 32-bit signed integer, reverse digits of an integer.
 */
public class Reverse_Integer {
	public static void main(String[] args) {
		System.out.println(reverse(-123));	// prints -321
		System.out.println(reverse(123));	// prints 321
		System.out.println(reverse(120));	// prints 21
	}
	
	public static int reverse(int x) {
		int temp = x > 0 ? x : -x;			// temp = x if x > 0 or -x if x < 0
		
		long z = 0; 						// z is the value that will be returned
		
		while(temp > 0) {					// while temp > 0
			z = (z * 10) + (temp % 10);		// z is  z * 10 + the last digit of temp
			temp /= 10;						// temp is divided by 10 to get the next digit
		}
		
		if(z > Integer.MAX_VALUE) {
			return 0;						// if z is bigger than a 32-bit int, return 0
		}else {
			return x > 0 ? (int)z : (int)-z;// else return z if x > 0, or -z if x < 0
		}
	}
}
