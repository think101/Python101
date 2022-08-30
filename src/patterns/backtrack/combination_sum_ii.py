from typing import List


class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        c.sort()
        res = set()

        def dfs(ind, target, visited):
            if ind >= len(c) or target < 0:
                return

            if target == c[ind]:
                res.add(tuple(visited[::] + [c[ind]]))
                return

            visited.append(c[ind])
            for i in range(ind+1, len(c)):
                dfs(i, target - c[ind], visited)
            visited.pop()

        for i in range(len(c)):
            if i-1 >= 0 and c[i-1] == c[i]:
                continue
            dfs(i, target, [])

        res = [list(t) for t in res]

        return list(res)


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(s.combinationSum2([2, 5, 2, 1, 2], 5))
    print(s.combinationSum2([1, 2, 3], 4))
    print(s.combinationSum2([1, 2, 3], 1))
