
import Foundation

/**
 Given the root of a binary tree, return the maximum width of the given tree.

 The maximum width of a tree is the maximum width among all levels.

 The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-nil nodes), where the nil nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

 It is guaranteed that the answer will in the range of a 32-bit signed integer.
 */


public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}


func widthOfBinaryTree(_ root: TreeNode?) -> Int {
    if root == nil {
        return 0
    }
    var maxWidth = 0
    var deque: [(TreeNode, Int)] = [(root!, 1)]
    while !deque.isEmpty {
        let (_, indexL) = deque.first!
        let (_, indexR) = deque.last!
        maxWidth = max(indexR - indexL + 1, maxWidth)

        var newDeque: [(TreeNode, Int)] = []
        while deque.count > 0 {
            let (nodeL, indexL) = deque.removeFirst()
            if nodeL.left != nil {
                newDeque.append((nodeL.left!, indexL*2))
            }
            if nodeL.right != nil {
                newDeque.append((nodeL.right!, indexL*2+1))
            }
        }
        deque = newDeque


    }
    return maxWidth
}


var node = TreeNode(10)
let leftNode1 = TreeNode(1)
leftNode1.left = TreeNode(0)
node.left = leftNode1

let rightNode1 = TreeNode(12)
rightNode1.left = TreeNode(11)
rightNode1.right = TreeNode(22)

node.right = rightNode1

assert(widthOfBinaryTree(node) == 4)

leftNode1.left = nil
assert(widthOfBinaryTree(node) == 2)

leftNode1.right = TreeNode(7)
assert(widthOfBinaryTree(node) == 3)

node = TreeNode(10)
assert(widthOfBinaryTree(node) == 1)

assert(widthOfBinaryTree(nil) == 0)
