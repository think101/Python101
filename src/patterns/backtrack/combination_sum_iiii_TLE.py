from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []

        def dfs(target, visited):
            if target == 0:
                res.append(visited[::])
                return
            if target < 0:
                return

            for i in nums:
                visited.append(i)
                dfs(target - i, visited)
                visited.pop()

        dfs(target, [])
        return len(res)


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum4([1, 2, 3], 4))
    print(s.combinationSum4([9], 3))
