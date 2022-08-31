from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(ind, visited, target):
            if target == 0 and len(visited) == k:
                res.append(visited[::])
                return
            if target < 0:
                return

            for i in range(ind, 10):
                visited.append(i)
                dfs(i+1, visited, target-i)
                visited.pop()

        min_v, max_v = 0, 0
        for i in range(k):
            min_v = min_v+i+1
            max_v = max_v+9-i

        if min_v <= n <= max_v:
            dfs(1, [], n)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
    print(s.combinationSum3(4, 1))
