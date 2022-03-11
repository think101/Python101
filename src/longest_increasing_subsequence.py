from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1

        for i in range(1, len(nums)):
            t = 1

            for j in range(0, i):
                if nums[j] < nums[i] and (dp[j] + 1 > t):
                    t = dp[j] + 1

            dp[i] = t

            if t > res:
                res = t

        return res
