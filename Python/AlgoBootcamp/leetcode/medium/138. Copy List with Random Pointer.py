# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
#
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
#
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
#
# Return the head of the copied linked list.
#
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.
# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
# Constraints:
# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Runtime: 35 ms, faster than 96.58% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 14.8 MB, less than 83.27% of Python3 online submissions for Copy List with Random Pointer.
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # We can avoid using extra space for old_node ---> new_node mapping
        # by tweaking the original linked list. Simply interweave the nodes of
        # the old and copied list. For example: Old List: A --> B --> C --> D
        # InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
        if head is None:
            return None

        temp = head
        while temp:
            node = Node(temp.val)
            node.next = temp.next
            temp.next = node
            temp = node.next

        temp = head
        while temp:
            copy = temp.next

            cur = copy.next

            if temp.random:
                copy.random = temp.random.next
            if copy.next:
                copy.next = copy.next.next
            temp = cur

        return head.next


solution = Solution()
root = Node(1)
root.next = Node(2)
n3 = Node(3)
root.next.next = n3
root.random = n3
node = solution.copyRandomList(root)
assert node.val == 1
assert node.next.val == 2
assert node.random.val == 3

empty = solution.copyRandomList(None)
assert empty is None


class Solution1:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # use a node  as a key of a map
        # iterate head and fill a map with node:newNodeRef
        # iterate second time and set links between new items
        if head is None:
            return None
        reference = {}
        temp = head
        while temp:
            node = Node(temp.val)
            reference[temp] = node
            temp = temp.next

        temp = head
        while temp:
            node = reference[temp]
            if temp.next:
                node.next = reference[temp.next]
            if temp.random:
                node.random = reference[temp.random]
            temp = temp.next
        return reference[head]


solution = Solution1()
root = Node(1)
root.next = Node(2)
n3 = Node(3)
root.next.next = n3
root.random = n3
node = solution.copyRandomList(root)
assert node.val == 1
assert node.next.val == 2
assert node.random.val == 3

empty = solution.copyRandomList(None)
assert empty is None