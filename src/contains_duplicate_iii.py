from typing import List

from sortedcontainers import SortedDict


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # num to count
        sd = SortedDict()
        l = min(len(nums), k)

        for i in range(l+1):
            if nums[i] not in sd:
                sd[nums[i]] = 0

            sd[nums[i]] += 1
            ind = sd.keys().index(nums[i])
            if (ind - 1 >= 0 and abs(nums[i] - nums[ind - 1]) <= t) or (sd[nums[i]] > 1 and t == 0) or (ind + 1 <= l and abs(nums[i] - nums[ind + 1]) <= t):
                return True

        i = l+1
        while i < len(nums):
            sd[nums[i - k - 1]] -= 1
            if sd[nums[i - k]] == 0:
                del sd[nums[i - k]]

            if nums[i] not in sd:
                sd[nums[i]] = 0

            sd[nums[i]] += 1
            ind = sd.keys().index(nums[i])
            if (ind - 1 >= 0 and abs(nums[i] - nums[ind - 1]) <= t) or (sd[nums[i]] > 1 and t == 0) or (ind + 1 <= l and abs(nums[i] - nums[ind + 1]) <= t):
                return True

            i += 1

        return False


t = Solution()
# print(t.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
# print(t.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
# print(t.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
# print(t.containsNearbyAlmostDuplicate([1, 2, 5, 6, 7, 2, 4], 4, 0))

