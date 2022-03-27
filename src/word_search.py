from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col, word_len = len(board), len(board[0]), len(word)

        def dfs(index: int, i: int, j: int) -> bool:
            if i < 0 or i >= row or j < 0 or j >= col or index >= word_len or board[i][j] != word[index:index + 1]:
                return False

            if index == word_len - 1:
                return True

            tmp = board[i][j]
            board[i][j] = 0
            result = dfs(index + 1, i - 1, j) or dfs(index + 1, i + 1, j) or dfs(index + 1, i, j - 1) or dfs(index + 1,
                                                                                                             i, j + 1)
            if not result:
                board[i][j] = tmp
            return result

        for a in range(row):
            for b in range(col):
                v = [[0] * col for _ in range(row)]
                if dfs(0, a, b):
                    return True

        return False


t = Solution()
# print(t.exist([["A", "A"], ["A", "A"]], "AA"))
print(t.exist([["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
               ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]],
              "AAAAAAAAAAAAAAB"))
