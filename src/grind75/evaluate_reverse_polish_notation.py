from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []

        for i in range(len(tokens)):
            t = tokens[i]
            if t in ["+", "-", "*", "/"]:
                op1, op2 = int(q.pop(0)), int(q.pop(0))
                if t == "+":
                    q.insert(0, op2 + op1)
                elif t == "-":
                    q.insert(0, op2 - op1)
                elif t == "*":
                    q.insert(0, op2 * op1)
                else:
                    q.insert(0, int(op2 / op1))
            else:
                q.insert(0, t)

            if i == len(tokens) - 1:
                return q.pop(0)


if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    print(s.evalRPN(["4", "13", "5", "/", "+"]))

