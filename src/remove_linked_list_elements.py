from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy.next
        previous = dummy

        while(head):
            if head.val == val:
                previous.next = head.next
                head = head.next
            else:
                previous = head
                head = head.next

        return dummy.next