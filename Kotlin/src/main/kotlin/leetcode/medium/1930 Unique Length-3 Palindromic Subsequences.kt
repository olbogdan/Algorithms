package leetcode.medium

class `1930 Unique Length-3 Palindromic Subsequences` {
    fun countPalindromicSubsequence(s: String): Int {
        val left = mutableSetOf<Char>()

        val right = s.groupingBy { it }.eachCount().toMutableMap()

        val result = mutableSetOf<Pair<Char, Char>>()
        for (i in s.indices) {
            val currentChar: Char = s[i]
            right[currentChar] = right[currentChar]?.minus(1) ?: 0
            if (right[currentChar] == 0) {
                right.remove(currentChar)
            }
            for (ch in left) {
                if (ch in right) {
                    result.add(currentChar to ch)
                }
            }
            left.add(currentChar)
        }
        return result.size
    }
}

fun main() {
    val sol = `1930 Unique Length-3 Palindromic Subsequences`()
    var res = sol.countPalindromicSubsequence("abc")
    assert(res == 0)
    res = sol.countPalindromicSubsequence("abca")
    assert(res == 2)
}
