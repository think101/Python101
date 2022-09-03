from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target+1):
            sum = 0
            for j in nums:
                if i - j < 0:
                    break

                sum += dp[i - j]

            dp[i] = sum

        return dp[target]


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum4([1, 2, 3], 4))
    print(s.combinationSum4([9], 3))
