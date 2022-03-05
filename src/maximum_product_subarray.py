from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = [1] * len(nums)
        current_min = [1] * len(nums)
        current_max[0] = nums[0]
        current_min[0] = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            current_max[i] = max(nums[i], current_max[i-1] * nums[i], current_min[i-1] * nums[i])
            current_min[i] = min(nums[i], current_max[i-1] * nums[i], current_min[i-1] * nums[i])
            res = max(current_max[i], res)

        return res


t = Solution()
print(t.maxProduct([-4, -3, -2]))

