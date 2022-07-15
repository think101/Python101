class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, pDiag, nDiag = set(), set(), set()  # used columns, positive diagonals, negative diagonals
        res = 0

        def dfs(i):
            nonlocal res
            if i == n:
                res += 1
                return

            for j in range(n):
                if j not in cols and i - j not in nDiag and i + j not in pDiag:
                    cols.add(j)
                    pDiag.add(i + j)
                    nDiag.add(i - j)
                    dfs(i+1)

                    cols.remove(j)
                    pDiag.remove(i+j)
                    nDiag.remove(i-j)

        dfs(0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens(4))
    print(s.totalNQueens(8))
