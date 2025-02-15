package DP;

import java.util.*;

public class EvaluateExpression {

	    private static final Map<String, Integer> memoizationMap = new HashMap<>();
	    
	    public static void main(String[] args) {
	        char[] expression1 = {'T', '|', 'F', '&', 'T', '^', 'T'};
	        char[] expression2 = {'T', '^', 'F', '&', 'T'};
	
	        int result1 = EvaluateExpressionRecursive(expression1, 0, expression1.length - 1, true);
	        int result2 = EvaluateExpressionRecursive(expression2, 0, expression2.length - 1, true);
	
	        System.out.println("Number of ways to evaluate the expression 1 to true: " + result1);
	        System.out.println("Number of ways to evaluate the expression 2 to true: " + result2);
	    }
    

	    public static int EvaluateExpressionRecursive(char[] S, int i, int j, boolean isTrue) {
	        if (i > j) {
	            return 0;
	        }

	        if (i == j) {
	            if (isTrue) {
	                return (S[i] == 'T') ? 1 : 0;
	            } else {
	                return (S[i] == 'F') ? 1 : 0;
	            }
	        }

	        int count = 0;
	        for (int k = i + 1; k < j; k += 2) {
	            int LT = EvaluateExpressionRecursive(S, i, k - 1, true);
	            int LF = EvaluateExpressionRecursive(S, i, k - 1, false);
	            int RT = EvaluateExpressionRecursive(S, k + 1, j, true);
	            int RF = EvaluateExpressionRecursive(S, k + 1, j, false);

	            if (S[k] == '&') {
	                if (isTrue) {
	                    count += LT * RT;
	                } else {
	                    count += LT * RF + LF * RT + LF * RF;
	                }
	            } else if (S[k] == '|') {
	                if (isTrue) {
	                    count += LT * RF + LF * RT + LT * RT;
	                } else {
	                    count += LF * RF;
	                }
	            } else if (S[k] == '^') {
	                if (isTrue) {
	                    count += LT * RF + LF * RT;
	                } else {
	                    count += LT * RT + LF * RF;
	                }
	            }
	        }

	        return count;
	    }

	    




	        public static int EvaluateExpressionMemo(char[] S, int i, int j, boolean isTrue) {
	            if (i > j) {
	                return 0;
	            }

	            if (i == j) {
	                if (isTrue) {
	                    return (S[i] == 'T') ? 1 : 0;
	                } else {
	                    return (S[i] == 'F') ? 1 : 0;
	                }
	            }

	            String key = i + "|" + j + "|" + isTrue;
	            if (memoizationMap.containsKey(key)) {
	                return memoizationMap.get(key);
	            }

	            int count = 0;
	            for (int k = i + 1; k < j; k += 2) {
	                int LT = EvaluateExpressionMemo(S, i, k - 1, true);
	                int LF = EvaluateExpressionMemo(S, i, k - 1, false);
	                int RT = EvaluateExpressionMemo(S, k + 1, j, true);
	                int RF = EvaluateExpressionMemo(S, k + 1, j, false);

	                if (S[k] == '&') {
	                    if (isTrue) {
	                        count += LT * RT;
	                    } else {
	                        count += LT * RF + LF * RT + LF * RF;
	                    }
	                } else if (S[k] == '|') {
	                    if (isTrue) {
	                        count += LT * RF + LF * RT + LT * RT;
	                    } else {
	                        count += LF * RF;
	                    }
	                } else if (S[k] == '^') {
	                    if (isTrue) {
	                        count += LT * RF + LF * RT;
	                    } else {
	                        count += LT * RT + LF * RF;
	                    }
	                }
	            }

	            memoizationMap.put(key, count);
	            return count;
	        }    
}


/*
import java.util.Scanner;

public class BooleanExpression {

    private static final int MOD = 1003;
    private static int[][][] dp;

    private static int solve(String s, int i, int j, boolean isTrue) {
        if (i > j) return 0;
        if (dp[i][j][isTrue] != -1) return dp[i][j][isTrue];

        if (i == j) {
            if (isTrue)
                return (s.charAt(i) == 'T') ? 1 : 0;
            else
                return (s.charAt(i) == 'F') ? 1 : 0;
        }

        int ans = 0;
        for (int k = i + 1; k < j; k += 2) {
            if (dp[i][k - 1][1] == -1)
                dp[i][k - 1][1] = solve(s, i, k - 1, true);
            if (dp[i][k - 1][0] == -1)
                dp[i][k - 1][0] = solve(s, i, k - 1, false);
            if (dp[k + 1][j][1] == -1)
                dp[k + 1][j][1] = solve(s, k + 1, j, true);
            if (dp[k + 1][j][0] == -1)
                dp[k + 1][j][0] = solve(s, k + 1, j, false);

            if (s.charAt(k) == '&') {
                if (isTrue)
                    ans = (ans + (dp[k + 1][j][1] * dp[i][k - 1][1]) % MOD) % MOD;
                else
                    ans = (ans + ((dp[k + 1][j][1] * dp[i][k - 1][0]) % MOD +
                                  (dp[k + 1][j][0] * dp[i][k - 1][1]) % MOD +
                                  (dp[k + 1][j][0] * dp[i][k - 1][0]) % MOD) % MOD) % MOD;
            } else if (s.charAt(k) == '|') {
                if (isTrue)
                    ans = (ans + ((dp[k + 1][j][1] * dp[i][k - 1][0]) % MOD +
                                  (dp[k + 1][j][0] * dp[i][k - 1][1]) % MOD +
                                  (dp[k + 1][j][1] * dp[i][k - 1][1]) % MOD) % MOD) % MOD;
                else
                    ans = (ans + (dp[k + 1][j][0] * dp[i][k - 1][0]) % MOD) % MOD;
            } else if (s.charAt(k) == '^') {
                if (isTrue)
                    ans = (ans + ((dp[k + 1][j][1] * dp[i][k - 1][0]) % MOD +
                                  (dp[k + 1][j][0] * dp[i][k - 1][1]) % MOD) % MOD) % MOD;
                else
                    ans = (ans + ((dp[k + 1][j][1] * dp[i][k - 1][1]) % MOD +
                                  (dp[k + 1][j][0] * dp[i][k - 1][0]) % MOD) % MOD) % MOD;
            }
        }

        dp[i][j][isTrue] = ans % MOD;
        return ans % MOD;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            int n = scanner.nextInt();
            dp = new int[2 * n][2 * n][2];
            for (int i = 0; i < 2 * n; i++) {
                for (int j = 0; j < 2 * n; j++) {
                    for (int k = 0; k < 2; k++) {
                        dp[i][j][k] = -1;
                    }
                }
            }

            String booleanExpression = scanner.next();
            System.out.println(solve(booleanExpression, 0, 2 * n - 1, true));
        }
    }
}

*/

