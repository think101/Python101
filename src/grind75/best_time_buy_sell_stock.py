from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur_min = prices[0]

        for i in range(1, len(prices)):
            cur_min = min(cur_min, prices[i])
            res = max(res, prices[i] - cur_min)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([1, 2, 3, 4, 5]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
