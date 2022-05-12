from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def dfs(i, j, index, path: List[str]):
            if i < 0 or i >= row or j < 0 or j >= col or [i,j] in path or board[i][j] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            path.append([i, j])
            print(path)
            if dfs(i-1, j, index+1, path) or dfs(i+1, j, index+1, path) or dfs(i, j-1, index+1, path) or dfs(i, j+1, index+1, path) :
                return True

            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, []):
                        return True

        return False
