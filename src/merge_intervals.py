from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
