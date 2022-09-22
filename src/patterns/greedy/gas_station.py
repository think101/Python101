from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        cnt = len(gas)
        total = 0
        res = 0

        for i in range(cnt):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([4, 5, 3, 1, 4], [5, 4, 3, 4, 2]))
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(s.canCompleteCircuit([2], [2]))
