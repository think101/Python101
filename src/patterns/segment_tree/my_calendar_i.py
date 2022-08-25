from sortedcontainers import SortedDict


class MyCalendar:

    def __init__(self):
        self.events = SortedDict()

    def book(self, start: int, end: int) -> bool:
        if len(self.events) == 0:
            self.events[start] = end
            return True

        bi_left = self.events.bisect_left(start)
        if (bi_left - 1 >= 0 and start < self.events[self.events.iloc[bi_left - 1]]) \
                or (bi_left < len(self.events) and end > self.events.iloc[bi_left]):
            return False

        self.events[start] = end
        return True


if __name__ == "__main__":
    obj = MyCalendar()
    print(obj.book(10, 20))
    print(obj.book(15, 25))
    print(obj.book(20, 30))
