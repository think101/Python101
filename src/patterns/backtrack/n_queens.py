from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = [None for i in range(n)]
        excludes = {}  # key as placement value as list of excluded spaces

        def calc_excludes(i, j):
            ex = set()
            # the ith line
            for k in range(n):
                if [i, k] not in excludes.values():
                    ex.add([i, k])

            # the jth column
            for k in range(n):
                if[k, j] not in excludes.values():
                    ex.add([k, j])

            # i++ j--  or i-- j++
            a, b = i, j
            while a < n and b >= 0:
                if[a, b] not in excludes.values():
                    ex.add([a, b])
                a += 1
                b -= 1

            a, b = i, j
            while a >= 0 and b < n:
                if[a, b] not in excludes.values():
                    ex.add([a, b])
                a -= 1
                b += 1


            # i-- j--  or i++ j++
            a, b = i, j
            while a >= 0 and b >= 0:
                if[a, b] not in excludes.values():
                    ex.add([a, b])
                a -= 1
                b -= 1

            a, b = i, j
            while a < n and b < n:
                if[a, b] not in excludes.values():
                    ex.add([a, b])
                a += 1
                b += 1

            excludes[(i, j)] = ex

        def dfs(i):
            # find a solution
            if i == n:
                for key in excludes:
                    l = ["."] * n
                    l[key[1]] = 'Q'
                    res[key[0]] = l


            for j in range(n):
                if [i, j] not in excludes.values():
                    # take [i, j] as queen's placement, add [i,j]'s excluded spaces into excludes
                    calc_excludes(i, j)
                    dfs(i+1)
                    excludes.pop((i, j), None)

        dfs(0)
        return res
