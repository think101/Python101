from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        single = False

        for k in freq:
            if freq[k] % 2 == 0:
                res += freq[k]
            else:
                single = True
                res += freq[k] - 1

        if single:
            res += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
    print(s.longestPalindrome("a"))
