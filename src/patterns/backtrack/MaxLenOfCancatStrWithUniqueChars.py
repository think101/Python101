from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = ""

        def dfs(i, curr):
            nonlocal res
            if i == len(arr):
                return len(res)

            for j in range(i, len(arr)):
                curr += arr[j]
                if len(set(curr)) == len(curr) and len(curr) > len(res):
                    res = curr
                    dfs(j+1, curr)
                curr = curr[:-len(arr[j])]

        dfs(0, "")
        return len(res)


if __name__ == "__main__":
    s = Solution()
    print(s.maxLength(["a", "abc", "d", "de", "def"]))

