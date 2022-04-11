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

    def search(self, word: str) -> bool:
        def dfs(node, w) -> bool:
            cur = node

            for i in range(len(w)):
                if w[i:i + 1] == '.':
                    if i == len(w) - 1:
                        return True
                    for key in cur.children:
                        if dfs(cur.children[key], w[i + 1:]):
                            return True
                    return False
                else:
                    if w[i:i + 1] not in cur.children:
                        return False
                    else:
                        cur = cur.children[w[i:i + 1]]
                        if i == len(w) - 1:
                            return cur.is_word

        return dfs(self.root, word)


t = WordDictionary()
t.addWord("bad")
t.addWord("dad")
t.addWord("mad")
#print(t.search("pad"))
#print(t.search("bad"))
#print(t.search(".ad"))
print(t.search("b.."))
