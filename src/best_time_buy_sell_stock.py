from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            if prices[i] - min_price > res:
                res = prices[i] - min_price

        return res


t = Solution()
print(t.maxProfit([7,1,5,3,6,4]))
print(t.maxProfit([7,6,4,3,1]))

