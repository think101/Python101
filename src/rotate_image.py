from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # a,b left upper   x,y right bottom
        def rotate(a, x):
            if a == x:
                return

            for t in range(x - a):
                tmp = matrix[a][a]
                # left column
                for i in range(a, x):
                    matrix[i][a] = matrix[i + 1][a]
                # bottom row
                for j in range(a, x):
                    matrix[x][j] = matrix[x][j + 1]
                # right column
                for i in range(a, x):
                    matrix[x - i + a][x] = matrix[x - i + a - 1][x]
                # up row
                for j in range(a, x - 1):
                    matrix[a][x - j + a] = matrix[a][x - j + a - 1]

                matrix[a][a + 1] = tmp

        a, x = 0, len(matrix) - 1
        while a < x:
            rotate(a, x)
            a += 1
            x -= 1


t = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t.rotate(matrix)
print(matrix)
