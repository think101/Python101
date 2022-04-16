class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        n = sorted(self.nums)
        if len(n) % 2 == 0:
            l, r = int(len(n) / 2) - 1, int(len(n) / 2)
            return (n[l] + n[r]) / 2
        else:
            return n[int((len(n) - 1) / 2)]
