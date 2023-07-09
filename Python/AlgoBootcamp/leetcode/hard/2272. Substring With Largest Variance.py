# The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.
#
# Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.
#
# A substring is a contiguous sequence of characters within a string.
#
#
#
# Example 1:
#
# Input: s = "aababbb"
# Output: 3
# Explanation:
# All possible variances along with their respective substrings are listed below:
# - Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
# - Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
# - Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
# - Variance 3 for substring "babbb".
# Since the largest possible variance is 3, we return it.
# Example 2:
#
# Input: s = "abcde"
# Output: 0
# Explanation:
# No letter occurs more than once in s, so the variance of every substring is 0.
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of lowercase English letters.


class Solution:
    def largestVariance(self, s: str) -> int:
        freq1 = 0
        freq2 = 0
        variance = 0

        # create distinct list of character pairs
        pairs = [(l1, l2) for l1 in set(s) for l2 in set(s) if l1 != l2]

        # run once for original string order, then again for reverse string order
        for runs in range(2):
            for pair in pairs:

                for letter in s:
                    # no reason to process letters that aren't part of the current pair
                    if letter not in pair:
                        continue

                    if letter == pair[0]:
                        freq1 += 1
                    elif letter == pair[1]:
                        freq2 += 1

                    if freq1 < freq2:
                        freq1 = freq2 = 0
                    elif freq1 > 0 and freq2 > 0:
                        variance = max(variance, freq1 - freq2)

                freq1 = freq2 = 0

            # reverse the string for the second time around
            s = s[::-1]

        return variance


sol = Solution()
assert sol.largestVariance("aababbb") == 3
