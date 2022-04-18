from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res, i = 0, 0
        cur_end = intervals[0][1]
        while i < len(intervals):
            # there is overlapping
            if i + 1 < len(intervals):
                if cur_end > intervals[i + 1][0]:
                    cur_end = min(cur_end, intervals[i + 1][1])
                    res += 1
                else:
                    cur_end = intervals[i + 1][1]

            i += 1

        return res


t = Solution()
print(t.eraseOverlapIntervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]))
