# Given the head of a linked list, reverse the nodes of the list k at a time,
# and return the modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
#
# Constraints:
#
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
#
#
# Follow-up: Can you solve the problem in O(1) extra memory space?
from typing import Optional

# Runtime: 41 ms, faster than 99.56% of Python3 online submissions for Reverse Nodes in k-Group.
# Memory Usage: 15.2 MB, less than 85.17% of Python3 online submissions for Reverse Nodes in k-Group.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getRight(node):
            if node is None:
                return None
            i = 1
            while i < k and node:
                node = node.next
                i += 1
            return node

        previousGroup = None
        startOfGroup = head
        endOfGroup = result = getRight(startOfGroup)  # last item of a first groupd will be a firest item of result
        print(endOfGroup.val)
        while endOfGroup:
            nextGroupStart = endOfGroup.next  # continue of origin linked list chain

            cur = startOfGroup
            prev = None
            while cur != nextGroupStart:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            if previousGroup:
                previousGroup.next = endOfGroup
            previousGroup = startOfGroup

            endOfGroup = getRight(nextGroupStart)
            startOfGroup = nextGroupStart


            if endOfGroup:
                print(endOfGroup.val)
            else:
                print("endOfGroup is none")

        print(result.val)
        if startOfGroup:
            previousGroup.next = startOfGroup
        return result


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

sol = Solution()
sol.reverseKGroup(node1, 2)