# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    slow = head
    fast = head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


nocycle = ListNode(1, ListNode(2, ListNode(3)))
assert hasCycle(nocycle) is False

cyclen1 = ListNode(1, None)
cyclen2 = ListNode(2, cyclen1)
cyclen1.next = cyclen2
assert hasCycle(cyclen1) is True
