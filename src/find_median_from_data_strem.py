import heapq


class MedianFinder:

    def __init__(self):
        # min_h for large part, max_h for small part
        self.min_h, self.max_h = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_h, -1 * num)

        # if max_h max value > min_h min value, move max_h top to min_h
        if self.max_h and self.min_h and -1 * self.max_h[0] > self.min_h[0]:
            value = -1 * heapq.heappop(self.max_h)
            heapq.heappush(self.min_h, value)

        # if size not even
        if len(self.min_h) > len(self.max_h) + 1:
            value = -1 * heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, value)
        elif len(self.max_h) > len(self.min_h) + 1:
            value = -1 * heapq.heappop(self.max_h)
            heapq.heappush(self.min_h, value)

    def findMedian(self) -> float:
        if len(self.min_h) > len(self.max_h):
            return self.min_h[0]
        elif len(self.max_h) > len(self.min_h):
            return -1 * self.max_h[0]
        else:
            return (-1 * self.max_h[0] + self.min_h[0]) / 2


if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())
    mf.addNum(3)
    print(mf.findMedian())

