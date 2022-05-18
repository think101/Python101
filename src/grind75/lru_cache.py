class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.c = capacity
        self.left = None
        self.right = None

    def get(self, key: int) -> int:
        if not self.d or key not in self.d:
            return -1

        t = self.left
        while t and t.key != key:
            t = t.next

        if t.prev:
            t.prev.next = t.next
        if t.next:
            t.next.prev = t.prev

        self.right.next = t
        t.prev = self.right
        t.next = None
        self.right = t

        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value

        if len(self.d) < self.c:
            self.d[key] = value
        else:
            self.d.pop(self.left.key, None)

            self.right.next = Node(key, value)
            self.right.next.prev = self.right
            self.right = self.right.next

            if self.c == 1:
                self.left = self.right
                self.left.prev = None
            else:
                self.left.next.prev = None
                self.left = self.left.next


t = LRUCache(2)
t.put(1, 1)
t.put(2, 2)
print(t.get(1))

