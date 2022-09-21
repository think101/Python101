from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_max = 0
        i = 0

        while i <= curr_max:
            curr_max = max(curr_max, nums[i] + i)
            if curr_max >= len(nums) - 1:
                return True
            i += 1

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
    print(s.canJump([3, 2, 1, 0, 4]))
    print(s.canJump([0]))
    print(s.canJump([2, 0, 0]))
