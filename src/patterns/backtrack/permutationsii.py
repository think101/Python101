from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        nums.sort()
        res = []
        i = 0
        while i < len(nums):  # since I need to change i while looping, I use while loop instead of for loop
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1

            perms = self.permuteUnique(nums[:i] + nums[i + 1:])
            for perm in perms:
                res.append(perm + [nums[i]])

            i += 1

        return res



if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
