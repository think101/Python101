from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        for i in range(len(s)):
            t = s[:i + 1]

            if t in wordDict:
                dp[i] = True
            else:
                for word in wordDict:
                    if i - len(word) >= 0 and dp[i - len(word)] and t[-len(word):] == word:
                        dp[i] = True
                        break

        return dp[len(s) - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
