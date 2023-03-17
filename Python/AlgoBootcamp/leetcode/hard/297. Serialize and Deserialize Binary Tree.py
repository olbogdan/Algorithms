#Serialization is the process of converting a data structure or object into a sequence
# of bits so that it can be stored in a file or memory buffer, or transmitted across
# a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and this string can
# be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
# You do not necessarily need to follow this format, so please be creative and come up with
# different approaches yourself.
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:
#
# Input: root = []
# Output: []
# # Your Codec object will be instantiated and called as such:
# # ser = Codec()
# # deser = Codec()
# # ans = deser.deserialize(ser.serialize(root))


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return "N"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + "," + left + "," + right

    def deserialize(self, data):
        array = data.split(",")
        return self.buildTree(array)

    def buildTree(self, array):
        rootVal = array.pop(0)
        if rootVal == "N":
            return None
        left = self.buildTree(array)
        right = self.buildTree(array)
        node = TreeNode(rootVal)
        node.left = left
        node.right = right
        return node


root = TreeNode(5)
left = TreeNode(1)
right = TreeNode(10)
rightRight = TreeNode(20)
root.left = left
root.right = right
right.right = rightRight
codec = Codec()
serialized = codec.serialize(root)
assert serialized == "5,1,N,N,10,N,20,N,N"
tree = codec.deserialize(serialized)
assert tree.val == "5"
