import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = collections.Counter(t)
        freq_s = {}

        count, start = 0, -1
        res = s

        for i in range(len(s)):
            if s[i] not in freq_t:
                continue

            if start == -1:
                start = i

            if s[i] not in freq_s:
                freq_s[s[i]] = 0

            if freq_t[s[i]] > freq_s[s[i]]:
                count += 1
            freq_s[s[i]] = freq_s[s[i]] + 1

            if count == len(t) and i - start + 1 < len(res):
                res = s[start:i+1]

            if start > 0 and count == len(t) and s[i] == s[start]:
                #shift start
                for j in range(start+1, i):
                    if s[j] not in freq_t:
                        continue

                    if freq_s[s[j]] == freq_t[s[j]]:
                        if i - j + 1 < len(res):
                            res = s[j:i+1]
                        break
                    elif freq_s[s[j]] > freq_t[s[j]]:
                        freq_s[s[j]] = freq_s[s[j]] - 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
