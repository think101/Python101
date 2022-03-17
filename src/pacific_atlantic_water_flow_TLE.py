from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        result = []

        # 1 for pacific 2 for altantic 3 for both
        def dfs(heights: List[List[int]], i: int, j: int, h: int) -> int:
            if i < 0 or j < 0:
                return 1
            if i == row or j == col:
                return 2
            if heights[i][j] > h:
                return 0

            h = heights[i][j]
            heights[i][j] = 999999

            r = dfs(heights, i+1, j, h) | dfs(heights, i-1, j, h) | dfs(heights, i, j+1, h) | dfs(heights, i, j-1, h)

            heights[i][j] = h
            return r

        for i in range(row):
            for j in range(col):
                if dfs(heights, i, j, heights[i][j]) == 3:
                    result.append([i, j])
        return result


t = Solution()
print(t.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
print(t.pacificAtlantic([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))