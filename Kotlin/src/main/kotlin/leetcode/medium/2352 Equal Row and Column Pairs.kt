package leetcode.medium
/*Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).



Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]


Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105*/
class `2352 Equal Row and Column Pairs` {

    fun equalPairs(grid: Array<IntArray>): Int {
        val rowCounter = mutableMapOf<String, Int>() // {key: rowHash, val int: reps}

        val n = grid.size
        for (r in 0 until n) {
            val rowKey = StringBuilder("*")
            for (c in 0 until n) {
                rowKey.append(grid[r][c])
                rowKey.append("*")
            }
            val key = rowKey.toString()
            rowCounter[key] = rowCounter.getOrDefault(key, 0) + 1
        }

        var result = 0
        for (c in 0 until n) {
            val colKey = StringBuilder("*")
            for (r in 0 until n) {
                colKey.append(grid[r][c])
                colKey.append("*")
            }
            val key = colKey.toString()
            result += rowCounter.getOrDefault(key, 0)
        }

        return result
    }
}