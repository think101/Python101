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

    # 0 not exists, 1 str exists as pref, 2 str exists as word
    def search(self, w: str) -> int:
        cur = self.root
        for i in range(len(w)):
            if w[i:i + 1] not in cur.children:
                return 0
            else:
                cur = cur.children[w[i:i + 1]]
                if i == len(w) - 1:
                    if cur.is_word:
                        return 2  # word
                    else:
                        return 1  # prefix


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wd = WordDictionary()
        for w in words:
            wd.addWord(w)

        res = set()
        row, col = len(board), len(board[0])

        def copyVisited(visited):
            new_v = [[0] * col for _ in range(row)]
            for a in range(row):
                for b in range(col):
                    new_v[a][b] = visited[a][b]
            return new_v

        def dfs(visited, i, j, str):
            if i < 0 or i >= row or j < 0 or j >= col or visited[i][j] == 1:
                return False
            str += board[i][j]
            r = wd.search(str)
            if r == 0:
                return False
            elif r == 2:
                res.add(str)

            # prefix or word
            visited[i][j] = 1
            dfs(copyVisited(visited), i - 1, j, str)
            dfs(copyVisited(visited), i + 1, j, str)
            dfs(copyVisited(visited), i, j - 1, str)
            dfs(copyVisited(visited), i, j + 1, str)

        for i in range(row):
            for j in range(col):
                v = [[0] * col for _ in range(row)]
                dfs(v, i, j, "")

        return list(res)


t = Solution()
# board = [["o", "a"], ["e", "t"]]
# words = ["oa", "oet", "oat", "et", "etao", "tao", "abc"]
board = [["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]]
words = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]
print(t.findWords(board, words))
