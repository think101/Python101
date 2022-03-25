from typing import List, Optional
from sortedcontainers import SortedDict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sd = SortedDict()
        dummy = ListNode(-1, None)
        current = dummy

        for li in lists:
            if li is not None:
                if li.val in sd:
                    sd.get(li.val).append(li)
                else:
                    sd.setdefault(li.val, [li])

        while sd:
            node_list = sd.pop(sd.keys()[0])
            current.next = node_list.pop(0)
            if len(node_list) > 0:
                sd.setdefault(node_list[0].val, node_list)
            current = current.next

            if current.next is not None:
                if current.next.val in sd:
                    sd.get(current.next.val).append(current.next)
                else:
                    sd.setdefault(current.next.val, [current.next])
            current.next = None

        return dummy.next

