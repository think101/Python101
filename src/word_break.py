from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * len(s)

        for i in range(0, len(s)):
            if s[:i+1] in wordDict:
                dp[i] = 1
                continue

            for j in range(0, i):
                if dp[j] == 1 and s[j+1:i+1] in wordDict:
                    dp[i] = 1
                    continue

        return dp[len(s)-1]


t = Solution()
print(t.wordBreak("leetcode", ["leet", "code"]))
print(t.wordBreak("applepenapple", ["apple", "pen"]))
print(t.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))