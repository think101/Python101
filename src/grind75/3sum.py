from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        freq = Counter(nums)

        res = []
        for i in range(len(nums)):
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                t = -nums[i] - nums[j]
                if t >= nums[j] and freq[t] >= 1 + int(nums[i] == t) + int(nums[j] == t):
                    res.append([nums[i], nums[j], t])

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([0, 0, 0, 0]))
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum([]))
