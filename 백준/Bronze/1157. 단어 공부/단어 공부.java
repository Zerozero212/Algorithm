import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine().toUpperCase();

        int[] counts = new int[26];

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            counts[c - 'A']++;
        }

        int maxCount = -1; 
        char result = '?'; 

        for (int i = 0; i < 26; i++) {
            if (counts[i] > maxCount) {
                maxCount = counts[i]; 
                result = (char) ('A' + i); 
            } else if (counts[i] == maxCount) {
                result = '?'; 
            }
        }

        System.out.println(result);

        br.close();
    }
}