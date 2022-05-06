class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d.setdefault(key, [])
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        length = len(self.d[key])
        l, r = 0, length - 1

        res = ""
        while l <= r:
            m = (l + r) // 2
            if self.d[key][m][0] == timestamp:
                return self.d[key][m][1]
            elif self.d[key][m][0] > timestamp:
                r = m - 1
            else:
                res = self.d[key][m][1]
                l = m + 1

        return res


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
