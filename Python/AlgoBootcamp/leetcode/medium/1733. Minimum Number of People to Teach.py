# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.
#
# You are given an integer n, an array languages, and an array friendships where:
#
# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.
#
# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
#
#
# Example 1:
#
# Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# Output: 1
# Explanation: You can either teach user 1 the second language or user 2 the first language.
# Example 2:
#
# Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
# Output: 2
# Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        langs = [set(l) for l in languages]
        needTeach = set()
        for u, v in friendships:
            u -= 1  # 0 based index
            v -= 1
            foundCommon = False
            for lang1 in langs[u]:
                if lang1 in langs[v]:
                    foundCommon = True
                    break
            if not foundCommon:
                needTeach.add(u)
                needTeach.add(v)

        if not needTeach:
            return 0

        # number of ppl associated to language
        count = [0] * (n + 1)
        for person in needTeach:
            for lang in langs[person]:
                count[lang] += 1

        # the language that covers the most people
        maxCovered = max(count)

        return len(needTeach) - maxCovered


sol = Solution()
assert sol.minimumTeachings(2, [[1], [2], [1, 2]], [[1, 2], [1, 3], [2, 3]]) == 1
assert sol.minimumTeachings(3, [[2], [1, 3], [1, 2], [3]], [[1, 4], [1, 2], [3, 4], [2, 3]]) == 2
