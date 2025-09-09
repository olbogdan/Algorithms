# On day 1, one person discovers a secret.
#
# You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.
#
# Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: n = 6, delay = 2, forget = 4
# Output: 5
# Explanation:
# Day 1: Suppose the first person is named A. (1 person)
# Day 2: A is the only person who knows the secret. (1 person)
# Day 3: A shares the secret with a new person, B. (2 people)
# Day 4: A shares the secret with a new person, C. (3 people)
# Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
# Day 6: B shares the secret with E, and C shares the secret with F. (5 people)
# Example 2:
#
# Input: n = 4, delay = 1, forget = 3
# Output: 6
# Explanation:
# Day 1: The first person is named A. (1 person)
# Day 2: A shares the secret with B. (2 people)
# Day 3: A and B share the secret with 2 new people, C and D. (4 people)
# Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)
#
#
# Constraints:
#
# 2 <= n <= 1000
# 1 <= delay < forget <= n


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0

        for day in range(2, n + 1):
            if day - delay >= 1:
                share = (share + dp[day - delay]) % mod

            if day - forget >= 1:
                share = (share - dp[day - forget]) % mod
            dp[day] = share

        # all who still remember
        ans = 0
        for day in range(n - forget + 1, n + 1):
            if day >= 1:
                ans = (ans + dp[day]) % mod

        return ans


sol = Solution()
assert sol.peopleAwareOfSecret(6, 2, 4) == 5
assert sol.peopleAwareOfSecret(4, 1, 3) == 6
