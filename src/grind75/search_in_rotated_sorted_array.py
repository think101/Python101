from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        def b_search(l, r, target):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        # decide which part middle belongs to
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:  # left part
                    return b_search(l, m - 1, target)
                else:
                    l = m + 1
            elif nums[m] <= nums[r]:
                if nums[r] >= target > nums[m]:  # right part
                    return b_search(m + 1, r, target)
                else:
                    r = m - 1

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 1))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 2))
