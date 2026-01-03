import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String base = sc.nextLine();
        String bomb = sc.nextLine();
        int bombLen = bomb.length();
        StringBuilder sb = new StringBuilder();

        for (int i=0; i<base.length(); i++) {
            sb.append(base.charAt(i));
            if (sb.length() >= bombLen && sb.charAt(sb.length()-1) == bomb.charAt(bombLen-1)) {
                boolean isEqual = true;
                for (int j=bombLen-1;j>=0;j--) {
                    if (sb.charAt(sb.length()-bombLen+j) != bomb.charAt(j)) {
                        isEqual = false;
                        break;
                    }
                }
                if (isEqual) {
                    sb.delete(sb.length()-bombLen,sb.length());
                }
            }
        }
        System.out.println(sb.length() == 0 ? "FRULA" : sb);
    }
}