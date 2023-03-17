#Serialization is converting a data structure or object into a sequence
# of bits so that it can be stored in a file or memory buffer,
# or transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# Design an algorithm to serialize and deserialize a binary search tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You need to ensure that a binary search tree can be serialized to a string,
# and this string can be deserialized to the original tree structure.
# The encoded string should be as compact as possible.
# Example 1:
#
# Input: root = [2,1,3]
# Output: [2,1,3]
# Example 2:
#
# Input: root = []
# Output: []
# Constraints:
#
# The number of nodes in the tree is in the range [0, 104].
# 0 <= Node.val <= 104
# The input tree is guaranteed to be a binary search tree.
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        array = []

        def dfs(root):
            if not root:
                array.append("N")
                return
            array.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(array)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        array = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            val = array[i]
            i += 1
            if val == "N":
                return None
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


root = TreeNode(2)
left = TreeNode(1)
right = TreeNode(3)
root.left = left
root.right = right
codec = Codec()
serialized = codec.serialize(root)
assert serialized == "2,1,N,N,3,N,N"
assert codec.deserialize(serialized).val == "2"


