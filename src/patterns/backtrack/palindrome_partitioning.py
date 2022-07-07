from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part[::])
                return

            for j in (i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res

    def isPalin(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False

            i, j = i + 1, j - 1

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("a"))
    print(s.partition("aa"))
    print(s.partition("ab"))
    print(s.partition("abc"))
    print(s.partition("abcdcc"))
