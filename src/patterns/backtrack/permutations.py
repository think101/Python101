from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            perms = self.permute(nums[:i] + nums[i + 1:])
            for perm in perms:
                res.append(perm + [nums[i]])

            i += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))

