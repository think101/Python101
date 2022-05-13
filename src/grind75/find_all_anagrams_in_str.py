import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        l = len(p)
        d = collections.Counter(p)

        def isAnagram(d1, d2):
            if len(d1) != len(d2):
                return False

            for k in d1:
                if k not in d2 or d1[k] != d2[k]:
                    return False
            return True

        res = []
        di = {}
        for i in range(l):
            if s[i] not in di:
                di[s[i]] = 0
            di[s[i]] += 1
        if isAnagram(di, d):
            res.append(0)

        for i in range(l, len(s)):
            if s[i] not in di:
                di[s[i]] = 0
            di[s[i]] += 1

            di[s[i-l]] -= 1
            if di[s[i-l]] == 0:
                di.pop(s[i-l], None)

            if isAnagram(di, d):
                res.append(i-l+1)

        return res

    def findAnagrams_TLE(self, s: str, p: str) -> List[int]:
        l = len(p)
        d = collections.Counter(p)

        def isAnagram(d1, d2):
            if len(d1) != len(d2):
                return False

            for k in d1:
                if k not in d2 or d1[k] != d2[k]:
                    return False
            return True

        res = []
        for i in range(len(s)):
            di = collections.Counter(s[i:i+l])
            if isAnagram(di, d):
                res.append(i)

        return res

t = Solution()
print(t.findAnagrams("cbaebabacd", "abc"))
print(t.findAnagrams("abab", "ab"))
