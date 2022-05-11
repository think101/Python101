from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # directions
        row, col = len(matrix), len(matrix[0])

        direct, i, j = 0, 0, 0
        res.append(matrix[0][0])
        matrix[0][0] = 0
        while True:
            direct = direct % 4
            i, j = i + d[direct][0], j + d[direct][1]
            if 0 <= i < row and 0 <= j < col and matrix[i][j] != 0:
                res.append(matrix[i][j])
                matrix[i][j] = 0
            else:
                # change direction
                i, j = i - d[direct][0], j - d[direct][1]
                direct = (direct + 1) % 4
                if not (0 <= i + d[direct][0] < row and 0 <= j + d[direct][1] < col and matrix[i + d[direct][0]][
                    j + d[direct][1]] != 0):
                    break

        return res


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(Solution().spiralOrder(matrix))
