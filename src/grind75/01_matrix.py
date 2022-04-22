from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])

        def copyVisited(visited):
            newVisited = [[0] * col for _ in range(row)]
            for i in range(row):
                for j in range(col):
                    newVisited[i][j] = visited[i][j]
            return newVisited

        def dfs(r, c, step, visited):
            if r < 0 or r >= row or c < 0 or c >= col or visited[r][c] == 1:
                return

            visited[r][c] = 1
            if mat[r][c] == 1:
                mat[r][c] = step + 1
            else:
                mat[r][c] = min(mat[r][c], step + 1)

            dfs(r - 1, c, step + 1, copyVisited(visited))
            dfs(r + 1, c, step + 1, copyVisited(visited))
            dfs(r, c + 1, step + 1, copyVisited(visited))
            dfs(r, c - 1, step + 1, copyVisited(visited))

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    visited = [[0] * col for _ in range(row)]
                    dfs(i, j, 0, visited)

        return mat


if __name__ == "__main__":
    mat = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]
    print(Solution().updateMatrix(mat))
