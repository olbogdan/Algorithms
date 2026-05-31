# Given the head of a linked list, rotate the list to the right by k places.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def size(self, head: ListNode) -> int:
        i = 0
        while head:
            i += 1
            head = head.next
        return i

    def getTail(self, head: ListNode) -> ListNode:
        while head.next:
            head = head.next
        return head

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        N = self.size(head)
        shift = k % N
        if shift == 0: return head

        shift = N - shift  # shift from the end

        cur = head
        prev = None
        i = 0
        while i < shift:
            prev = cur
            cur = cur.next
            i += 1

        tail = self.getTail(head)
        prev.next = None
        tail.next = head
        return cur


def build_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


sol = Solution()

# Example 1
head = build_list([1, 2, 3, 4, 5])
assert to_array(sol.rotateRight(head, 2)) == [4, 5, 1, 2, 3]

# Example 2
head = build_list([0, 1, 2])
assert to_array(sol.rotateRight(head, 4)) == [2, 0, 1]

# Edge: empty list
assert sol.rotateRight(None, 5) is None

# Edge: k = 0
head = build_list([1, 2, 3])
assert to_array(sol.rotateRight(head, 0)) == [1, 2, 3]

# Edge: k is multiple of list size
head = build_list([1, 2, 3, 4])
assert to_array(sol.rotateRight(head, 8)) == [1, 2, 3, 4]

# Edge: single node
head = build_list([7])
assert to_array(sol.rotateRight(head, 100)) == [7]
