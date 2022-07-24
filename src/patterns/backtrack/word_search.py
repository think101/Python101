from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, ind):

            if board[i][j] == word[ind]:
                board[i][j] = '0'

                if ind == len(word) - 1 or \
                        (i - 1 >= 0 and dfs(i - 1, j, ind + 1)) or \
                        (i + 1 < len(board) and dfs(i + 1, j, ind + 1)) or \
                        (j - 1 >= 0 and dfs(i, j - 1, ind + 1)) or \
                        (j + 1 < len(board[0]) and dfs(i, j + 1, ind + 1)):
                    return True

                board[i][j] = word[ind]

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False


if __name__ == "__main__":
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(s.exist(board, word))
    board = [["a", "b"], ["c", "d"]]
    word = "abcd"
    print(s.exist(board, word))
