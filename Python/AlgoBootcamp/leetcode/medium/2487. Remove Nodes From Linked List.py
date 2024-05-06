# You are given the head of a linked list.
#
# Remove every node which has a node with a greater value anywhere to the right side of it.
#
# Return the head of the modified linked list.
#
#
#
# Example 1:
#
#
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.
# Example 2:
#
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.
#
#
# Constraints:
#
# The number of the nodes in the given list is in the range [1, 105].
# 1 <= Node.val <= 105
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverseNodes(head)
        head = self.createIncreasing(head)
        return self.reverseNodes(head)

    def createIncreasing(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = head
        while cur:
            curMax = cur.val
            nextNode = cur.next
            while nextNode and nextNode.val < curMax:
                nextNode = nextNode.next
            cur.next = nextNode
            cur = cur.next
        return dummy.next

    def reverseNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


sol = Solution()
head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
newHead = sol.removeNodes(head)
assert newHead.val == 13
assert newHead.next.val == 8
assert newHead.next.next is None

head = ListNode(1, ListNode(1, ListNode(1, ListNode(1))))
newHead = sol.removeNodes(head)
assert newHead.val == 1
assert newHead.next.val == 1
assert newHead.next.next.val == 1
assert newHead.next.next.next.val == 1
assert newHead.next.next.next.next is None
