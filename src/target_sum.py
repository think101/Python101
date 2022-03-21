from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)

        @lru_cache(maxsize=None)
        def dfs(tt: int, index: int) -> int:
            # last element
            if index == length-1:
                return int(nums[index] == tt) + int(-nums[index] == tt)

            return dfs(tt + nums[index], index + 1) + dfs(tt - nums[index], index + 1)

        return dfs(target, 0)


t = Solution()
print(t.findTargetSumWays([1, 1, 1, 1, 1], 3))

