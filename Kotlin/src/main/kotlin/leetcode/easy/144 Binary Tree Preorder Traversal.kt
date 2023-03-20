package leetcode.easy

import java.util.*

/*Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?*/


class BTPTSolution {
    class TreeNode(var `val`: Int) {
        var left: TreeNode? = null
        var right: TreeNode? = null
    }
    fun preorderTraversal(root: TreeNode?): List<Int> {
        val result = mutableListOf<Int>()
        fun helper(node : TreeNode?) {
            node ?: return
            result.add(node.`val`)
            helper(node.left)
            helper(node.right)
        }
        helper(root)
        return result
    }
}

class BTPTSolution2 {
    class TreeNode(var `val`: Int) {
        var left: TreeNode? = null
        var right: TreeNode? = null
    }
    fun preorderTraversal(root: TreeNode?): List<Int> {
        val stack = Stack<TreeNode>()
        var current = root
        val result = mutableListOf<Int>()

        while (current != null || !stack.isEmpty()) {
            if (current != null) {
                result.add(current.`val`)
                current.right?.let { stack.push(it) }
                current = current.left
            } else {
                current = stack.pop()
            }
        }

        return result
    }
}