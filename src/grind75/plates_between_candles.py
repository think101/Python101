from bisect import bisect
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []

        for i in range(len(s)):
            if s[i] == '|':
                candles.append(i)

        res = [0 for i in range(len(queries))]
        for i in range(len(queries)):
            left = bisect(candles, queries[i][0] - 1)
            right = bisect(candles, queries[i][1]) - 1

            if left >= len(candles) or right < 0 or candles[right] - candles[left] <= 1:
                res[i] = 0
                continue

            res[i] = candles[right] - candles[left] - 1 - (right - left - 1)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]]))
    print(s.platesBetweenCandles("||*", [[2, 2]]))
