from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        ones = []

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    ones.append([i, j])

        def dfs(one):
            i, j = one[0], one[1]
            res = 0
            if grid[i][j] == "1":
                res += 1
                grid[i][j] = "0"

                dfs([i-1, j]) if i-1 >= 0 else None
                dfs([i+1, j]) if i+1 < row else None
                dfs([i, j-1]) if j-1 >= 0 else None
                dfs([i, j+1]) if j+1 < col else None
            return res

        return sum(dfs(one) for one in ones)


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(grid))

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands(grid))
