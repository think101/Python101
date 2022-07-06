from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        d = {}  # dict with key as i, and value as the result of s[i:]

        def helper(s):
            if len(s) == 1:
                d[len(s)] = [[s]]
                return [[s]]

            current_res = []
            for i in range(1, len(s)):
                t = s[i:]
                if len(t) not in d:
                    helper(t)

                r = d[len(s) - i]
                for l in r:
                    first_s = s[:i]
                    if first_s == first_s[::-1]:
                        current_res.append([first_s] + l)

            d[len(s)] = current_res

        helper(s)
        return d.get(len(s))


if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("a"))
    print(s.partition("aa"))
    print(s.partition("ab"))
    print(s.partition("abc"))
    print(s.partition("abcdcc"))

