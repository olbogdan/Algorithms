# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummyNode = ListNode(next=head)
    slow = dummyNode
    fast = head
    for i in range(n):
        if not fast:
            break
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummyNode.next


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
assert removeNthFromEnd(node, 5).val == 2

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = removeNthFromEnd(node, 4)
assert result.val == 1
assert result.next.val == 3

