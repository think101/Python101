from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        excludes = {}  # key as placement value as list of excluded spaces

        def calc_excludes(i, j):
            ex = set()
            sums = set(sum(excludes.values(), []))
            # the ith line
            for k in range(n):
                if (i, k) not in sums:
                    ex.add((i, k))

            # the jth column
            for k in range(n):
                if (k, j) not in sums:
                    ex.add((k, j))

            # i++ j--  or i-- j++
            a, b = i, j
            while a < n and b >= 0:
                if (a, b) not in sums:
                    ex.add((a, b))
                a += 1
                b -= 1

            a, b = i, j
            while a >= 0 and b < n:
                if (a, b) not in sums:
                    ex.add((a, b))
                a -= 1
                b += 1

            # i-- j--  or i++ j++
            a, b = i, j
            while a >= 0 and b >= 0:
                if (a, b) not in sums:
                    ex.add((a, b))
                a -= 1
                b -= 1

            a, b = i, j
            while a < n and b < n:
                if (a, b) not in sums:
                    ex.add((a, b))
                a += 1
                b += 1

            excludes[(i, j)] = list(ex)

        def dfs(i):
            # find a solution
            if i == n:
                r = [None for _ in range(n)]
                for key in excludes:
                    l = ["."] * n
                    l[key[1]] = 'Q'
                    r[key[0]] = "".join(l)
                res.append(r)
                return

            for j in range(n):
                #print(i, j, excludes)
                if (i, j) not in sum(excludes.values(), []):
                    # take [i, j] as queen's placement, add [i,j]'s excluded spaces into excludes
                    calc_excludes(i, j)
                    dfs(i+1)
                    excludes.pop((i, j), None)

        dfs(0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))
    print(s.solveNQueens(8))
    print(s.solveNQueens(9))
    print(s.solveNQueens(10))

