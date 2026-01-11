
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> ans = new ArrayList<>();

        for (int i=N; i>=1; i--) {
            ans.add(arr[i-1],i);
        }

        StringBuilder sb = new StringBuilder();
        for (int val: ans) {
            sb.append(val).append(" ");
        }
        System.out.println(sb);
    }
}