from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        os = []
        visited = set()

        for i in range(row):
            for j in range(col):
                if (i == 0 or i == row - 1 or j == 0 or j == col - 1) and board[i][j] == 'O':
                    os.append((i, j))

        def dfs(i, j, visited):

            visited.add((i, j))
            board[i][j] = 'M'

            if i - 1 >= 0 and (i - 1, j) not in visited and board[i - 1][j] == 'O':
                dfs(i - 1, j, visited)
            if i + 1 < row and (i + 1, j) not in visited and board[i + 1][j] == 'O':
                dfs(i + 1, j, visited)
            if j - 1 >= 0 and (i, j - 1) not in visited and board[i][j - 1] == 'O':
                dfs(i, j - 1, visited)
            if j + 1 < col and (i, j + 1) not in visited and board[i][j + 1] == 'O':
                dfs(i, j + 1, visited)

        for i, j in os:
            if board[i][j] == 'O':
                dfs(i, j, visited)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == "__main__":
    board = [["O", "O", "O"], ["O", "X", "O"], ["O", "O", "O"]]
    Solution().solve(board)
    print(board)

