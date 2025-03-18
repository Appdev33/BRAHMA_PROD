package DatStructuresStreams;

public class MiscAlgos {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String text = "ABABDABACDABABCABAB";
        String pattern = "ABABCABAB";

        KMPSearch(text, pattern);

	}
	
	
    public static int KMPSearch(String text, String pattern) {
        int[] lps = computeLPSArray(pattern);
        int i = 0; // Index for text
        int j = 0; // Index for pattern

        while (i < text.length()) {
            if (pattern.charAt(j) == text.charAt(i)) {
                i++;
                j++;
            }

            if (j == pattern.length()) {
                System.out.println("Found pattern at index " + (i - j));
                j = lps[j - 1]; // Use LPS to avoid unnecessary comparisons
            } else if (i < text.length() && pattern.charAt(j) != text.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1]; // Backtrack in the pattern
                } else {
                    i++;
                }
            }
        }

        return -1; // Pattern not found
    }

    // Function to compute the LPS array
    private static int[] computeLPSArray(String pattern) {
        int[] lps = new int[pattern.length()];
        int length = 0; // Length of the previous longest prefix suffix
        int i = 1; // LPS[0] is always 0

        while (i < pattern.length()) {
            if (pattern.charAt(i) == pattern.charAt(length)) {
                length++;
                lps[i] = length;
                i++;
            } else {
                if (length != 0) {
                    length = lps[length - 1]; // Backtrack
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }


}
