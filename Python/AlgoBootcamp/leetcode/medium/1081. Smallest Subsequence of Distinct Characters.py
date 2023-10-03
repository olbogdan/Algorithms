# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
#
#
# Example 1:
#
# Input: s = "bcabc"
# Output: "abc"

from collections import deque, Counter

def removeDuplicateLetters(s: str) -> str:
    counter = Counter(s)
    used = set()

    result = deque()
    for i in s:
        counter[i] = counter[i] - 1

        if i not in used:
            while result and result[-1] > i and counter[result[-1]] > 0:
                used.remove(result.pop())
            result.append(i)
            used.add(i)
    return "".join(result)

assert removeDuplicateLetters("bcabc") == "abc"
assert removeDuplicateLetters("bbcaac") == "bac"
assert removeDuplicateLetters("edebbed") == "bed"


class Solution2:
    def smallestSubsequence(self, s: str) -> str:

        count = Counter(s)
        result = []
        for char in s:
            count[char] -= 1
            if char not in result:
                while result and char < result[-1] and count[result[-1]] > 0:
                    result.pop()
                result.append(char)
        return "".join(result)
sol = Solution2()
res = sol.smallestSubsequence("cbaacabcaaccaacababa")
assert res == "abc"
