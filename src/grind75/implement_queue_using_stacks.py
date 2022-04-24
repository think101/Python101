class MyQueue:

    def __init__(self):
        self.q1, self.q2 = [], []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        for i in range(len(self.q1)):
            self.q2.append(self.q1.pop())

        t = self.q2.pop()

        for i in range(len(self.q2)):
            self.q1.append(self.q2.pop())

        return t

    def peek(self) -> int:
        for i in range(len(self.q1)):
            self.q2.append(self.q1.pop())

        t = self.q2[len(self.q2) - 1]

        for i in range(len(self.q2)):
            self.q1.append(self.q2.pop())

        return t

    def empty(self) -> bool:
        return len(self.q1) == 0


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

    print(q.empty())