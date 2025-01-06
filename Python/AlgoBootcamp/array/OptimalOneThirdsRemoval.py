import heapq

# return maxSumm after removing 1/3 items from the array by keeping order of remaining elements
# maxSumm is a sum(left remaining) - sum(left remaining)

class Solution:
    def getOptimalOneThirdsRemoval(self, weights: [int]) -> int:
        N = len(weights)
        THIRD = N//3
        leftPQ = self.getLeftHeap(0, THIRD, weights) # contains 33% of left side
        rightPQ = self.getRightHeap(THIRD, N, weights) # originally contains 66% of right side

        optimalRightItems = set()
        rightSum = 0
        for _ in range(THIRD):
            # take 1/3 of smallest elements and add them to the optimalRightItems
            number, idx = heapq.heappop(rightPQ)
            rightSum += number
            optimalRightItems.add(idx)

        leftSum = sum(leftPQ)
        result = leftSum - rightSum

        usedIdx = set()  # idx that can not be used for right anymore
        for idx in range(THIRD, THIRD*2):
            leftSum += weights[idx]
            heapq.heappush(leftPQ, weights[idx])
            # now leftPQ contains 1/3 + 1 element, remove the smallest extra element
            leftSum -= heapq.heappop(leftPQ)

            # remove value from right if it is used in right array
            if idx in optimalRightItems:
                optimalRightItems.remove(idx)
                rightSum -= weights[idx]
                # find new optimal right item after removal
                while rightPQ[0][1] in usedIdx:
                    heapq.heappop(rightPQ)
                rightVal, rightIdx = heapq.heappop(rightPQ)
                rightSum += rightVal
                optimalRightItems.add(rightIdx)

            usedIdx.add(idx)
            result = max(result, leftSum - rightSum)
        return result

    # returns min heap containing a pair of (value, index)
    def getRightHeap(self, start, end, weights):
        pq = [(weights[idx], idx) for idx in range(start, end)]
        heapq.heapify(pq)
        return pq

    # returns min heap containing values
    def getLeftHeap(self, start, end, weights):
        pq = [weights[idx] for idx in range(start, end)]
        heapq.heapify(pq)
        return pq


item_weights = [3, 2, 1] # 3 - 1 = 2
assert Solution().getOptimalOneThirdsRemoval(item_weights) == 2

item_weights = [1, 3, 4, 7, 5, 2] # (4+7) - (5+2) = 4
assert Solution().getOptimalOneThirdsRemoval(item_weights) == 4

item_weights = [-3, -2, -1] # -3 - (-2) = -1
assert Solution().getOptimalOneThirdsRemoval(item_weights) == -1

item_weights = [0, 0, -1000, 100, 0, 0] # 0 + 0 - (-1000+0) = 1000
assert Solution().getOptimalOneThirdsRemoval(item_weights) == 1000
print("tests passed ✅")
