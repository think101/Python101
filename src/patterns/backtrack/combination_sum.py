from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(visited, target, i):
            if target < 0:
                return
            elif target == 0:
                res.append(visited[::])

            for j in range(i, len(candidates)):
                visited.append(candidates[j])
                dfs(visited, target - candidates[j], j)
                visited.pop()

        dfs([], target, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3], 5))
