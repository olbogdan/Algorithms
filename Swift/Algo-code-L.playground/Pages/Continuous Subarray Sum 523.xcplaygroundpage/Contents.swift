import Foundation

func checkSubarraySum(_ array: [Int], _ k: Int) -> Bool {
    var remainder: Dictionary<Int, Int> = [0 : -1]
    var sum = 0
    for (index, value) in array.enumerated() {
        sum = value + sum
        let mod = sum % k
        if remainder[mod] == nil {
            remainder[mod] = index
        } else if index - remainder[mod]! > 1 {
            return true
        }
    }
    return false
}

let nums0 = [5, 12]
let nums1 = [5, 12, 0]
let nums2 = [5, 0, 0]
let nums3 = [5, 2, 2]
let nums4 = [5, 2, 2, 2]

assert(checkSubarraySum(nums0, 6) == false)
assert(checkSubarraySum(nums1, 6) == true)
assert(checkSubarraySum(nums2, 6) == true)
assert(checkSubarraySum(nums3, 6) == false)
assert(checkSubarraySum(nums4, 6) == true)



func checkSubarraySum2(_ nums: [Int], _ k: Int) -> Bool {
    var prev = 0
    var sum = 0
    var set: Set<Int> = []
    for num in nums {
        sum = sum + num
        let mod = sum % k
        if set.contains(mod) {
            return true
        }
        set.insert(prev)
        prev = mod
    }
    return false
}

print(checkSubarraySum(nums0, 6))
