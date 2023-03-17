import Foundation



func sum(arr: [Int]) -> Int {
    var total = 0
    for i in arr {
        total += i
    }
    return total
}

func sumRecursive(arr: [Int]) -> Int {
    if arr.count == 0 {
        return 0
    }
    if arr.count == 1 {
        return arr[0]
    }
    var mutatingArray = arr
    let last1 = mutatingArray.removeLast()
    let last2 = mutatingArray.removeLast()
    mutatingArray.append(last1+last2)
    return sumRecursive(arr: mutatingArray)
}

func maximum(arr: [Int]) -> Int {
    var maximum = Int.min
    for i in arr {
        if maximum < i {
            maximum = i
        }
    }
    return maximum
}

let array = [0, 1, 2, 4, 5, -1, -2]
print(sumRecursive(arr: array))
print(maximum(arr: array))
