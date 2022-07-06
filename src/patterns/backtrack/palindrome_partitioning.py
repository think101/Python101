from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        d = {}     # dict with key as i, and value as the result of s[i:]

        def helper(s):
            if len(s) == 1:
                d.put(len(s), [[s]])
                return [[s]]

            current_res = []
            for i in range(1, len(s)):
                r = d[len(s) - i]
                first_s = s[:1] + r[0][0]
                if first_s == first_s[::-1]:
                    current_res.append([first_s] + r[1:])

            d.put(len(s), current_res)

        helper(s)
        return d.get(len(s))



if __name__ == "__main__":
    s = Solution()
    print(s.partition([1, 2, 3]))

