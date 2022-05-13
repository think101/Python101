import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
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
