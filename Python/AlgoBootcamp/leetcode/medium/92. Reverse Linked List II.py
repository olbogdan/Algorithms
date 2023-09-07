# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:
#
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
#
# Constraints:
#
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
# Follow up: Could you do it in one pass?
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        endOfLeftHalf = None
        startReverse = head
        i = 1
        while startReverse and i != left:
            endOfLeftHalf = startReverse
            startReverse = startReverse.next
            i += 1

        endReverse = startReverse
        while endReverse and i != right:
            endReverse = endReverse.next
            i += 1
        beginingOfRightHalf = endReverse.next

        prev = startReverse
        cur = startReverse.next
        while cur != beginingOfRightHalf:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        startReverse.next = beginingOfRightHalf
        if endOfLeftHalf:
            endOfLeftHalf.next = endReverse
        else:
            head = endReverse
        return head


node = ListNode(10, ListNode(2, ListNode(3, ListNode(4))))
sol = Solution()
res = sol.reverseBetween(node, 1,4)
assert res.val == 4


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # edge case when left == 1 positoion, then "right" should be the result
        # if left == 1:
        #   resultNode = right else head
        if left == right:
            return head
        cur = head
        endOfFirstHalf = None
        i = 1
        while i != left:
            endOfFirstHalf = cur
            cur = cur.next
            i += 1
        beginOfReverse = cur

        prev = cur
        cur = cur.next
        i += 1
        while i != right + 1:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            i += 1

        beginOfReverse.next = cur
        if endOfFirstHalf:
            endOfFirstHalf.next = prev
            return head
        else:
            return prev