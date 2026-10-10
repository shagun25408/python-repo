#include <stdio.h>
#include <string.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int longest_common_subsequence_length(char *str1, char *str2) {
    int m = strlen(str1);
    int n = strlen(str2);

    // Create a 2D array to store the lengths of LCS
    int dp[m + 1][n + 1];

    // Build the dp array
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if (str1[i - 1] == str2[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    // The length of the LCS is found in dp[m][n]
    return dp[m][n];
}

int main() {
    char str1[] = "ABCBDAB";
    char str2[] = "BDCAB";

    int lcs_length = longest_common_subsequence_length(str1, str2);
    printf("Length of Longest Common Subsequence: %d\n", lcs_length);

    return 0;
}

