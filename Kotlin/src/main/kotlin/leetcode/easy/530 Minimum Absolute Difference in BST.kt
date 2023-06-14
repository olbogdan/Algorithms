package leetcode.easy
/*Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
*/
import java.lang.Integer.min


class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class `530 Minimum Absolute Difference in BST` {
    fun getMinimumDifference(root: TreeNode?): Int {
        var prev: Int? = null
        var result = Int.MAX_VALUE

        fun dfs(node: TreeNode?) {
            if (node == null) {
                return
            }
            dfs(node.left)

            prev?.let {prev ->
                result = min(result, node.`val` - prev)
            }
            prev = node.`val`

            dfs(node.right)
        }
        dfs(root)

        return if (result != Int.MAX_VALUE) result else 0
    }
}