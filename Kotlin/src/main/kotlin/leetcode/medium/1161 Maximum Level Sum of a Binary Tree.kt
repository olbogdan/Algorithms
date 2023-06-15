package leetcode.medium
/*Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.



Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2


Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105*/
import java.util.*

private class `1161 Maximum Level Sum of a Binary Tree` {
    fun maxLevelSum(root: TreeNode?): Int {
        var maxLevelSum = root?.`val` ?: 0
        var maxLevelNumber = 1
        val stack = Stack<TreeNode>()
        root?.let { stack.push(it) }
        var levelNumber = 1
        while (stack.isNotEmpty()) {
            var levelSum = 0
            val size = stack.size
            for (i in 0 until size) {
                val node = stack.removeFirst()
                levelSum += node.`val`
                node.left?.let {
                    stack.push(it)
                }
                node.right?.let {
                    stack.push(it)
                }
            }
            if (levelSum > maxLevelSum) {
                maxLevelSum = levelSum
                maxLevelNumber = levelNumber
            }
            levelNumber++
        }
        return maxLevelNumber
    }
}


/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 */
private data class TreeNode(var `val`: Int, var left: TreeNode? = null, var right: TreeNode? = null) {
}


fun main() {
    val root = TreeNode(900, null, TreeNode(10250, TreeNode(98693), TreeNode(-89388, TreeNode(-32127))))
    val solution = `1161 Maximum Level Sum of a Binary Tree`()
    val result = solution.maxLevelSum(root)
    require(result == 2)
}
