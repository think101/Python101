from collections import defaultdict
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        count = defaultdict(set)
        for idea in ideas:
            count[idea[0]].add(hash(idea[1:]))

        res = 0
        for a, count_a in count.items():
            for b, count_b in count.items():
                if a < b:
                    same = count_a & count_b
                    res += len(count_a - same) * len(count_b - same)

        return res * 2


if __name__ == "__main__":
    s = Solution()
    print(s.distinctNames(["coffee", "donuts", "time", "toffee"]))
    print(s.distinctNames(["lack", "back"]))
