from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(ind, k, visited):
            if k < 0:
                return

            if k == 0:
                res.append(visited[::])
                return

            for j in range(ind + 1, n + 1):
                visited.append(j)
                dfs(j, k - 1, visited)
                visited.pop()

        dfs(0, k, [])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))
    print(s.combine(1, 1))
