from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            dp[i] = -1
            for c in coins:
                t = dp[i - c] + 1 if i - c >= 0 else -1
                if t > 0 and (t < dp[i] or dp[i] == -1):
                    dp[i] = t

        return dp[amount]


t = Solution()
print(t.coinChange([1, 2, 5], 11))

