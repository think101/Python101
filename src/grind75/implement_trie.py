class TrieNode:
    def __init__(self, c: str):
        self.val = c
        self.neighbors = {}
        self.wordEnd = False


class Trie:

    def __init__(self):
        self.nodes = {}

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            if i == 0:
                if word[i:i + 1] not in self.nodes:
                    self.nodes[word[i:i + 1]] = TrieNode(word[i:i + 1])
                cur = self.nodes[word[i:i + 1]]
            else:
                if word[i:i + 1] not in cur.neighbors:
                    cur.neighbors[word[i:i + 1]] = TrieNode(word[i:i + 1])
                cur = cur.neighbors[word[i:i + 1]]

        if i == len(word) - 1:
            cur.wordEnd = True

    def search(self, word: str) -> bool:
        if not word or word[0] not in self.nodes:
            return False

        def search(node, word):
            if len(word) == 0 or node.val != word[0]:
                return False

            if len(word) == 1 and node.val == word and node.wordEnd is True:
                return True

            for n in node.neighbors:
                if search(node.neighbors[n], word[1:]):
                    return True
            return False
        return search(self.nodes[word[0]], word)

    def startsWith(self, prefix: str) -> bool:
        if not prefix or prefix[0] not in self.nodes:
            return False

        def startWith(node, prefix):
            if len(prefix) == 0 or node.val != prefix[0]:
                return False

            if len(prefix) == 1 and node.val == prefix:
                return True

            for n in node.neighbors:
                if startWith(node.neighbors[n], prefix[1:]):
                    return True
            return False

        return startWith(self.nodes[prefix[0]], prefix)


if __name__ == '__main__':
    trie = Trie()
    trie.insert("rent")
    print(trie.search("rest"))
    print(trie.startsWith("re"))
