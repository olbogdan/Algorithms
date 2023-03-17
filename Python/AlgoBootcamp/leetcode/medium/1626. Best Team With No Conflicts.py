# You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.
#
# However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.
#
# Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.
# Example 1:
#
# Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# Output: 34
# Explanation: You can choose all the players.
# Example 2:
#
# Input: scores = [4,5,6,5], ages = [2,1,2,1]
# Output: 16
# Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
# Example 3:
#
# Input: scores = [1,2,3,5], ages = [8,9,10,1]
# Output: 6
# Explanation: It is best to choose the first 3 players.
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scag = []  # age, score
        dp = []  # index, score
        for i in range(len(scores)):
            scag.append((scores[i], ages[i]))
            dp.append(0)
        scag.sort()
        dp[0] = scag[0][0]

        for i in range(1, len(scag)):
            newS, newA = scag[i]
            dp[i] = newS
            for j in range(0, i):
                if newA >= scag[j][1]:
                    dp[i] = max(dp[i], dp[j] + newS)

        return max(dp)



sol = Solution()
res = sol.bestTeamScore([596,277,897,622,500,299,34,536,797,32,264,948,645,537,83,589,770], [18,52,60,79,72,28,81,33,96,15,18,5,17,96,57,72,72])
assert res == 3287
res = sol.bestTeamScore([1,2,3,5], [8,9,10,1])
assert res == 6
