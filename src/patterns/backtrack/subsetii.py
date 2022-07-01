from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))
    print(s.subsetsWithDup([1, 2, 2, 3]))
    print(s.subsetsWithDup([1, 2, 2, 3, 4]))
    print(s.subsetsWithDup([1, 2, 2, 3, 4, 5]))
