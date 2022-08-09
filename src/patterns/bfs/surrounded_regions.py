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

        for i, j in os:
            q = [(i, j)]

            while (q):
                x, y = q.pop(0)

                if ((x, y) in visited):
                    continue

                board[x][y] = 'M'
                visited.add((x, y))

                if x - 1 >= 0 and (x - 1, y) not in visited and board[x - 1][y] == 'O':
                    q.append((x - 1, y))
                if x + 1 < row and (x + 1, y) not in visited and board[x + 1][y] == 'O':
                    q.append((x + 1, y))
                if y - 1 >= 0 and (x, y - 1) not in visited and board[x][y - 1] == 'O':
                    q.append((x, y - 1))
                if y + 1 < col and (x, y + 1) not in visited and board[x][y + 1] == 'O':
                    q.append((x, y + 1))

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

