class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = set()

        for i in range(len(s)):
            if s[i] in letters:
                return s[i]
            letters.add(s[i])

        return ''


if __name__ == "__main__":
    s = Solution()
    print(s.repeatedCharacter("abcd"))
    print(s.repeatedCharacter("aabbccdd"))
