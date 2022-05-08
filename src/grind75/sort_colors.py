import collections
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freq = collections.Counter(nums)
        curr = 0
        for i in range(3):
            for j in range(freq[i]):
                nums[curr] = i
                curr += 1


t = Solution()
t.sortColors([2, 0, 2, 1, 1, 0])
