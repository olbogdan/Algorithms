#You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# Constraints:
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        cur = result
        memo = 0
        while l1 or l2:
            l1val = 0
            if l1:
                l1val = l1.val
            l2val = 0
            if l2:
                l2val = l2.val
            newVal = l1val + l2val + memo
            if newVal > 9:
                memo = 1
            else:
                memo = 0
            newVal = newVal % 10

            node = ListNode()
            node.val = newVal
            cur.next = node
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if memo == 1:
            cur.next = ListNode(1)
        return result.next


solution = Solution2()
l1 = ListNode(1)
l2 = ListNode(2)
l2.next = ListNode(5)
result = solution.addTwoNumbers(l1, l2)
assert result.val == 3
assert result.next.val == 5

solution = Solution2()
l1 = ListNode(9)
l2 = ListNode(9)
result = solution.addTwoNumbers(l1, l2)
assert result.val == 8
assert result.next.val == 1
