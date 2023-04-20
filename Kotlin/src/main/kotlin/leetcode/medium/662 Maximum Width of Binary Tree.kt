package leetcode.medium
/*Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.



Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).


Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100*/


class `662 Maximum Width of Binary Tree` {
    class TreeNode(var `val`: Int) {
        var left: TreeNode? = null
        var right: TreeNode? = null
    }
    fun widthOfBinaryTree(root: TreeNode?): Int {
        val deq = ArrayDeque<TreeNode>()
        root?.let {
            it.`val` = 0
            deq.add(it)
        }
        var result = 0
        while (deq.isNotEmpty()) {
            val levelWidth = deq.last().`val` - deq.first().`val` + 1
            result = maxOf(result, levelWidth)
            repeat(deq.size) {
                val node = deq.removeFirst()
                node.left?.let {
                    it.`val` = node.`val` * 2 + 1
                    deq.add(it)
                }
                node.right?.let {
                    it.`val` = node.`val` * 2 + 2
                    deq.add(it)
                }
            }
        }
        return result
    }
}
