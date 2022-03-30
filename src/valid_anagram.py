class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for c in s:
            d.setdefault(c, 0)
            d[c] += 1

        for c in t:
            if c not in d:
                return False
            d[c] -= 1

        for k in d:
            if d[k] != 0:
                return False

        return True


t = Solution()
print(t.isAnagram("anagram", "nagaram"))
