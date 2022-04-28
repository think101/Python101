from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev, cur, ne = None, head, head.next

        while ne:
            t = ne.next
            cur.next = prev
            ne.next = cur

            prev = cur
            cur = ne
            ne = t

        return cur


def print_list(head: Optional[ListNode]):
    while head:
        print(head.val)
        head = head.next

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print_list(s.reverseList(head))
