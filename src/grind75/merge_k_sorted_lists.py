from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

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
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    l = [l1, l2, l3]
    print_list(s.mergeKLists(l))
