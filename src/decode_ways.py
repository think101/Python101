class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[0] = 1

        for i in range(1, len(s)+1):
            if i-1 < 0 and int(s[i-1:i]) in range(1, 27):
                dp[i] = 1
            elif i-1 >= 0 and int(s[i-1:i]) in range(1, 27) and dp[i-1] > 0:
                dp[i] += dp[i-1]

            if i-2 >= 0 and s[i-2:i-1] != '0' and int(s[i-2:i]) in range(1, 27) and dp[i-2] > 0:
                dp[i] += dp[i-2]

        return dp[len(s)]


t = Solution()
print(t.numDecodings("12"))
print(t.numDecodings("226"))
print(t.numDecodings("0"))

