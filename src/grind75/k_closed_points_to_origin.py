from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])
        return points[:k]


t = Solution()
print(t.kClosest([[1, 3], [-2, 2]], 1))
print(t.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
print(t.kClosest([[1, 3], [-2, 2]], 2))
