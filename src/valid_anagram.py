class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = "abcdefghijklmnopqrstuvwxyz"
        d = dict.fromkeys(letters, 0)

        for i in range(len(s)):
            d[s[i:i + 1]] += 1

        for i in range(len(t)):
            if t[i:i+1] not in d:
                return False
            d[t[i:i + 1]] -= 1

        for i in range(len(letters)):
            if d[letters[i:i + 1]] != 0:
                return False

        return True


t = Solution()
print(t.isAnagram("anagram", "nagaram"))
