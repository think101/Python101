from typing import List


class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        c.sort()
        res = []

        def dfs(ind, target, visited):
            if target < 0:
                return

            if target == 0:
                res.append(visited[::])
                return

            prev = -1
            for i in range(ind, len(c)):
                if c[i] == prev:
                    continue

                visited.append(c[i])
                dfs(i+1, target - c[i], visited)
                visited.pop()
                prev = c[i]

        dfs(0, target, [])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(s.combinationSum2([2, 5, 2, 1, 2], 5))
    print(s.combinationSum2([1, 2, 3], 4))
    print(s.combinationSum2([1, 2, 3], 1))
