import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();

        System.out.println(facto(T));
        sc.close();
    }

    public static int facto(int n) {
        if (n==0 || n==1) return 1;

        int num = 1;

        for (int i=2; i<=n; i++) {
            num *= i;
        }
        return num;
    }
}