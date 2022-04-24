class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        res = 0
        dp = [0 for _ in range(len(s))]  # dp[i] length of longest substr end at s[i]
        dp[0] = 1

        for i in range(1, len(s)):
            ss = s[i-dp[i-1]:i]
            t = ss.rfind(s[i])
            if t >= 0:
                dp[i] = dp[i-1] - t
            else:
                dp[i] = dp[i-1] + 1

            res = max(res, dp[i])

        return res

t = Solution()
print(t.lengthOfLongestSubstring("abcabcbb"))
print(t.lengthOfLongestSubstring("bbbbb"))
print(t.lengthOfLongestSubstring("pwwkew"))
print(t.lengthOfLongestSubstring(""))
print(t.lengthOfLongestSubstring(" "))

