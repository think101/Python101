import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()
        counter = collections.Counter(nums)

        for i in range(0, len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j - 1 != i and j - 1 >= 0 and nums[j - 1] == nums[j]:
                    continue

                t = -nums[i] - nums[j]
                if t >= nums[j] and t in counter.keys() and counter.get(t) >= 1 + int(nums[i] == t) + int(nums[j] == t):
                    l = [nums[i], nums[j], t]
                    result.append(l)

        return result


t = Solution()
print(t.threeSum([-1, 0, 1, 2, -1, -4]))
