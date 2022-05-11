from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = -1
        l, r = 0, len(height) - 1

        while l < r:
            t = min(height[l], height[r]) * (r - l)
            res = max(res, t)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res


t = Solution()
print(t.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
