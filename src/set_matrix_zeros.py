class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        rows = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            if i in rows:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        for j in range(len(matrix[0])):
            if j in cols:
                for i in range(len(matrix)):
                    matrix[i][j] = 0


t = Solution()
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
t.setZeroes(matrix)
print(matrix)
