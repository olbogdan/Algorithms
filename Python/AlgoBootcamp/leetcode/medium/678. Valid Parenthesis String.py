# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
#
# The following rules define a valid string:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "(*)"
# Output: true
# Example 3:
#
# Input: s = "(*))"
# Output: true
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.


class Solution:
    def checkValidString(self, s: str) -> bool:
        opened = []
        asterisks = []
        for i in range(len(s)):
            char = s[i]

            if char == "(":
                opened.append(i)
            elif char == "*":
                asterisks.append(i)
            else:
                if opened:
                    opened.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
        while opened and asterisks:
            if opened[-1] < asterisks[-1]:
                opened.pop()
                asterisks.pop()
            else:
                return False
        return False if opened else True


sol = Solution()
assert sol.checkValidString("()") is True
assert sol.checkValidString("(*)") is True
assert sol.checkValidString("(*))") is True
assert sol.checkValidString("(*))(") is False
assert sol.checkValidString("(**") is True
assert sol.checkValidString("***(((") is False


class Solution:
    def checkValidString(self, s: str) -> bool:
        opn = 0
        # opn >= cls !
        for i in range(len(s)):
            if s[i] == ')':
                opn -= 1
                if opn < 0:
                    return False
            else:
                opn += 1
        cls = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                cls -= 1
                if cls < 0:
                    return False
            else:
                cls += 1
        return True


sol = Solution()
assert sol.checkValidString("(*))(") is False
assert sol.checkValidString("(**") is True
assert sol.checkValidString("***(((") is False
