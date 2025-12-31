import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 테스트 케이스 개수 T 입력
        int T = sc.nextInt();
        
        // nextInt() 후 남은 개행 문자 제거
        sc.nextLine();

        for (int i = 0; i < T; i++) {
            String input = sc.nextLine();
            if (isValid(input)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
        
        sc.close();
    }

    /**
     * 괄호 문자열이 올바른지(VPS) 판단하는 함수
     */
    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == '(') {
                // 열린 괄호는 스택에 담음
                stack.push(ch);
            } else {
                // 닫힌 괄호가 나왔는데 스택이 비어있다면 올바르지 않은 괄호
                if (stack.isEmpty()) {
                    return false;
                }
                // 스택에 열린 괄호가 있다면 하나를 꺼냄 (짝 맞추기)
                stack.pop();
            }
        }

        // 모든 과정을 마친 후 스택이 비어있어야만 모든 괄호의 짝이 맞는 것
        return stack.isEmpty();
    }
}