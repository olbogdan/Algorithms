# You are given the head of a linked list, and an integer k.
#
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:
#
# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
#
#
# Constraints:
#
# The number of nodes in the list is n.
# 1 <= k <= n <= 105
# 0 <= Node.val <= 100
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find first node to swap
        first = head
        for _ in range(1, k):
            first = first.next

        # find second node to swap
        slow = head  # slow is our second node
        fast = first
        while fast.next:
            slow = slow.next
            fast = fast.next

        first.val, slow.val = slow.val, first.val
        return head


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
sol = Solution()
node = sol.swapNodes(node, 5)
assert node.next.next.next.next.val == 6
assert node.next.next.next.next.next.val == 5
