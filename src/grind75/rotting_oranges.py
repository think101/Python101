from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0

        def rotten(rottens):
            for r in rottens:
                i, j = r[0], r[1]
                if i-1 >= 0 and grid[i - 1][j] == 1:
                    grid[i-1][j] = 2
                if i+1 < row and grid[i + 1][j] == 1:
                    grid[i+1][j] = 2
                if j-1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j-1] = 2
                if j+1 < col and grid[i][j + 1] == 1:
                    grid[i][j+1] = 2

                grid[i][j] = 3

        while True:
            rs = []
            fresh = 0
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 2:
                        rs.append([i, j])
                    elif grid[i][j] == 1:
                        fresh += 1
            if rs:
                print(rs)
                res += 1
                rotten(rs)
            else:
                break

        if fresh:
            return -1
        return res - 1 if res else 0


if __name__ == "__main__":
    s = Solution()
    print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))

