from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        visited = [[0] * col for _ in range(row)]
        oldColor = image[sr][sc]

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or visited[r][c] == 1:
                return

            visited[r][c] = 1

            if image[r][c] != oldColor:
                return

            image[r][c] = newColor

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)

        return image


if __name__ == '__main__':
    s = Solution()
    print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
    print(s.floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1))
