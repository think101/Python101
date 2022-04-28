class MinStack:

    def __init__(self):
        self.s, self.ms = [], []


    def push(self, val: int) -> None:
        self.s.insert(0, val)
        self.ms.insert(0, min(self.ms[0], val)) if self.ms else self.ms.insert(0, val)

    def pop(self) -> None:
        self.s.pop(0)
        self.ms.pop(0)

    def top(self) -> int:
        return self.s[0]


    def getMin(self) -> int:
        return self.ms[0]


t = MinStack()
t.push(1)
t.push(2)
print(t.getMin())
t.push(0)
print(t.getMin())
t.pop()
print(t.getMin())
t.pop()
print(t.getMin())


# note min stack is different from min heap
