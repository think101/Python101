from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(1, target+1):
            res = 0
            for j in nums:
                if i-j >= 0 and dp[i-j] > 0:
                    res += dp[i-j]
            dp[i] = res

        return dp[target]
    

t = Solution()
print(t.combinationSum4([1, 2, 3], 4))
print(t.combinationSum4([1, 2, 3], 5))