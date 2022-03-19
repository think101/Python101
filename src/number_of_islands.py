from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[0 for j in range(col)] for i in range(row)]

        def dfs(g: List[List[str]], i: int, j: int, v: List[List[int]]):
            if i < 0 or j < 0 or i == row or j == col:
                return
            if g[i][j] == '0' or v[i][j] == 1:
                return

            v[i][j] = 1
            dfs(g, i - 1, j, v)
            dfs(g, i + 1, j, v)
            dfs(g, i, j - 1, v)
            dfs(g, i, j + 1, v)

        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    result += 1
                    dfs(grid, i, j, visited)

        return result

