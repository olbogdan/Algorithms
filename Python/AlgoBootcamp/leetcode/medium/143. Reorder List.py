# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
from collections import deque
from typing import Optional


#         Plan of the solution:
#         save head as first to dummy node
#         find middle
#         add [middle:end] to a stack
#         remove middle next
#         iterate first.append top of stack until next exist and stack not empty
#         add leftover from stack
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]) -> None:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow
    queue = deque()
    while mid.next:
        queue.append(mid.next)
        mid = mid.next
    slow.next = None
    first = head
    while first and queue:
        saveTemp = first.next
        first.next = queue.pop()
        first.next.next = saveTemp
        first = first.next.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reorderList(head)
assert head.val == 1
assert head.next.val == 4
assert head.next.next.val == 2
assert head.next.next.next.val == 3


class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        # if odd
        if fast:
            prev = slow
            slow = slow.next

        # detach first half from second
        prev.next = None

        # revert second half
        secondHalf = self.getReverted(slow)

        self.mergeHalfs(head, secondHalf)

    def mergeHalfs(self, first, second):
        while first:
            tempFirst = first.next
            tempSecond = None
            if second:
                tempSecond = second.next
            first.next = second
            if second:
                second.next = tempFirst
            first = tempFirst
            second = tempSecond

    def getReverted(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = node
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


sol = Solution2()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol.reorderList(head)
assert head.val == 1
assert head.next.val == 4
assert head.next.next.val == 2
assert head.next.next.next.val == 3