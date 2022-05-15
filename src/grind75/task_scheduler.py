import collections
from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)

        heap = [-cnt for cnt in freq.values()]
        heapify(heap)
        q = []

        t = 0  # time
        while heap or q:
            if q and q[0][1] == t:
                heappush(heap, q[0][0])
                q.pop(0)

            if heap:
                elem = heappop(heap)
                elem += 1
                if elem != 0:
                    q.append([elem, t + 1 + n])

            t += 1

        return t


t = Solution()
print(t.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(t.leastInterval(["A", "A", "A", "B", "B", "B"], 0))
print(t.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
