from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        ones = []

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ones.append[[i, j]]

        def bfs(one):
            res = 0
            if grid[one[0], one[1]] == 1:
                res += 1
                grid[one[0], one[1]] = 0

                bfs([one[0]-1, one[1]]) if one[0]-1 >= 0 else None
                bfs([one[0]+1, one[1]]) if one[0]+1 < row else None
                bfs([one[0], one[1]-1]) if one[1]-1 >= 0 else None
                bfs([one[0], one[1]+1]) if one[1]+1 < col else None
            return res

        return sum(bfs(one) for one in ones)


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(grid))
