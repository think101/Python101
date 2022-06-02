from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
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
    print(s.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
    print(s.jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))
    print(s.jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]))
