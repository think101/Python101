# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        first = second = dummy

        for i in range(n):
            first = first.next

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

