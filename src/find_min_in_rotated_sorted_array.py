from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right + 1 - left) // 2
            if nums[middle] > nums[len(nums) - 1]:
                left = middle + 1
            else:
                right = middle - 1

        return nums[left]


t = Solution()
print(t.findMin([2, 1]))
