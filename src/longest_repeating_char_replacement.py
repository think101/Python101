class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)

        uc_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        p1, p2 = 0, 1
        freq = {}
        for i in range(26):
            freq[uc_letters[i:i + 1]] = 0
        freq[s[p1:p1 + 1]] += 1
        freq[s[p2:p2 + 1]] += 1

        def check_freq_max() -> int:
            freq_max = 0
            for i in range(26):
                if freq[uc_letters[i:i + 1]] > freq_max:
                    freq_max = freq[uc_letters[i:i + 1]]
            return freq_max

        res = 0
        while p2 < len(s):
            if p2 - p1 + 1 - check_freq_max() <= k:
                if p2 - p1 + 1 > res:
                    res = p2 - p1 + 1
                p2 += 1
                if p2 < len(s):
                    freq[s[p2:p2 + 1]] += 1
            else:
                freq[s[p1:p1 + 1]] -= 1
                p1 += 1

        return res


t = Solution()
print(t.characterReplacement('ABAB', 2))
print(t.characterReplacement('AABABBA', 1))
print(t.characterReplacement('AABABBA', 2))

# O(n) time, O(1) space

