from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0 and n == 1:
            return True

        graph = {}
        for edge in edges:
            graph.setdefault(edge[0], []).append(edge[1])
            graph.setdefault(edge[1], []).append(edge[0])

        visit = {}

        def dfs(num: int, prev: int) -> bool:
            if num != prev and num in visit:
                return False

            visit[num] = 1
            if num in graph:
                for nei in graph[num]:
                    if nei != prev and dfs(nei, num) == False:
                        return False

            return True

        return dfs(0, -1) and len(visit) == n


t = Solution()
print(t.validTree(2, [[1, 0]]))
print(t.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(t.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
