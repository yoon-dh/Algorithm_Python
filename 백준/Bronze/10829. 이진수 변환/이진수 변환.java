import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long n = Long.parseLong(sc.nextLine());
		
		ArrayList<Long> arr = new ArrayList<>();
		
		for (int i = 0; 0 < n; i++) {
			long temp = n % 2;
			n /= 2;
			arr.add(temp);
		}
		
		Collections.reverse(arr);
		
		for (long i:arr) {
			System.out.print(i);
		}
		
	}

}
