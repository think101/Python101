from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        result = []

        reach_p = [[0 for j in range(col)] for i in range(row)]
        reach_a = [[0 for j in range(col)] for i in range(row)]

        def dfs(heights: List[List[int]], i: int, j: int, h: int, reach_matrix: List[List[int]]):
            if i < 0 or j < 0 or i == row or j == col:
                return
            if reach_matrix[i][j] or heights[i][j] < h:
                return

            reach_matrix[i][j] = 1
            dfs(heights, i - 1, j, heights[i][j], reach_matrix)
            dfs(heights, i + 1, j, heights[i][j], reach_matrix)
            dfs(heights, i, j - 1, heights[i][j], reach_matrix)
            dfs(heights, i, j + 1, heights[i][j], reach_matrix)

        for i in range(row):
            dfs(heights, i, 0, 0, reach_p)  # left column
            dfs(heights, i, col - 1, 0, reach_a)  # right column
        for j in range(col):
            dfs(heights, 0, j, 0, reach_p)  # up row
            dfs(heights, row - 1, j, 0, reach_a)  # bottom row

        for i in range(row):
            for j in range(col):
                if reach_p[i][j] and reach_a[i][j]:
                    result.append([i, j])

        return result


t = Solution()
print(t.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
print(t.pacificAtlantic(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))
