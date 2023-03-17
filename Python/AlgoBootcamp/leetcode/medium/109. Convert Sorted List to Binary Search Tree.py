# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a
# height-balanced
#  binary search tree.
#
#
#
# Example 1:
#
#
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
# Example 2:
#
# Input: head = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in head is in the range [0, 2 * 104].
# -105 <= Node.val <= 105
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        result = []
        arr = []
        h = head
        while h:
            arr.append(h.val)
            h = h.next

        def constructTree(L, R) -> Optional[TreeNode]:
            if L > R:
                return None
            mid = (L + R) // 2
            resultNode = TreeNode(arr[mid])
            resultNode.left = constructTree(L, mid - 1)
            resultNode.right = constructTree(mid + 1, R)
            return resultNode

        return constructTree(0, len(arr) - 1)


ln = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol = Solution()
res = sol.sortedListToBST(ln)
assert res.val == 2
assert res.left.val == 1
assert res.right.val == 3
