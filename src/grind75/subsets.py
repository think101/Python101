from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(n, start, path):
            if len(path) == n:
                res.append(path.copy())
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(n, i + 1, path)
                path.pop()

        for i in range(len(nums) + 1):
            dfs(i, 0, [])

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
    print(s.subsets([1, 2, 3, 4]))
