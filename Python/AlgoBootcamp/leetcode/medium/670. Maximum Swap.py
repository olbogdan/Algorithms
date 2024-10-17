# You are given an integer num. You can swap two digits at most once to get the maximum valued number.
#
# Return the maximum valued number you can get.
#
#
#
# Example 1:
#
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
#
# Input: num = 9973
# Output: 9973
# Explanation: No swap.
#
#
# Constraints:
#
# 0 <= num <= 108


class Solution:
    def maximumSwap(self, num: int) -> int:
        numArr = []
        while num:
            mod = num % 10
            num = num // 10
            numArr.append(mod)
        # starts from less signif digit
        prefixes = []
        for idx, n in enumerate(numArr):
            if not prefixes:
                prefixes.append((idx, n))
            else:
                prevIdx, prevN = prefixes[-1]
                if n > prevN:
                    prefixes.append((idx, n))
                else:
                    prefixes.append(prefixes[-1])
        for idx in range(len(numArr) - 1, 0, -1):
            prefIdx, prefN = prefixes[idx - 1]
            if numArr[idx] < prefN:
                numArr[idx], numArr[prefIdx] = numArr[prefIdx], numArr[idx]
                break
        res = 0
        multy = 1
        for n in numArr:
            res += n * multy
            multy *= 10

        return res


sol = Solution()
assert sol.maximumSwap(19) == 91
assert sol.maximumSwap(2736) == 7236
