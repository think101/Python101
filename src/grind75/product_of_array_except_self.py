from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        l1, l2, res = [0 for _ in range(length)], [0 for _ in range(length)], [0 for _ in range(length)]

        for i in range(length):
            l1[i] = l1[i-1] * nums[i] if i-1 >= 0 else nums[i]
            l2[length-1-i] = l2[length-i] * nums[length-1-i] if length-i < length else nums[length-1-i]

        for i in range(length):
            res[i] = 1
            res[i] = l1[i-1] * res[i] if i-1 >= 0 else res[i]
            res[i] = l2[i+1] * res[i] if i+1 < length else res[i]

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
    print(s.productExceptSelf([1, 2, 3, 4, 5]))
