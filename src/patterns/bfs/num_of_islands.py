from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ones = []
        res = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    ones.append((i, j))

        for (a, b) in ones:
            if grid[a][b] == "0":
                continue

            res += 1

            q = [(a, b)]
            while (q):
                i, j = q.pop(0)

                grid[i][j] = "0"
                if i - 1 >= 0 and grid[i - 1][j] == "1":
                    q.append((i - 1, j))
                if i + 1 < row and grid[i + 1][j] == "1":
                    q.append((i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == "1":
                    q.append((i, j - 1))
                if j + 1 < col and grid[i][j + 1] == "1":
                    q.append((i, j + 1))

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
