# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.
#
# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.
#
#
#
# Example 1:
#
# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Example 2:
#
# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#
#
# Constraints:
#
# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
# All the integer values in the input expression are in the range [0, 99].
# The integer values in the input expression do not have a leading '-' or '+' denoting the sign.
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = self.getOperations()

        def backtrack(l, r):
            res = []
            for i in range(l, r):
                if not expression[i].isdigit():
                    oper = operators[expression[i]]
                    leftArr = backtrack(l, i)
                    rightArr = backtrack(i + 1, r)
                    for n1 in leftArr:
                        for n2 in rightArr:
                            res.append(oper(n1, n2))
            if not res:
                res.append(int(expression[l:r]))
            return res

        return backtrack(0, len(expression))

    def getOperations(self):
        return {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }


sol = Solution()
assert sol.diffWaysToCompute("2-1-1") == [2, 0]
