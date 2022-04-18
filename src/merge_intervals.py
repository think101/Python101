from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        res = []

        # need to change i within the loop, need to use while instead of for
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]

            while i+1 < len(intervals) and end >= intervals[i+1][0]:
                end = max(intervals[i+1][1], end)
                i += 1

            res.append([start, end])
            i += 1

        return res

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        for i in intervals:
            cur = i
            merged = []
            for j in range(len(res)):
                if cur[0] > res[j][1] or cur[1] < res[j][0]:
                    continue
                else:
                    cur = [min(cur[0], res[j][0]), max(cur[1], res[j][1])]
                    merged.append(j)

            if merged:
                for x in merged:
                    res[x] = None
                res = [x for x in res if x is not None]
                res.append(cur)
            else:
                res.append(i)

        return res


t = Solution()
print(t.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
print(t.merge2([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
print(t.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(t.merge2([[1, 3], [2, 6], [8, 10], [15, 18]]))
