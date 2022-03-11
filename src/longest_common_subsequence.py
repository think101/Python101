class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        col, row = len(text1)+1, len(text2)+1
        dp = [[0 for x in range(col)] for y in range(row)]

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = max(dp[i-1][j-1]+1 if text1[j-1] == text2[i-1] else dp[i-1][j-1],
                               dp[i-1][j], dp[i][j-1])

        return dp[row-1][col-1]


t = Solution()
print(t.longestCommonSubsequence("abcde", "ace"))
print(t.longestCommonSubsequence("abc", "abc"))
print(t.longestCommonSubsequence("abc", "def"))

