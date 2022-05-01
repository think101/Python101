from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        for i in range(1, target + 1):
            res = []
            for j in candidates:
                if i == j:
                    res.append([j])
                elif i - j > 0 and dp[i - j]:
                    for l in dp[i - j]:
                        if l:
                            ll = sorted(l + [j])  # need to create a new list and sort it
                            if ll not in res:
                                res.append(ll)

            dp[i] = res

        return dp[target]


t = Solution()
print(t.combinationSum([2, 3, 6, 7], 7))
