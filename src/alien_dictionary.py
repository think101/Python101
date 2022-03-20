from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Create a graph
        graph = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            min_length = min(len(words[i]), len(words[i + 1]))
            if words[i][:min_length] == words[i + 1][:min_length] and len(words[i]) > len(words[i + 1]):
                return ""

            for j in range(min_length):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break   # we only need to add the first different char pair

        visited = {}  # 1 visiting 2 visited
        result = []

        # no need to pass in graph, visited and result
        # not required to specify the type of c, and return type
        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = 1
            for n in graph[c]:
                if dfs(n) == 1:
                    return 1

            result.append(c)
            visited[c] = 2

        for c in graph:
            if dfs(c) == 1:
                return ""

        result.reverse()
        return ''.join(result)

t = Solution()
print(t.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
print(t.alienOrder(["z", "x"]))
print(t.alienOrder(["z", "x", "z"]))
print(t.alienOrder(["z", "x", "z", "x"]))
print(t.alienOrder(["ac", "ab", "zc", "zb"]))