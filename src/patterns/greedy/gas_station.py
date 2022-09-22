from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1

        cnt = len(gas)
        remains = [0] * cnt
        positives = []

        for i in range(cnt):
            remains[i] = gas[i] - cost[i]
            if remains[i] > 0:
                positives.append(i)

        for i in range(len(positives)):
            ind = positives[i]
            total = 0

            j = ind
            for j in range(ind, cnt):
                total += remains[j]

                if (total <= 0 and j < cnt - 1) or (total < 0 and j == cnt - 1):
                    break

            if total >= 0 and j == cnt - 1:
                return positives[i]

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([4, 5, 3, 1, 4], [5, 4, 3, 4, 2]))
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(s.canCompleteCircuit([2], [2]))
