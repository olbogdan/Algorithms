# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
#
# Return the head of the linked list after doubling it.
#
#
#
# Example 1:
#
#
# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
# Example 2:
#
#
# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 104]
# 0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        head = self.doubleHelper(head)
        return self.reverse(head)

    def doubleHelper(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy.next = head
        prev = None
        while cur:
            prev = cur
            val = cur.val * 2 + carry
            if val > 9:
                val = val % 10
                carry = 1
            else:
                carry = 0
            cur.val = val
            cur = cur.next
        if carry != 0:
            prev.next = ListNode(val=1)
        return dummy.next

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


sol = Solution()
head = ListNode(1, ListNode(8, ListNode(9)))
newHead = sol.doubleIt(head)
assert newHead.val == 3
assert newHead.next.val == 7
assert newHead.next.next.val == 8
assert newHead.next.next.next is None
