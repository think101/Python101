import collections
from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

        print(red, white, blue)

    def sortColors_hmmm(self, nums: List[int]) -> None:
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
