import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		for(int i = 1; i <= n; i++) {
			int d = 0;
			while(d != i) {
				System.out.print("*");
				d++;
			}
			
			System.out.println();
		}
	}
}
