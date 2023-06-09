package leetcode.easy
/*You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.



Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].


Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.*/


class `744 Find Smallest Letter Greater Than Target` {
    fun nextGreatestLetter(letters: CharArray, target: Char): Char {
        if (target < letters[0] || target >= letters.last()) {
            return letters[0]
        }
        var left = 0
        var right = letters.size - 1

        var result = letters[0]
        while (left <= right) {
            val mid = left + (right - left) / 2
            if (letters[mid] <= target) {
                left = mid + 1
            } else {
                result = letters[mid]
                right = mid - 1
            }
        }
        return result
    }
}

