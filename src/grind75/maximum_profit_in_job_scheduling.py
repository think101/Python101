from typing import List
from sortedcontainers import SortedDict
from bisect import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = SortedDict()
        max_end = 0

        for i in range(len(startTime)):
            if endTime[i] not in jobs:
                jobs[endTime[i]] = []

            jobs[endTime[i]].append([startTime[i], profit[i]])

            max_end = max(max_end, endTime[i])

        dp = SortedDict()

        for i in range(len(jobs)):
            end_ind = bisect(dp.keys(), jobs.keys()[i])
            t = 0
            if end_ind > 0:
                t = dp[jobs.keys()[end_ind - 1]]

            for j in range(len(jobs[jobs.keys()[i]])):
                start = jobs[jobs.keys()[i]][j][0]
                start_ind = bisect(dp.keys(), start)
                if start_ind > 0:
                    t = max(t, dp[dp.keys()[start_ind-1]] + jobs[jobs.keys()[i]][j][1] )
                else:
                    t = max(t, jobs[jobs.keys()[i]][j][1])

            dp[jobs.keys()[i]] = t


        return dp[max_end]

    def jobScheduling_MLE(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = {}
        max_end = 0

        for i in range(len(startTime)):
            if endTime[i] not in jobs:
                jobs[endTime[i]] = []

            jobs[endTime[i]].append([startTime[i], profit[i]])

            max_end = max(max_end, endTime[i])

        #print(max_end)
        dp = [0] * (max_end + 1)
        dp[1] = 0

        for i in range(2, max_end + 1):
            t = dp[i - 1]

            if i in jobs:
                for j in range(len(jobs[i])):
                    t = max(t, dp[jobs[i][j][0]] + jobs[i][j][1])

            dp[i] = t

        return dp[max_end]


if __name__ == "__main__":
    s = Solution()
    # print(s.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
    # print(s.jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))
    print(s.jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]))
