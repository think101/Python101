from functools import reduce
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bo = reduce(lambda x, y: x | y, nums)
        res = []

        def backtrack(visited, i):
            if len(visited) > 0 and (reduce(lambda x, y: x | y, visited)) == max_bo:
                res.append(visited[::])

            for j in range(i, len(nums)):
                visited.append(nums[j])
                backtrack(visited, j + 1)
                visited.pop()

        backtrack([], 0)
        return len(res)


if __name__ == "__main__":
    s = Solution()
    print(s.countMaxOrSubsets([3, 1]))
    print(s.countMaxOrSubsets([2, 2, 2]))

