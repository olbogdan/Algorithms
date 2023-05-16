# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:
#
# Input: head = []
# Output: []
# Example 3:
#
# Input: head = [1]
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stubNode = ListNode()
        if head and head.next:
            stubNode.next = head.next
        else:
            # check if only one node
            stubNode.next = head

        prev = None
        while head and head.next:
            nextHead = head.next.next

            newFirst = head.next
            newSecond = head

            if prev:
                prev.next = newFirst
            prev = newSecond

            newFirst.next = newSecond
            newSecond.next = nextHead
            head = nextHead

        # handle if num of nodes is odd, link prev to next node
        if prev and head:
            prev.next = head

        return stubNode.next
    