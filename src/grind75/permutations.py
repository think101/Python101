from typing import List


class Solution:
    def permute_dfs(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(depth, n, used, curr):
            if depth == n:
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    dfs(depth + 1, n, used, curr)
                    used[i] = False
                    curr.pop()

        dfs(0, len(nums), [False] * len(nums), [])
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            t = self.permute(nums[:i] + nums[i+1:])
            for x in t:
                res.append([nums[i]] + x)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))
