from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0
        for i in range(len(nums)):
            sum1 += i
            sum2 += nums[i]

        return sum1 + len(nums) - sum2


t = Solution()
print(t.missingNumber([0, 1, 3]))
print(t.missingNumber2([0, 1, 3]))
