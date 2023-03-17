from collections import \
    deque  # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 #
 # An input string is valid if:
 #
 # Open brackets must be closed by the same type of brackets.
 # Open brackets must be closed in the correct order.
 # Every close bracket has a corresponding open bracket of the same type.
 #
 #
 # Example 1:
 #
 # Input: s = "()"
 # Output: true
 # Example 2:
 #
 # Input: s = "()[]{}"
 # Output: true
 # Example 3:
 #
 # Input: s = "(]"
 # Output: false


def isValid(s: str) -> bool:
    if len(s) == 1:
        return False
    stack = deque()
    opening = {"(", "[", "{"}
    closingMap = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in opening:
            stack.append(char)
        else:
            if not stack or stack.pop() != closingMap[char]:
                return False
    if stack:
        return False
    else:
        return True


assert isValid("(({})){}") is True
assert isValid("(") is False
assert isValid("([)]") is False