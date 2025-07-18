# You are given a 0-indexed integer array nums consisting of 3 * n elements.
#
# You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:
#
# The first n elements belonging to the first part and their sum is sumfirst.
# The next n elements belonging to the second part and their sum is sumsecond.
# The difference in sums of the two parts is denoted as sumfirst - sumsecond.
#
# For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
# Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
# Return the minimum difference possible between the sums of the two parts after the removal of n elements.
#
#
#
# Example 1:
#
# Input: nums = [3,1,2]
# Output: -1
# Explanation: Here, nums has 3 elements, so n = 1.
# Thus we have to remove 1 element from nums and divide the array into two equal parts.
# - If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
# - If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
# - If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
# The minimum difference between sums of the two parts is min(-1,1,2) = -1.
# Example 2:
#
# Input: nums = [7,9,5,8,1,3]
# Output: 1
# Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
# If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
# To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
# It can be shown that it is not possible to obtain a difference smaller than 1.
#
#
# Constraints:
#
# nums.length == 3 * n
# 1 <= n <= 105
# 1 <= nums[i] <= 105
from heapq import heappop, heappush
from typing import List


# intuition:
# minimize the left size
# maximize the right size
# default PQ in python smallest to the biggest
# main iteration:
#    biggest of left PQ replace by something smaller. MIN(biggestLeft, nums[i])
#

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        QTR = N // 3
        leftSum = 0
        leftQ = []  # inverted, to return the biggest value (use for swap with smaller)
        for i in range(QTR):
            leftSum += nums[i]
            heappush(leftQ, -nums[i])

        rightQ = []  # inverted, to return bigges (to use as store if cur biggest removed)
        for i in range(QTR, N):
            heappush(rightQ, (-nums[i], i))

        rightSum = 0  # holds sum of biggest values
        usedForRightSumIdxs = set()  # (idx of used biggest values)
        for i in range(QTR):
            numInverted, idx = heappop(rightQ)
            rightSum += numInverted * -1
            usedForRightSumIdxs.add(idx)
        res = leftSum - rightSum
        for i in range(QTR, QTR * 2):
            candidate = nums[i]
            # new value can make left part smaller
            if candidate < leftQ[0] * -1:
                removedBigItem = heappop(leftQ) * -1
                leftSum -= removedBigItem
                leftSum += candidate  # add slitly smaller item
                heappush(leftQ, -candidate)  # add it to the leftQ
            # the candidate cannot be used in the right part anymore
            if i in usedForRightSumIdxs:
                rightSum -= nums[i]
                numInverted, idx = heappop(rightQ)
                while idx <= i:  # cannot be used, coz already on the left size
                    numInverted, idx = heappop(rightQ)
                rightSum += numInverted * -1
                usedForRightSumIdxs.add(idx)
            res = min(res, leftSum - rightSum)
        return res


