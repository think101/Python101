from typing import List


class PermutationCombination:

    # candidates: candidate numbers
    # n: number of candidates used to generate permutation
    def permutation(self, candidates: List[int], n: int) -> List[List[int]]:
        res = []

        def dfs(depth: int, n: int, used: List[bool], path: List[int]) -> None:
            if depth == n:
                res.append(path.copy())
                return

            for i in range(len(candidates)):
                if not used[i]:
                    used[i] = True
                    path.append(candidates[i])
                    dfs(depth + 1, n, used, path)
                    used[i] = False
                    path.pop()

        dfs(0, n, [False] * len(candidates), [])
        return res

    def combination(self, candidates: List[int], n: int) -> List[List[int]]:
        res = []

        def dfs(depth: int, n: int, start: int, path: List[int]) -> None:
            if depth == n:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(depth + 1, n, i + 1, path)
                path.pop()

        dfs(0, n, 0, [])
        return res

t = PermutationCombination()
print(t.permutation([1, 2, 3], 2))
print(t.combination([1, 2, 3], 2))

print(t.permutation([1, 2, 3], 3))
print(t.combination([1, 2, 3], 3))

