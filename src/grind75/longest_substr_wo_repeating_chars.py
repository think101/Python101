class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        dp = {}

        i, j, res = 0, 0, 0
        dp[s[i]] = 0

        for j in range(1, len(s)):
            if s[j] in dp:
                t = dp[s[j]]
                for k in range(i, t + 1):
                    dp.pop(s[k], None)
                dp[s[j]] = j
                res = max(res, j - t)
                i = t + 1
            else:
                dp[s[j]] = j
                res = max(res, j - i + 1)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
