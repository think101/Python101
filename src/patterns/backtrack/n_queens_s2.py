from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pDiag, nDiag = [], [], []  # used columns, positive diagonals, negative diagonals
        curr = []                        # current placements
        res = []

        def dfs(i):
            if i == n:
                res.append(curr[::])
                return

            for j in range(n):
                if j not in cols and i - j not in nDiag and i + j not in pDiag:
                    l = ["."] * n
                    l[j] = 'Q'
                    curr.append("".join(l))

                    cols.append(j)
                    pDiag.append(i + j)
                    nDiag.append(i - j)
                    dfs(i+1)

                    curr.pop()
                    cols.pop()
                    pDiag.pop()
                    nDiag.pop()

        dfs(0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))
    print(s.solveNQueens(8))
