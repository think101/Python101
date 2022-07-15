class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, pDiag, nDiag = [], [], []  # used columns, positive diagonals, negative diagonals
        res = 0

        def dfs(i):
            nonlocal res
            if i == n:
                res += 1
                return

            for j in range(n):
                if j not in cols and i - j not in nDiag and i + j not in pDiag:
                    cols.append(j)
                    pDiag.append(i + j)
                    nDiag.append(i - j)
                    dfs(i+1)

                    cols.pop()
                    pDiag.pop()
                    nDiag.pop()

        dfs(0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens(4))
    print(s.totalNQueens(8))
