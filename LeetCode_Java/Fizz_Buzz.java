/**
 * @author azsy
 * 
 * Write a program that outputs the string representation of numbers from 1 to n.
 * But for multiples of three it should output “Fizz” instead of the number, 
 * and for the multiples of five output “Buzz”. 
 * 
 * For numbers which are multiples of both three and five output “FizzBuzz”.
 */
import java.util.*;
public class Fizz_Buzz {
	public static void main(String[] args) {
		List<String> tests = fizzBuzz(15);
		for(String val : tests) {
			System.out.println(val);
		}
	}
	
	public static List<String> fizzBuzz(int n){
		ArrayList<String> fizz = new ArrayList<>();
		for(int i = 1; i <= n; i++) {
			if(i % 3 == 0 && i % 5 == 0) {	// if i is divisible by both 3 & 5, append FizzBuzz
				fizz.add("FizzBuzz");
			}else if(i % 3 == 0) {			// if i is only divisible by 3, append Fizz
				fizz.add("Fizz");
			}else if(i % 5 == 0) {
				fizz.add("Buzz");			// if i is only divisible by 5, append Buzz
			}else {
				fizz.add(String.valueOf(i));// else just append i since it is not divisble by either both 3 or 5
			}
		}
		return fizz;						// returns the arraylist
	}
}
