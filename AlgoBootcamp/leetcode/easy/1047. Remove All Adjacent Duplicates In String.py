# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
#
# We repeatedly make duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
from collections import deque


def removeDuplicates(s: str) -> str:
    dq = deque()
    dq.append(s[0])
    for i in range(1, len(s)):
        if len(dq) > 0 and dq[-1] == s[i]:
            dq.pop()
        else:
            dq.append(s[i])

    return "".join(dq)

assert removeDuplicates("abbaca") == "ca"
