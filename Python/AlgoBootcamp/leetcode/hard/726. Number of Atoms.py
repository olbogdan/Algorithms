# Given a string formula representing a chemical formula, return the count of each atom.
#
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
#
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.
#
# For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# Two formulas are concatenated together to produce another formula.
#
# For example, "H2O2He3Mg4" is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula.
#
# For example, "(H2O2)" and "(H2O2)3" are formulas.
# Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.
#
# The test cases are generated so that all the values in the output fit in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: formula = "H2O"
# Output: "H2O"
# Explanation: The count of elements are {'H': 2, 'O': 1}.
# Example 2:
#
# Input: formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# Example 3:
#
# Input: formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
#
#
# Constraints:
#
# 1 <= formula.length <= 1000
# formula consists of English letters, digits, '(', and ')'.
# formula is always valid.


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        stack.append({})
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append({})
                i += 1
            elif formula[i] == ')':
                i += 1
                lastMap = stack.pop()
                number = 0
                while i < len(formula) and formula[i].isdigit():
                    number *= 10
                    number += int(formula[i])
                    i += 1
                self.multiplyMapByNumber(lastMap, number)
                self.mergeMaps(lastMap, stack[-1])
            else:
                element = ""
                element += formula[i]
                i += 1
                if i < len(formula) and formula[i].isalpha() and formula[i].islower():
                    element += formula[i]
                    i += 1
                number = 0
                while i < len(formula) and formula[i].isdigit():
                    number *= 10
                    number += int(formula[i])
                    i += 1
                self.addElementToMap(element, number, stack[-1])
        return self.convertMapToResult(stack[0])

    def addElementToMap(self, element, number, toMap):
        if number == 0:
            number = 1
        if element in toMap:
            toMap[element] += number
        else:
            toMap[element] = number

    def multiplyMapByNumber(self, mapToMultiply, number):
        if number == 0:
            return
        for k in mapToMultiply.keys():
            mapToMultiply[k] *= number

    def convertMapToResult(self, fromMap) -> str:
        listed = []
        for k, v in fromMap.items():
            if v == 1:
                listed.append(k)
            else:
                listed.append(k + str(v))
        listed.sort()
        return "".join(listed)

    def mergeMaps(self, fromMap, toMap):
        for k, v in fromMap.items():
            if k in toMap:
                toMap[k] += fromMap[k]
            else:
                toMap[k] = fromMap[k]


sol = Solution()
print(sol.countOfAtoms("H2O"))
assert sol.countOfAtoms("H2O") == "H2O"
