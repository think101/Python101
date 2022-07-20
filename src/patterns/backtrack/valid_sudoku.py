from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        subs = {}

        for i in range(9):
            for j in range(9):
                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                if (i//3, j//3) not in subs:
                    subs[(i//3, j//3)] = set()

                if board[i][j] != '.' and (
                        board[i][j] in rows[i] or
                        board[i][j] in cols[j] or
                        board[i][j] in subs[(i//3, j//3)]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                subs[(i//3, j//3)].add(board[i][j])

        return True


if __name__ == "__main__":
    s = Solution()
    board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
             ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", ".", "1", ".", "9", ".", ".", "."],
             [".", ".", "7", ".", ".", ".", "2", "4", "."],
             [".", "6", "4", ".", "1", ".", "5", "9", "."],
             [".", "9", "8", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "8", ".", "3", ".", "2", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    print(s.isValidSudoku(board))
    board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
             [".", "4", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    print(s.isValidSudoku(board))
