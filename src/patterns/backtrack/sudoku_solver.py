from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = {}  # numbers used in each row
        cols = {}  # numbers used in each col
        subs = {}  # numbers used in each sub box

        for i in range(9):
            for j in range(9):
                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()

                a, b = i // 3, j // 3
                if (a, b) not in subs:
                    subs[(a, b)] = set()

                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    subs[(a, b)].add(board[i][j])

        def backtrack(i, j, rows, cols, subs, board):
            print(i, j)
            while i < 9:
                while j < 9:
                    if i == 9:
                        print(i, j)
                        return True

                    if board[i][j] != '.':
                        if j < 8:
                            j += 1
                        else:
                            i += 1
                            j = 0
                        continue

                    for k in range(1, 10):
                        if str(k) in rows[i] or str(k) in cols[j] or str(k) in subs[(i // 3, j // 3)]:
                            continue

                        board[i][j] = str(k)
                        rows[i].add(str(k))
                        cols[j].add(str(k))
                        subs[(i // 3, j // 3)].add(str(k))

                        if j < 8:
                            if backtrack(i, j + 1, rows, cols, subs, board):
                                return True
                        else:
                            if backtrack(i + 1, 0, rows, cols, subs, board):
                                return True

                        board[i][j] = '.'
                        rows[i].remove(str(k))
                        cols[j].remove(str(k))
                        subs[(i // 3, j // 3)].remove(str(k))

                    return False

        backtrack(0, 0, rows, cols, subs, board)


if __name__ == "__main__":
    s = Solution()
    board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
             ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", ".", "1", ".", "9", ".", ".", "."],
             [".", ".", "7", ".", ".", ".", "2", "4", "."],
             [".", "6", "4", ".", "1", ".", "5", "9", "."],
             [".", "9", "8", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "8", ".", "3", ".", "2", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "6"],
             [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    s.solveSudoku(board)
    print(board)
