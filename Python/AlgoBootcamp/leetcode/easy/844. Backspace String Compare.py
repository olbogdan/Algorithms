# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
#
#
# Example 1:
#
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:
#
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:
#
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
#
#
# Follow up: Can you solve it in O(n) time and O(1) space?


class Solution1:
    def backspaceCompare(self, s: str, t: str) -> bool:
        BACK = '#'
        def getWord(w) -> str:
            stack = []
            for ch in w:
                if ch != BACK:
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return getWord(s) == getWord(t)


sol = Solution1()
res = sol.backspaceCompare("ab##", "c#d#")
assert res is True

res = sol.backspaceCompare("xywrrmp", "xywrrmu#p")
assert res is True

res = sol.backspaceCompare("nzp#o#g", "b#nzp#o#g")
assert res is True

res = sol.backspaceCompare("nzp#o#g", "b#n")
assert res is False


class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:
        BACK = '#'
        i1 = len(s) - 1
        i2 = len(t) - 1
        while i1 >= 0 or i2 >= 0:
            backs1 = 0
            while i1 >= 0 and s[i1] == BACK:
                backs1 += 1
                i1 -= 1
                while i1 >= 0 and s[i1] != BACK and backs1 > 0:
                    backs1 -= 1
                    i1 -= 1

            backs2 = 0
            while i2 >= 0 and t[i2] == BACK:
                backs2 += 1
                i2 -= 1
                while i2 >= 0 and t[i2] != BACK and backs2 > 0:
                    backs2 -= 1
                    i2 -= 1

            if i1 < 0 and i2 < 0:
                return True
            elif i1 < 0 or i2 < 0 or s[i1] != t[i2]:
                return False
            i1 -= 1
            i2 -= 1

        return i1 == i2


sol = Solution2()
res = sol.backspaceCompare("ab##", "c#d#")
assert res is True

res = sol.backspaceCompare("xywrrmp", "xywrrmu#p")
assert res is True

res = sol.backspaceCompare("nzp#o#g", "b#nzp#o#g")
assert res is True

res = sol.backspaceCompare("nzp#o#g", "b#n")
assert res is False
