class Solution:
    def longestPalindrome_TLE(self, s: str) -> str:
        if len(s) < 2:
            return s

        def isPalin(s: str):
            s = ''.join([i for i in s if i.isalpha() or i.isnumeric()]).lower()
            return s == s[::-1]

        res = ""
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if isPalin(s[i:j]) and j - i + 1 > len(res):
                    res = s[i:j]

        return res

    def longestPalindrome(self, s: str) -> str:
        r = ""

        def longestPAtIndex(i: int):
            res = s[i:i + 1]
            b, f = i - 1, i + 1

            t = ""
            while b >= 0 and f < len(s):
                if s[b:b + 1] == s[f:f + 1]:
                    t = s[b:f + 1]
                else:
                    break
                b -= 1
                f += 1
            if len(t) > len(res):
                res = t

            b, f = i, i + 1
            t = ""
            while b >= 0 and f < len(s):
                if s[b:b + 1] == s[f:f + 1]:
                    t = s[b:f + 1]
                else:
                    break
                b -= 1
                f += 1
            if len(t) > len(res):
                res = t

            return res

        for i in range(len(s)):
            subs = longestPAtIndex(i)
            if len(subs) > len(r):
                r = subs

        return r


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("c"))
    print(s.longestPalindrome("cc"))
    print(s.longestPalindrome("ccc"))
    print(s.longestPalindrome("cccc"))
