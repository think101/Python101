from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        queue = []

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    mat[i][j] = -1
                else:
                    queue.append((i, j))

        while queue:
            i, j = queue.pop(0)

            if i - 1 >= 0 and mat[i-1][j] == -1:
                mat[i-1][j] = mat[i][j] + 1
                queue.append((i-1, j))
            if i + 1 < row and mat[i+1][j] == -1:
                mat[i+1][j] = mat[i][j] + 1
                queue.append((i+1, j))
            if j - 1 >= 0 and mat[i][j-1] == -1:
                mat[i][j-1] = mat[i][j] + 1
                queue.append((i, j-1))
            if j + 1 < col and mat[i][j+1] == -1:
                mat[i][j+1] = mat[i][j] + 1
                queue.append((i, j+1))

        return mat


if __name__ == "__main__":
    mat = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]
    print(Solution().updateMatrix(mat))
