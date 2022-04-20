from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = int((l + r) / 2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 0))
    print(s.search([-1, 0, 3, 5, 9, 12], 9))
    print(s.search([-1, 0, 3, 5, 9, 12], 2))
