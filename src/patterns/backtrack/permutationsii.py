from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        nums.sort()
        res = []
        for i in range(len(nums)):
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1

            perms = self.permuteUnique(nums[:i] + nums[i+1:])
            for perm in perms:
                res.append(perm[::].append(nums[i]))

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
