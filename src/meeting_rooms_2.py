from typing import List


class Solution:
    def minMeetingRooms_Wrong(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        for i in range(len(intervals)):
            cur = 1
            for j in range(i+1, len(intervals)):
                if intervals[i][1] > intervals[j][0]:
                    cur += 1
                else:
                    break
            res = max(res, cur)

        return res
