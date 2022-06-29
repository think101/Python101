from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while(j < k):
                t = nums[i] + nums[j] + nums[k]
                if abs(t - target) < abs(result - target):
                    result = t

                if t < target:
                    j += 1
                else:
                    k -= 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([1, 1, 1, 1], 3))
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([1, 1, 1, 1], 3))
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([1, 1, 1, 1], 3))
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([1, 1, 1, 1], 3))
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([1, 1, 1, 1], 3))
