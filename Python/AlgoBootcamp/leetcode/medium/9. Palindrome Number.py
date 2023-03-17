# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.
# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Constraints:
#
# -231 <= x <= 231 - 1
#
#
# Follow up: Could you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x >= (div * 10):
            div *= 10

        while x != 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            # remove left digit
            x = x % div
            # remove right digit
            x = x // 10
            div = div/100
        return True


sol = Solution()
assert sol.isPalindrome(101) == True
assert sol.isPalindrome(111) == True
assert sol.isPalindrome(1111) == True
assert sol.isPalindrome(11011) == True
assert sol.isPalindrome(2) == True
assert sol.isPalindrome(120021) == True
assert sol.isPalindrome(12002) == False
assert sol.isPalindrome(12) == False
