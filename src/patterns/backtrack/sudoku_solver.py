from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = {}   # numbers used in each row
        cols = {}   # numbers used in each col
        subs = {}   # numbers used in each sub box

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if i not in rows:
                        rows[i] = set()
                    if j not in cols:
                        cols[j] = set()

                    a, b = i // 3, j //3
                    if (a, b) not in subs:
                        subs[(a, b)] = set()

                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    subs[(a,b)].add(board[i][j])


        def backtrack(i, j, rows, cols, subs, board):
            while i < 9:
                while j < 9:
                    if i == 9:
                        return True

                    if board[i][j] != '.':
                        if j < 8:
                            j += 1
                        else:
                            i += 1
                        continue

                    for k in range(9):
                        if k in rows[i] or k in cols[j] or k in subs[(i//3, j//3)]:
                            continue

                        board[i][j] = k
                        rows[i].add(k)
                        cols[j].add(k)
                        subs[(i//3, j//3)].add(k)

                        if j < 8:
                            if backtrack(i, j+1, rows, cols, subs, board):
                                return True
                        else:
                            if backtrack(i+1, 0, rows, cols, subs, board):
                                return True

                        board[i][j] = '.'
                        rows[i].remove(k)
                        cols[j].remove(k)
                        subs[(i//3, j//3)].remove(k)

                    return False

        backtrack(0, 0, rows, cols, subs, board)
