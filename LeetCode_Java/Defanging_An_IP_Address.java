/**
 * @author azsy
 *
 * Given a valid (IPv4) IP address, return a defanged version of that IP address.
 * A defanged IP address replaces every period "." with "[.]".
 */
public class Defanging_An_IP_Address {
	
	public static void main(String[] args) {
		System.out.println(defangIPaddr("1.1.1.1"));	 // 1[.]1[.]1[.]1
		System.out.println(defangIPaddr("255.100.50.0"));// 255[.]100[.]50[.]0
	}
	
	public static String defangIPaddr(String address) {
		StringBuilder sb = new StringBuilder();		// stringbuilder sb is used since it will constantly be changing
		
		for(int i = 0; i < address.length(); i++) {
			if(address.charAt(i) == '.') {
				sb.append("[.]");					// if the current char is '.' replace it with "[.]"
			}else {
				sb.append(address.charAt(i));		// if its any other char just append to the sb
			}
		}
		
		return sb.toString();						// returns sb as a string object
	}
}
