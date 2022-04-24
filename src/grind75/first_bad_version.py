# The isBadVersion API is already defined for you.
# put a dummy function here for compilation
def isBadVersion(version: int) -> bool:
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = int((l + r) / 2)
            if isBadVersion(m):
                if not isBadVersion(m - 1):
                    return m
                else:
                    r = m - 1
            else:
                if isBadVersion(m + 1):
                    return m + 1
                else:
                    l = m + 1
