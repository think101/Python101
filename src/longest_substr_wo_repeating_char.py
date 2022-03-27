class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        prev = s[:1]
        res = 1

        for i in range(1, len(s)):
            c = s[i:i+1]
            p = prev.rfind(c)
            if p != -1:
                prev = prev[p+1:]+c
            else:
                prev = prev+c
                if len(prev) > res:
                    res = len(prev)

        return res

# O(n^2) O(len(s))
# note to use rfind instead of find