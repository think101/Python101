from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp[i] means the max index we can reach from index i
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i-1] < i:
                return False

            dp[i] = max(dp[i-1], nums[i]+i)

        return dp[len(nums)-1] >= len(nums)-1


t = Solution()
print(t.canJump([4,0,4,2,2,0,1,3,3,0,3]))
print(t.canJump([2,3,1,1,4]))
print(t.canJump([3,2,1,0,4]))
print(t.canJump([2,0,0]))
print(t.canJump([0]))

