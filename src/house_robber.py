from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(0, len(nums)):
            dp[i] = max(dp[i-2] + nums[i] if i-2 >= 0 else nums[i], dp[i-1])

        return dp[len(nums)-1]


t = Solution()
print(t.rob([1,2,3,1]))
print(t.rob([2,7,9,3,1]))

