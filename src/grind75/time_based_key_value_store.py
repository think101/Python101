class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.d:
            return self.d[(key, timestamp)]

        l = [(key, timestamp)] + list(self.d.keys())
        l.sort()
        i = l.index((key, timestamp))

        if i == 0:
            return ""

        return self.d[l[i - 1]]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    obj.set("foo", "bar3", 3)
    obj.set("foo", "bar5", 5)
    print(obj.get("foo", 6))
    print(obj.get("foo", 4))
    print(obj.get("foo", 1))
    print(obj.get("foo", 0))
