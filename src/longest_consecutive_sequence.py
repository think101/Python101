from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            a[i] = 1

        result = 0
        for i in nums:
            if a[i] == 0:
                continue

            length = 1
            t = i
            a[i] = 0
            while t-1 in a:
                length += 1
                t -= 1
                a[t] = 0
            t = i
            while t+1 in a:
                length += 1
                t += 1
                a[t] = 0
            if length > result:
                result = length

        return result


t = Solution()
print(t.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(t.longestConsecutive([1, 2, 0, 1]))
print(t.longestConsecutive([0, -1, 2, 6, 9]))

