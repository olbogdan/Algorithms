package leetcode.easy
/*Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.*/
import java.util.*


class `383 Ransom Note` {

    fun canConstruct(ransomNote: String, magazine: String): Boolean {
        val count = magazine.groupingBy { it }.eachCount().toMutableMap()
        for (c in ransomNote) {
            if (c !in count || count[c] == 0) {
                return false
            } else {
                count[c] = count[c]!! - 1
            }
        }
        return true
    }
}
