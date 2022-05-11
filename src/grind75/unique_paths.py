from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

    def uniquePaths_DP(self, m: int, n: int) -> int:

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == 0 and j == 0:
                return 1

            res = 0
            if i - 1 >= 0:
                res += dp(i - 1, j)
            if j-1 >= 0:
                res += dp(i, j - 1)
            return res

        return dp(m-1, n-1)

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths_DP(3, 2))
    print(s.uniquePaths_DP(7, 3))
