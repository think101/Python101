from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col, word_len = len(board), len(board[0]), len(word)

        def dfs(index: int, i: int, j: int, visited: List[List[int]]) -> bool:
            if i < 0 or i >= row or j < 0 or j >= col or index >= word_len or board[i][j] != word[index:index + 1] or \
                    visited[i][j] == 1:
                return False

            if index == word_len - 1:
                return True

            v = [[0] * col] * row
            for x in range(row):
                for y in range(col):
                    v[x][y] = visited[x][y]

            v[i][j] = 1
            return dfs(index + 1, i - 1, j, v) or dfs(index + 1, i + 1, j, v) or dfs(index + 1, i, j - 1, v) or dfs(
                index + 1, i, j + 1, v)

        for a in range(row):
            for b in range(col):
                if board[a][b] == word[:1]:
                    v = [[0] * col] * row
                    if dfs(0, a, b, v):
                        return True

        return False


t = Solution()
print(t.exist([["A", "B"], ["S", "F"]], "ABF"))
