# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
#
#
# Example 1:
#
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:
#
# Input: head = [2,1], x = 2
# Output: [1,2]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class NodeHolder:
    def __init__(self):
        self.last = None
        self.first = None

    def addNode(self, node: ListNode):
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def getFirst(self) -> Optional[ListNode]:
        return self.first


class NodeHolder:
    def __init__(self):
        self.last = None
        self.first = None

    def addNode(self, node: ListNode):
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def getFirst(self) -> Optional[ListNode]:
        return self.first


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftHolder = NodeHolder()
        rightHolder = NodeHolder()

        while head:
            if head.val < x:
                leftHolder.addNode(head)
            elif head.val >= x:
                rightHolder.addNode(head)
            prev = head
            head = head.next
            prev.next = None

        self.addAll(rightHolder, leftHolder)
        return leftHolder.first

    def addAll(self, fromHolder: NodeHolder, toHolder: NodeHolder):
        head = fromHolder.first
        while head:
            toHolder.addNode(head)
            head = head.next

head = ListNode(6, ListNode(2, ListNode(3)))
sol = Solution()
result = sol.partition(head, 3)
assert result.val == 2
assert result.next.val == 6
assert result.next.next.val == 3
