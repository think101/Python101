from typing import List, Optional
from sortedcontainers import SortedDict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sd = SortedDict()  # node value ot list of nodes

        for n in lists:
            if n:
                if n.val not in sd:
                    sd[n.val] = []
                sd[n.val].append(n)

        dummy = ListNode(0)
        current = dummy

        while sd:
            print("len:" + str(len(sd)))
            for key in sd:
                for n in sd[key]:
                    print_list(n)

            key, node_list = sd.popitem(0)
            t = node_list.pop(0)
            current.next = t
            current = t

            if t.next:
                if t.next.val not in sd:
                    sd[t.next.val] = []

                sd[t.next.val].append(t.next)

            current.next = None

            if len(node_list) > 0:
                if node_list[0].val not in sd:
                    sd[node_list[0].val] = []
                sd[node_list[0].val].extend(node_list)

        return dummy.next

    def mergeKLists_TLE(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(0)
        c_node = dummy

        while lists:
            current = -1
            for i in range(len(lists)):
                if lists[i]:
                    if current < 0 or lists[i].val < lists[current].val:
                        current = i

            if current >= 0:
                c_node.next = lists[current]
                lists[current] = lists[current].next

                if not lists[current]:
                    del lists[current]

                c_node = c_node.next
                c_node.next = None
            else:
                break

        return dummy.next


def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(2)
    l2 = ListNode(1)
    l2.next = ListNode(1)
    l2.next.next = ListNode(2)

    l = [l1, l2]
    print_list(s.mergeKLists(l))