sol = Solution()
assert sol.minimumDifference([3, 1, 2]) == -1
assert sol.minimumDifference([7, 9, 5, 8, 1, 3]) == 1
assert sol.minimumDifference([16,46,43,41,42,14,36,49,50,28,38,25,17,5,18,11,14,21,23,39,23]) == -14
assert sol.minimumDifference([81644,57022,50915,95859,56210,9357,40127,88010,76199,53687,46822,11437,1494,76980,92195,75013,7423,34588,41953,18541,38320,58258,33449,15959,81057,33006,9220,87220,96129,47400,29886,75172,43955,97686,63471,56944,5211,64765,39081,69226,4334,4176,73055,64741,58069,8756,43199,4214,71530,49411,14924,52085,54462,9111,26176,19113,83706,47857,45523,99181,25874,35294,78866,37476,67320,74986,55827,8058,78724,11987,23462,97558,61276,90452,50030,8797,79369,20997,63117,3020,77515,49740,63136,2908,37532,98426,83435,20135,72241,24895,44027,37476,17941,9664,70646,56210,25781,86270,58708,35928,62870,93873,93732,28510,3085,96542,38049,44850,37916,38483,89324,41176,64882,46336,96108,27373,50253,24736,52213,55869,2124,38290,42239,1752,74889,13296,14403,8233,82063,35093,99857,98281,46818,50644,32856,98609,34880,49108,90926,8615,10825,19152,99098,46548,27980,78208,56007,95238,56718,61282,36285,49802,71544,70268,52875,43363,19593,93340,32464,75981,32142,95057,90788,30476,16249,66720,5296,38619,70403,4615,96990,36408,92411,52395,65,13745,37965,88300,59397,54914,5,85017,30537,68214,85376,69123,69487,52057,67496,16573,69254,47762,22662,87241,54635,66413,51248,59804,60117,66615,23354,87255,31087,1891,22405,86353,509,38903,10981,10466,59284,89420,38023,67122,77050,48351,76132,59610,58130,81566,34462,14752,68583,17774,28510,95800,93876,61959,65523,3896,84284,59332,55492,312,81532,46099,88517,5386,45310,47418,50297,43340,71055,94134,89346,2621,47227,88140,98032,19439,71628,94520,13880,43098,98736,46490,89182,13791,20472,25370,62701,2408,5981,19743,67977,30654,59288,94964,10404,45122,66127,94876,27980,65354,8148,28316,55999,71630,50958,12503,8846,71939,35697,94353,4384,6615,63264,68443,3829,36120,72004,41820,74686,66761,98189,37324,44989,45786,81155,82049,61926,35660,97095,52182,18699,15367,41151,37877,55245,61890,25125,96766,66385,25463,75070,80964,16282,39281,31036,61155,35977,13297,42862,5577,1847,46575,8394,63014,1130,34004,28139,94701,99333,7520,69994,95685,19050,61365,32859,8840,12422,39763,52574,59647,73667,46174,5527,17796,34242,38632,63313,7186,11162,79448,22732,66322,31129,72939,44202,96430,15097,49019,92624,907,19806,63328,94234,34083,65270,6722,33279,93300,63647,50706,43555,8339,79626,61081,90413,94023,81837,52317,62387,76606,25726,53153,3229,15523,74483,47001,24688,39972,1293,11199,1254,13578,75550,78624,77709,77690,38213,9497,80549,79411,69871,40966,69351,82048,39199,25389,1009,54619,86903,33866,36540,8355,55566,20904,69265,9008,78363,69701,95478,96487,93507,35336,5439,16092,98675,57267,10112,36434,86447,59198,80877,80539,79502,36256,83889,85463,87749,36059,83944,67675,45071,7614,28857,9589,21677,69379,5988,52875,15315,4804,39027,9215,51594,92169,63682,68568,59012,91081,17034,10557,33906,38916,6426,71079,84319,73479,7706,30629,6903,77541,54919,29079,60418,23533,60853,91125,10803,61082,70740,19869,97042,39228,3498,11968,2491,35901,18835,20654,13751,96532,3581,75509,81002,47635,72741,19347,27782,46323,76504,26647,18447,35925,62283,15947,97501,91437,11395,87021,19406,89725,30568,13235,42789,30707,37089,73958,46737,78285,53000,81934,43387,49617,95862,4575,76772,96220,18430,8112,70813,17230,49802,88649,85824,93127,16368,92010,72200,44333,64231,65988,33541,12429,90916,57048,25295,69940,2779,63389,92701,2243,78916,8984,32219,11158,46982,91996,56409,41803,37276,41945,3597,80525,69491,15775,31685,60043,17222,15722,69735,80246,40783,21101,52815,50189,33637,61856,66976,65495,28584,74026,29674,68937,93659,46335,86079,88453,77823,4496,99995,41205,2352,89182,8785,59745,96936,90509,92549,82987,95449,67828,1290,78508,93918,10956,63733,53956,59548,69308,7295,91954,54448,52221,99740,68142,97164,3382,27682,7834,4713,31981,59829,65377,92835,86185,35182,60536,5385,1286,54115,21617,4869,28207,21507,41157,36231,54179,57201,91769]) == -7353520
