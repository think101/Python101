from heapq import heapify, heappush, heappop


class MedianFinder:

    def __init__(self):
        self.min_q = []
        heapify(self.min_q)
        self.max_q = []
        heapify(self.max_q)

    def addNum(self, num: int) -> None:
        heappush(self.max_q, num * -1)

        if self.min_q and self.max_q and self.max_q[0] * -1 > self.min_q[0]:
            heappush(self.min_q, heappop(self.max_q) * -1)

        if len(self.max_q) > len(self.min_q) + 1:
            heappush(self.min_q, heappop(self.max_q) * -1)
        elif len(self.min_q) > len(self.max_q) + 1:
            heappush(self.max_q, heappop(self.min_q) * -1)

    def findMedian(self) -> float:
        if len(self.max_q) > len(self.min_q):
            return self.max_q[0] * -1
        elif len(self.max_q) < len(self.min_q):
            return self.min_q[0]
        else:
            return (self.min_q[0] + self.max_q[0] * -1) / 2


if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    mf.addNum(3)
    print(mf.findMedian())
    mf.addNum(4)
    print(mf.findMedian())
    mf.addNum(5)
    print(mf.findMedian())
