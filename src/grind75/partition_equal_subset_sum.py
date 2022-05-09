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

        dp = [False] * (s + 1)
        dp[0] = True

        for n in nums:
            for i in range(s, -1, -1):
                if dp[i]:
                    dp[i + n] = True
                if dp[s // 2]:
                    return True

        return False

    def canPartition_TLE(self, nums: List[int]) -> bool:
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
                if target - nums[i] > 0 and findTarget(nums[:i] + nums[i + 1:], target - nums[i]):
                    return True

            return False

        return findTarget(nums[:m] + nums[m + 1:], s // 2 - nums[m])


if __name__ == "__main__":
    s = Solution()
    # print(s.canPartition([1, 5, 11, 5]))
    # print(s.canPartition([1, 2, 3, 5]))
    # print(s.canPartition([2, 2, 3, 5]))
    # print(s.canPartition([1, 3, 4, 4]))
    print(s.canPartition(
        [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         99, 97]))
