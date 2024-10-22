package leetcode.medium

import org.junit.jupiter.api.Assertions.assertTrue

//You are given the root of a binary tree and a positive integer k.
//
//The level sum in the tree is the sum of the values of the nodes that are on the same level.
//
//Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
//
//Note that two nodes are on the same level if they have the same distance from the root.
//
//
//
//Example 1:
//
//
//Input: root = [5,8,9,2,1,3,7,4,6], k = 2
//Output: 13
//Explanation: The level sums are the following:
//- Level 1: 5.
//- Level 2: 8 + 9 = 17.
//- Level 3: 2 + 1 + 3 + 7 = 13.
//- Level 4: 4 + 6 = 10.
//The 2nd largest level sum is 13.
//Example 2:
//
//
//Input: root = [1,2,null,3], k = 1
//Output: 3
//Explanation: The largest level sum is 3.
//
//
//Constraints:
//
//The number of nodes in the tree is n.
//2 <= n <= 105
//1 <= Node.val <= 106
//1 <= k <= n



class `2583 Kth Largest Sum in a Binary Tree` {
    class TreeNode(var `val`: Int) {
        var left: TreeNode? = null
        var right: TreeNode? = null
    }

    fun kthLargestLevelSum(root: TreeNode?, k: Int): Long {
        if (root == null) {
            return -1
        }
        val levels = mutableListOf<Long>()
        val q: ArrayDeque<TreeNode> = ArrayDeque()
        q.addLast(root)
        while (q.isNotEmpty()) {
            var levelSum = 0L
            val size = q.count()
            repeat (size) {
                val node = q.removeFirst()
                levelSum += node.`val`
                node.left?.let { q.addLast(it) }
                node.right?.let { q.addLast(it) }
            }
            levels.add(levelSum)
        }
        return getLargest(levels, k)
    }

    private fun getLargest(levels: MutableList<Long>, k: Int): Long {
        if (k > levels.count()) {
            return -1
        }
        levels.sort()
        return levels[levels.count() - k]
    }
}

fun main() {
    val instance = `2583 Kth Largest Sum in a Binary Tree`()
    val root = `2583 Kth Largest Sum in a Binary Tree`.TreeNode(5)
    root.left = `2583 Kth Largest Sum in a Binary Tree`.TreeNode(8)
    root.right = `2583 Kth Largest Sum in a Binary Tree`.TreeNode(9)
    root.left!!.left = `2583 Kth Largest Sum in a Binary Tree`.TreeNode(2)
    root.left!!.right = `2583 Kth Largest Sum in a Binary Tree`.TreeNode(1)
    root.right!!.left = `2583 Kth Largest Sum in a Binary Tree`.TreeNode(3)
    root.right!!.right = `2583 Kth Largest Sum in a Binary Tree`.TreeNode(7)
    root.left!!.left!!.left = `2583 Kth Largest Sum in a Binary Tree`.TreeNode(4)
    root.left!!.left!!.right = `2583 Kth Largest Sum in a Binary Tree`.TreeNode(6)
    assertTrue(13L == instance.kthLargestLevelSum(root, 2))
}
