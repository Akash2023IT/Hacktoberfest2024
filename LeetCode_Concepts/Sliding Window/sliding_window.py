import java.util.HashMap;
import java.util.Scanner;

public class LongestSubstringKDistinct {
    public static int findLength(String str, int k) {
        int start = 0;
        int maxLen = 0;
        HashMap<Character, Integer> freqMap = new HashMap<>();

        for (int end = 0; end < str.length(); end++) {
            char endChar = str.charAt(end);
            freqMap.put(endChar, freqMap.getOrDefault(endChar, 0) + 1);

            while (freqMap.size() > k) {
                char startChar = str.charAt(start);
                freqMap.put(startChar, freqMap.get(startChar) - 1);
                if (freqMap.get(startChar) == 0) {
                    freqMap.remove(startChar);
                }
                start++;
            }

            maxLen = Math.max(maxLen, end - start + 1);
        }

        return maxLen;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the string: ");
        String str = scanner.nextLine();

        System.out.print("Enter the value of K: ");
        int k = scanner.nextInt();

        int result = findLength(str, k);
        System.out.println("Length of the longest substring with " + k + " distinct characters: " + result);
    }
}
