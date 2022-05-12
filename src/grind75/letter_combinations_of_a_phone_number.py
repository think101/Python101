from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"],
             7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}

        def helper(digs: str):
            if len(digs) == 0:
                return []
            elif len(digs) == 1:
                return d[int(digs[0])]

            c = digs[0]
            r = helper(digs[1:])

            res = []
            for i in d[int(c)]:
                for s in r:
                    res.append(i + s)

            return res

        return helper(digits)


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinations("234"))
    print(s.letterCombinations("2345"))

