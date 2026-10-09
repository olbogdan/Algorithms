# 1541. Minimum Insertions to Balance a Parentheses String
# Solved
# Medium
#
# Topics
# premium lock icon
# Companies
#
# Hint
# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
#
# Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
#
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.
#
# Return the minimum number of insertions needed to make s balanced.
#
#
#
# Example 1:
#
# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.
# Example 2:
#
# Input: s = "())"
# Output: 0
# Explanation: The string is already balanced.
# Example 3:
#
# Input: s = "))())("
# Output: 3
# Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of '(' and ')' only.


class Solution:
    def minInsertions(self, s: str) -> int:
        opening = []
        count = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                opening.append('(')
            elif s[i] == ')':
                if opening:
                    if i != len(s) - 1 and s[i + 1] == ')':  # has double closing
                        i += 1
                    else:  # single closing or last, we need extra closing (+1)
                        count += 1
                    opening.pop()
                else:
                    if i != len(s) - 1 and s[i + 1] == ')':
                        count += 1
                        i += 1  # Skip next ')'
                    else:
                        count += 2
            i += 1

        return count + len(opening) * 2  # Each unmatched '(' needs two ')'


assert Solution().minInsertions("(()))") == 1
assert Solution().minInsertions("))())(") == 3

