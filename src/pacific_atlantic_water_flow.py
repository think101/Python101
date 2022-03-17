from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        result = []

        # 1 pacific 2 altantic
        status = [[0 for j in range(col)] for i in range(row)]
        for i in range(0, row):
            status[i][0] = 1
            status[i][col-1] = 2
        for j in range(0, col):
            status[0][j] = 1
            status[row-1][j] = 2
        status[row-1][0] = 3
        status[0][col-1] = 3
        result.append([row-1, 0])
        result.append([0, col-1])

        def checkNode(i: int, j: int, heights: List[List[int]]):
            if i-1 >= 0 and heights[i-1][j] >= heights[i][j]:
                if status[i-1][j] == 0:
                    status[i-1][j] = status[i][j]
                elif status[i-1][j] != status[i][j] and status[i][j] != 0:
                    status[i-1][j] = 3
                    result.append([i-1, j]) if [i-1,j] not in result else result
            if i+1 < row and heights[i+1][j] >= heights[i][j]:
                if status[i+1][j] == 0:
                    status[i+1][j] = status[i][j]
                elif status[i+1][j] != status[i][j] and status[i][j] != 0:
                    status[i+1][j] = 3
                    result.append([i+1, j]) if [i+1, j] not in result else result
            if j-1 >= 0 and heights[i][j-1] >= heights[i][j]:
                if status[i][j-1] == 0:
                    status[i][j-1] = status[i][j]
                elif status[i][j-1] != status[i][j] and status[i][j] != 0:
                    status[i][j-1] = 3
                    result.append([i, j-1]) if [i, j-1] not in result else result
            if j+1 < col and heights[i][j+1] >= heights[i][j]:
                if status[i][j+1] == 0:
                    status[i][j+1] = status[i][j]
                elif status[i][j+1] != status[i][j] and status[i][j] != 0:
                    status[i][j+1] = 3
                    result.append([i, j+1]) if [i, j+1] not in result else result

        for i in range(0, row):
            for j in range(0, col):
                checkNode(i,j, heights)

        return list(result)


t = Solution()
print(t.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

