from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        n = [0] * l  # next max height
        p = [0] * l  # prev max height

        p[0] = height[0]
        for i in range(1, l):
            p[i] = max(p[i - 1], height[i])

        n[l - 1] = height[l - 1]
        for i in range(l - 2, -1, -1):
            n[i] = max(height[i], n[i + 1])

        res = 0
        for i in range(1, l - 1):
            if min(p[i], n[i]) > height[i]:
                res += min(p[i], n[i]) - height[i]

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0]))
    print(s.trap([4, 2, 0, 3, 2, 5]))
