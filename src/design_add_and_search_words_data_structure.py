class WordDictionary:
    def __init__(self):
        self.d = []

    def addWord(self, word: str) -> None:
        self.d.append(word)

    def search(self, word: str) -> bool:
        for s in self.d:
            if len(word) != len(s):
                continue

            match = True
            for i in range(len(word)):
                if word[i:i + 1] != '.' and word[i:i + 1] != s[i:i + 1]:
                    match = False

            if match:
                return True

        return False


t = WordDictionary()
t.addWord("bad")
t.addWord("dad")
t.addWord("mad")
print(t.search("pad"))
print(t.search("bad"))
print(t.search(".ad"))
print(t.search("b.."))
print(t.search("b.d"))
