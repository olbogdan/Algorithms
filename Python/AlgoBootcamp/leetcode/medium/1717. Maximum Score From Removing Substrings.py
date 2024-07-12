# You are given a string s and two integers x and y. You can perform two types of operations any number of times.
#
# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.
#
#
#
# Example 1:
#
# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# Example 2:
#
# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
#
#
# Constraints:
#
# 1 <= s.length <= 105
# 1 <= x, y <= 104
# s consists of lowercase English letters.


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        abArray = ['a', 'b']
        AB = "ab"
        BA = "ba"
        res = 0

        def helper(input, target, score):
            nonlocal res
            stack = []
            for char in input:
                # optimize memory to not add useless chars
                if stack and stack[-1] not in abArray and char not in abArray:
                    continue
                stack.append(char)
                if len(stack) > 1 and stack[-2] + stack[-1] == target:
                    res += score
                    stack.pop()
                    stack.pop()
            return stack

        if x > y:
            output = helper(s, AB, x)
            helper(output, BA, y)
        else:
            output = helper(s, BA, y)
            helper(output, AB, x)
        return res


sol = Solution()
assert sol.maximumGain("cdbcbbaaabab", 4, 5) == 19
assert sol.maximumGain("aabbaaxybbaabb", 5, 4) == 20
