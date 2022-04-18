from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        i, j = 0, 0
        res, cur = 0,0

        while i < len(intervals) and j < len(intervals):
            if start[i] < end[j]:
                cur += 1
                i += 1
                res = max(res, cur)
            elif start[i] > end[j]:
                j += 1
                cur -= 1
            else:
                j += 1
                i += 1

        # it's possible there are still end time points, not processing them is fine

        return res

    def minMeetingRooms_Slow(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        checked = []
        for i in range(len(intervals)):
            if len(checked) == len(intervals):
                break
            if i in checked:
                continue

            checked.append(i)
            cur = []
            cur.append(i)
            res += 1
            for j in range(i + 1, len(intervals)):
                if j in checked:
                    continue
                overlap = False
                for k in cur:
                    if intervals[k][1] > intervals[j][0]:
                        overlap = True
                        break
                if not overlap:
                    checked.append(j)
                    cur.append(j)

        return res

    def minMeetingRooms_Wrong(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        for i in range(len(intervals)):
            cur = 1
            for j in range(i + 1, len(intervals)):
                if intervals[i][1] > intervals[j][0]:
                    cur += 1
                else:
                    break
            res = max(res, cur)

        return res


t = Solution()
print(t.minMeetingRooms_Slow([[0, 30], [5, 10], [15, 20]]))
print(t.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(t.minMeetingRooms_Slow([[1, 5], [8, 9], [8, 9]]))
print(t.minMeetingRooms([[1, 5], [8, 9], [8, 9]]))
