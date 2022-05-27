from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        dip = [[0 for j in range(l)] for i in range(l)]

        for i in range(l):
            t = heights[i]
            for j in range(i, l):
                t = min(t, heights[j])
                dip[i][j] = t

        res = 0
        for i in range(len(heights)):
            t = 0
            for j in range(i+1):
                a = dip[j][i] * (i - j + 1)
                t = max(t, a)

            res = max(res, t)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3, 2, 1]))
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3, 2, 1, 5, 6, 2, 3, 2, 1]))
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3, 2, 1, 5, 6, 2, 3, 2, 1, 5, 6, 2, 3, 2, 1]))
