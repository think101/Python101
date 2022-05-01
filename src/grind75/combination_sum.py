from typing import List


class Solution:
    def combinationSum_Mine(self, candidates: List[int], target: int) -> List[List[int]]:
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

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(target, i, cur):
            if target == 0:
                res.append(cur.copy())  # need to have a copy here
                return

            for j in range(i, len(candidates)):
                if candidates[j] > target:
                    break
                cur.append(candidates[j])
                dfs(target - candidates[j], j, cur)
                cur.pop(-1)

        dfs(target, 0, [])

        return res



t = Solution()
print(t.combinationSum([2, 3, 6, 7], 7))
print(t.combinationSum([2, 3, 5], 8))
print(t.combinationSum([2, 3, 5], 7))
print(t.combinationSum([2, 3, 5], 6))
print(t.combinationSum([2, 3, 5], 1))

