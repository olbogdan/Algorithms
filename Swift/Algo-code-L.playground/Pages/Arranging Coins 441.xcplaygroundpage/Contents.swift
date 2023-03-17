import Foundation

func arrangeCoins(_ n: Int) -> Int {
    var l = 1
    var r = n
    var result = 0
    while l <= r {
        let mid = (r+l)/2
        let coins = (Double(mid)/2)*(Double(mid)+1)
        if coins > Double(n) {
            r = mid - 1
        } else {
            l = mid + 1
            result = max(mid, result)
        }
    }
    return result
}

print(arrangeCoins(5))
print(arrangeCoins(10))
assert(arrangeCoins(2146467959) == 65519)
