package leetcode.medium
/*Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.*/

class `438 Find All Anagrams in a String` {
    fun findAnagrams(s: String, p: String): List<Int> {
        if (p.length > s.length) {
            return emptyList()
        }

        val pcount = p.groupingBy { it }.eachCount()
        val scount = mutableMapOf<Char, Int>()
        val res = mutableListOf<Int>()

        for (i in s.indices) {
            val char = s[i]
            scount[char] = scount.getOrDefault(char, 0) + 1

            if (i >= p.length - 1) {
                val startIdx = i - p.length + 1
                if (pcount == scount) {
                    res.add(startIdx)
                }

                val oldChar = s[startIdx]
                scount[oldChar] = scount.getOrDefault(oldChar, 0) - 1
                if (scount[oldChar] == 0) {
                    scount.remove(oldChar)
                }
            }
        }

        return res
    }
}
