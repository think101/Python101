from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wd = WordDictionary()
        for w in words:
            wd.addWord(w)

        res, visited = set(), set()
        row, col = len(board), len(board[0])

        def dfs(i, j, str, cur):
            if i < 0 or i >= row or j < 0 or j >= col or (i, j) in visited or board[i][j] not in cur.children:
                return

            str += board[i][j]
            cur = cur.children[board[i][j]]
            visited.add((i, j))
            if cur.is_word:
                res.add(str)

            dfs(i + 1, j, str, cur)
            dfs(i - 1, j, str, cur)
            dfs(i, j + 1, str, cur)
            dfs(i, j - 1, str, cur)

            visited.remove((i, j))

        for i in range(row):
            for j in range(col):
                dfs(i, j, "", wd.root)

        return list(res)


t = Solution()
# board = [["o", "a"], ["e", "t"]]
# words = ["oa", "oet", "oat", "et", "etao", "tao", "abc"]
board = [["a", "b", "c", "e"], ["z", "z", "d", "z"], ["z", "z", "c", "z"], ["z", "a", "b", "z"]]
words = ["abcdce"]
print(t.findWords(board, words))
