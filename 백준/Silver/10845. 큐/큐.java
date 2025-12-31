import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();

        Deque<Integer> deque = new ArrayDeque<>();

        for (int i=0; i<T; i++) {
            String s = sc.nextLine();

            if (s.startsWith("push")) {
                String[] parts = s.split(" ");
                int x = Integer.parseInt(parts[1]);
                deque.add(x);
            } else if (s.equals("pop")) {
                System.out.println(deque.isEmpty() ? -1 : deque.removeFirst());
            } else if (s.equals("size")) {
                System.out.println(deque.size());
            } else if (s.equals("empty")) {
                System.out.println(deque.isEmpty() ? 1 : 0);
            } else if (s.equals("front")) {
                System.out.println(deque.isEmpty() ? -1 : deque.getFirst());
            } else if (s.equals("back")) {
                System.out.println(deque.isEmpty() ? -1 : deque.getLast());
            }
        }

        sc.close();
    }
}