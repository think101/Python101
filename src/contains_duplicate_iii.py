from typing import List

from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sl = SortedList()

        for i in range(len(nums)):
            if i > k:
                sl.remove(nums[i-k-1])

            sl.add(nums[i])
            ind = sl.index(nums[i])

            if (ind - 1 >= 0 and abs(sl[ind-1] - sl[ind]) <= t) or (ind + 1 < len(sl) and abs(sl[ind+1] - sl[ind]) <= t):
                return True

        return False


t = Solution()
print(t.containsNearbyAlmostDuplicate([-3, 3, -6], 2, 3))
print(t.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
print(t.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
print(t.containsNearbyAlmostDuplicate([1, 2, 5, 6, 7, 2, 4], 4, 0))
