from typing import List


class Solution:
    def merge_wrong(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        t = []

        for i in range(len(intervals)):
            t = intervals[i]
            for j in range(i + 1, len(intervals)):
                if intervals[j][0] > t[1] or intervals[j][1] < t[0]:
                    res.append(t)
                    i = j    # can not set i here, because the next loop will be wrong
                    break

                t = [min(t[0], intervals[j][0]), max(t[1], intervals[j][1])]

        res.append(t)

        return res

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        t = []
        
        for i in range(len(intervals)):
            if not intervals[i]:
                continue

            t = intervals[i]
            for j in range(i+1, len(intervals)):
                if intervals[j][0] > t[1] or intervals[j][1] < t[0]:
                    res.append(t)
                    break

                t = [min(t[0], intervals[j][0]), max(t[1], intervals[j][1])]
                intervals[j] = None

        res.append(t)

        return res


t = Solution()
print(t.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(t.merge([[1, 4], [4, 5]]))
print(t.merge([[1, 4], [0, 4]]))
print(t.merge([[1, 4], [2, 3]]))
