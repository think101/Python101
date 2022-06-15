from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        def dfs(cookies, i, sums, res):
            #print(cookies, i, sums, res)
            if i == len(cookies):
                res[0] = min(res[0], max(sums))
                return

            if res[0] < max(sums):
                return

            for j in range(len(sums)):
                sums[j] += cookies[i]
                dfs(cookies, i + 1, sums, res)
                sums[j] -= cookies[i]

        res = [float('inf')]
        dfs(cookies, 0, [0] * k, res)
        return res[0]


if __name__ == "__main__":
    s = Solution()
    print(s.distributeCookies([8, 15, 10, 20, 8], 2))
    print(s.distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3))
    print(s.distributeCookies([76265, 7826, 16834, 63341, 68901, 58882, 50651, 75609], 8))
