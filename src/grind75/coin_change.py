from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0

        coins = sorted(coins)

        for i in range(1, amount+1):
            for c in coins:
                if i - c < 0:
                    break

                if dp[i-c] != -1 and (dp[i] == -1 or dp[i] > dp[i-c] + 1):
                    dp[i] = dp[i-c] + 1

        return dp[amount]


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange([2], 3))
    print(s.coinChange([1, 2, 5], 100))
