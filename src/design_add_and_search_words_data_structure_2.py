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
            if not cur.children[c]:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, word) -> bool:
            cur = node

            for i in range(len(word)):
                if word[i:i+1] == '.':
                    for n in cur.children:
                        if dfs(n, word[1:]):
                            return True
                    return False
                else:
                    if not cur.children[word[i:i+1]]:
                        return False
                    else:
                        cur = cur.children[word[i:i+1]]
                        if i == len(word)-1:
                            return cur.is_word

        return dfs(self.root, word)


t = WordDictionary()
t.addWord("bad")
t.addWord("dad")
t.addWord("mad")
print(t.search("pad"))
print(t.search("bad"))
print(t.search(".ad"))


