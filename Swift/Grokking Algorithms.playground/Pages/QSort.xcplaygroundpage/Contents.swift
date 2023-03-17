import Foundation

func qSort(_ arr: [Int]) -> [Int] {

    if arr.count < 2 {
        return arr
    }
    
    let pivot = arr[0]
    
    var leftArray = [Int]()
    for i in 1..<arr.count where arr[i] <= pivot {
        leftArray.append(arr[i])
    }
    
    var rightArray = [Int]()
    for i in 1..<arr.count where arr[i] > pivot {
        rightArray.append(arr[i])
    }
    return qSort(leftArray) + [arr[0]] + qSort(rightArray)
}

let array = [22, 0, 1, 100, 2, 4, 5, -1, -2]
print(qSort(array))
