import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)

        for i in freq:
            if freq[i] > len(nums) // 2:
                return i


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
