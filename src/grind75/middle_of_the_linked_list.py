from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next if fast else None

        return slow


t = ListNode(1)
t.next = ListNode(2)
t.next.next = ListNode(3)
t.next.next.next = ListNode(4)
t.next.next.next.next = ListNode(5)
print(Solution().middleNode(t).val)
t.next.next.next.next.next = ListNode(6)
print(Solution().middleNode(t).val)