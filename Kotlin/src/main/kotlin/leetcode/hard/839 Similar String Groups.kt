package leetcode.hard
/*Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?



Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1


Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.*/
class `839 Similar String Groups` {
    fun numSimilarGroups(strs: Array<String>): Int {
        val n = strs.size
        val visited = BooleanArray(n)
        var count = 0
        
        fun isSimilar(s1: String, s2: String): Boolean {
            var diff = 0
            for (i in s1.indices) {
                if (s1[i] != s2[i]) {
                    diff++
                    if (diff > 2) {
                        return false
                    }
                }
            }
            return true
        }

        fun dfs(i: Int) {
            visited[i] = true
            for (j in strs.indices) {
                if (!visited[j] && isSimilar(strs[i], strs[j])) {
                    dfs(j)
                }
            }
        }

        for (i in strs.indices) {
            if (!visited[i]) {
                dfs(i)
                count++
            }
        }

        return count
    }
}

fun main() {
    val solution = `839 Similar String Groups`()

    // Test case 1
    val strs1 = arrayOf("tars", "rats", "arts", "star")
    val expected1 = 2
    val result1 = solution.numSimilarGroups(strs1)
    assert(expected1 == result1) { "Test case 1 failed" }

    // Test case 2
    val strs2 = arrayOf("omv", "ovm")
    val expected2 = 1
    val result2 = solution.numSimilarGroups(strs2)
    assert(expected2 == result2) { "Test case 2 failed" }

    println("All test cases passed")
}
