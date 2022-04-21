from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][0] <= newInterval[0] <= intervals[i][1] or newInterval[0] <= intervals[i][0] <= \
                    newInterval[1]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            else:
                res.append(intervals[i])

        res.append(newInterval)

        return res


t = Solution()
print(t.insert([], [4, 8]))
