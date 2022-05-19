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
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, key):
        n = self.d[key]
        n.prev.next = n.next
        n.next.prev = n.prev
        n.next = None
        n.prev = None

    def add(self, key):
        n = self.d[key]
        n.prev = self.right.prev
        n.next = self.right
        self.right.prev.next = n
        self.right.prev = n

    def delete(self, key):
        self.remove(key)
        self.d.pop(key, None)

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        self.remove(key)
        self.add(key)

        return self.d[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].value = value
            self.remove(key)
            self.add(key)
            return

        self.d[key] = Node(key, value)
        self.add(key)

        if len(self.d) > self.c:
            self.delete(self.left.next.key)


t = LRUCache(2)
print(t.get(2))
t.put(2, 6)
print(t.get(1))
t.put(1, 5)
t.put(1, 2)
print(t.get(1))
print(t.get(2))

