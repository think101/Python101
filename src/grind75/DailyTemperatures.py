from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                res[stack.pop()] = i - stack[-1]
            stack.append(i)
        return res

    def dailyTemperatures_MINE(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        q, res = [0] * l, [0] * l
        top = -1

        for i in range(l):
            while top >= 0 and temperatures[i] > temperatures[q[top]]:
                res[q[top]] = i - q[top]
                top -= 1

            top += 1
            q[top] = i

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
