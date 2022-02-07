import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int x = sc.nextInt();
		
		int [] ar = new int[10000];
		for(int i = 0; i < n; i++) {
			ar[i] = sc.nextInt();
		}
		
		for(int i = 0; i < n; i++) {
			if(ar[i] < x)
				System.out.print(ar[i] + " ");
		}
	}
}
