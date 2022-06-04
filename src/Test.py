import bisect


def test_bisect():
    print("test_bisect")
    dp = [[2, 0], [3, 10], [6, 20], [99, 30]]
    i = bisect.bisect(dp, [6])
    print(i)
    i = bisect.bisect(dp, [7])
    print(i)
    i = bisect.bisect(dp, [5])
    print(i)
    i = bisect.bisect(dp, [1])
    print(i)


class Solution:
    pass


t = Solution()
test_bisect()
