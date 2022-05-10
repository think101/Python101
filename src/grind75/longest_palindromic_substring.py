class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        res = s[0]

        def checkPalin1(i):
            t = s[i]
            for j in range(1, i+1):
                if i + j < len(s) and i - j >= 0 and s[i+j] == s[i-j]:
                    t = s[i-j:i+j+1]
                else:
                    break
            return t

        def checkPalin2(i, j):
            if i+1 >= len(s) or s[i] != s[i+1]:
                return ""

            t = s[i]
            for j in range(0, i+1):
                if i + 1 + j < len(s) and i - j >= 0 and s[i + j + 1] == s[i-j]:
                    t = s[i-j:i+j+2]
                else:
                    break
            return t


        for i in range(0, len(s)):
            t1 = checkPalin1(i)
            t2 = checkPalin2(i, i+1)
            if len(t1) > len(res):
                res = t1
            if len(t2) > len(res):
                res = t2

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
