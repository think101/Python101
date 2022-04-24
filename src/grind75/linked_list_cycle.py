from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(-1)
        dummy.next = head

        fast, slow = dummy, dummy

        while fast and slow:
            fast = fast.next
            if fast == slow:
                return True

            if not fast:
                return False

            fast = fast.next
            slow = slow.next


if __name__ == "__main__":
    s = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = head.next.next

    assert s.hasCycle(head) is True

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = head.next.next

    assert s.hasCycle(head) is True
