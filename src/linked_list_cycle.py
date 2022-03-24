# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = p2 = head

        while True:
            p1 = p1.next if p1 is not None else None

            p2 = p2.next if p2 is not None else None
            p2 = p2.next if p2 is not None else None

            if p1 is None and p2 is None:
                return False
            elif p1 == p2:
                return True

