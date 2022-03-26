from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        row, col = len(matrix), len(matrix[0])
        i, j = 0, 0
        d = 1  # 1 right 2 down 3 left 4 up

        while True:
            if len(res) == row * col:
                break

            if d == 1:
                while j < col and matrix[i][j] != 999:
                    res.append(matrix[i][j])
                    matrix[i][j] = 999
                    j += 1
                j -= 1
                i += 1
            elif d == 2:
                while i < row and matrix[i][j] != 999:
                    res.append(matrix[i][j])
                    matrix[i][j] = 999
                    i += 1
                i -= 1
                j -= 1
            elif d == 3:
                while j >= 0 and matrix[i][j] != 999:
                    res.append(matrix[i][j])
                    matrix[i][j] = 999
                    j -= 1
                j += 1
                i -= 1
            else:
                while i >= 0 and matrix[i][j] != 999:
                    res.append(matrix[i][j])
                    matrix[i][j] = 999
                    i -= 1
                j += 1
                i += 1

            d = d + 1 if d + 1 <= 4 else 1

        return res


t = Solution()
print(t.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
