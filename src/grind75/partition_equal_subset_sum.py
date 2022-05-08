from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m, s = 0, 0

        for i in range(len(nums)):
            m = i if nums[i] > nums[m] else m
            s += nums[i]

        if nums[m] * 2 == s:
            return True
        elif nums[m] * 2 > s or s % 2 != 0:
            return False

        def findTarget(nums, target):
            if target in nums:
                return True

            for i in range(len(nums)):
                if target - nums[i] > 0:
                    return findTarget(nums[:i - 1] + nums[i + 1:], target - nums[i])

            return False

        return findTarget(nums[:m - 1] + nums[m + 1:], s // 2 - nums[m])


if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))
    print(s.canPartition([1, 2, 3, 5]))
    print(s.canPartition([2, 2, 3, 5]))
