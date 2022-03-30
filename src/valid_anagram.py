class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = "abcdefghijklmnopqrstuvwxyz"
        d = dict.fromkeys(letters, 0)

        for c in s:
            d[c] += 1

        for c in t:
            if c not in d:
                return False
            d[c] -= 1

        for c in letters:
            if d[c] != 0:
                return False

        return True


t = Solution()
print(t.isAnagram("anagram", "nagaram"))
