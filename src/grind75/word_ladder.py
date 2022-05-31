from string import ascii_lowercase
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = [beginWord]
        step = 1

        while q:
            step += 1

            for i in range(len(q)):
                word = q.pop(0)

                for j in range(len(word)):
                    c = word[j]

                    for char in ascii_lowercase:
                        if char != c:
                            newWord = ""
                            if j == 0:
                                newWord = char + word[1:]
                            elif j == len(word) - 1:
                                newWord = word[:len(word) - 1] + char
                            else:
                                newWord = word[:j] + char + word[j + 1:]

                            if newWord in wordSet:
                                # print(newWord)
                                if newWord == endWord:
                                    return step

                                wordSet.remove(newWord)
                                q.append(newWord)

        return 0


t = Solution()
print(t.ladderLength("hot", "dog", ["hot", "dog", "dot"]))
print(t.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(t.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
