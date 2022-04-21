from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur = nums[0]

        for i in range(1, len(nums)):
            if cur < 0:
                cur = nums[i]
            else:
                cur += nums[i]

            res = max(res, cur)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
