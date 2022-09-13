from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        s = set()

        def dfs(visited, i):
            if i == len(nums):
                s.add(tuple(visited[::]))
                return

            # include
            visited.append(nums[i])
            dfs(visited, i + 1)
            visited.pop()

            # not include ith elem
            dfs(visited, i + 1)

        dfs([], 0)

        res = []
        for t in s:
            res.append(list(t))

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))
    print(s.subsetsWithDup([1, 2, 2, 3]))
    print(s.subsetsWithDup([1, 2, 2, 3, 4]))
    print(s.subsetsWithDup([1, 2, 2, 3, 4, 5]))
