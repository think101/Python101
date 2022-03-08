from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        res = 0

        while l<r:
            t = min(height[r], height[l]) * (r-l)
            if t > res:
                res = t

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res

    