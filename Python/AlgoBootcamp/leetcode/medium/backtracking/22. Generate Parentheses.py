# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
# Constraints:
# 1 <= n <= 8
from collections import deque
from typing import List


def generateParenthesis(n: int) -> List[str]:
    openedPool = closedPool = n
    result = []
    currentStack = deque()

    def dfs():
        nonlocal openedPool
        nonlocal closedPool
        if len(currentStack) == n * 2:
            result.append("".join(currentStack))
            return
        if openedPool > 0:
            openedPool -= 1
            currentStack.append("(")
            dfs()
            openedPool += 1
            currentStack.pop()
        if openedPool < closedPool:
            closedPool -= 1
            currentStack.append(")")
            dfs()
            closedPool += 1
            currentStack.pop()

    dfs()
    return result


assert generateParenthesis(1) == ['()']
assert generateParenthesis(2) == ['(())', '()()']
assert generateParenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
