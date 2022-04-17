from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def isOverlap(interval1: List[int], interval2: List[int]):
            if interval1[0] > interval2[1] or interval1[1] < interval2[0]:
                return False
            return True

        def merge(interval1: List[int], interval2: List[int]):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

        res = []
        merged = 0

        for i in intervals:
            if isOverlap(i, newInterval):
                newInterval = merge(i, newInterval)
                merged = 1
            else:
                if merged == 1:
                    res.append(newInterval)
                    merged = 2
                res.append(i)

        if not merged:
            if len(res) == 0:
                res.append(newInterval)
            else:
                for i in range(len(res)):
                    if newInterval[1] < res[i][0]:
                        res.insert(i, newInterval)
                        merged = 2
                        break
                if not merged:
                    res.append(newInterval)
        elif merged == 1:
            res.append(newInterval)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1, 5]], [6, 8]))
    print(s.insert([[1, 5]], [0, 3]))
    print(s.insert([[1, 5]], [2, 3]))
