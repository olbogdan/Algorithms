package leetcode.medium
/*Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.



Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").


Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.*/
class `2405 Optimal Partition of String` {
    fun partitionString(s: String): Int {
        val seen = mutableSetOf<Char>()
        var res = 1
        for (ch in s) {
            if (ch in seen) {
                res += 1
                seen.clear()
            }
            seen.add(ch)
        }
        return res
    }
}


fun main() {
    val solution = `2405 Optimal Partition of String`()
    val s1 = "abcbca"
    val s2 = "xyzzyx"
    val s3 = "abcdefg"
    val s4 = "ababcbacadefegdehijhklij"

    println("Input: $s1, Output: ${solution.partitionString(s1)}") // Expected output: 3
    println("Input: $s2, Output: ${solution.partitionString(s2)}") // Expected output: 1
    println("Input: $s3, Output: ${solution.partitionString(s3)}") // Expected output: 7
    println("Input: $s4, Output: ${solution.partitionString(s4)}") // Expected output: 8
}