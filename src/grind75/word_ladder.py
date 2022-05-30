from string import ascii_lowercase
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def dfs(word, used):
            used.append(word)

            if word == endWord:
                return used

            for i in range(len(word)):
                c = word[i]

                for char in ascii_lowercase:
                    if char != c:
                        new_word = ""
                        if i == 0:
                            new_word = char + word[1:]
                        elif i == len(word) - 1:
                            new_word = word[:len(word) - 1] + char
                        else:
                            new_word = word[:i] + char + word[i + 1:]

                        # print(new_word)

                        if new_word in wordList and new_word not in used:
                            return dfs(new_word, used)

            return None

        res = dfs(beginWord, [])
        if res:
            # print(res)
            return len(res) - 1

        return 0


t = Solution()
print(t.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
