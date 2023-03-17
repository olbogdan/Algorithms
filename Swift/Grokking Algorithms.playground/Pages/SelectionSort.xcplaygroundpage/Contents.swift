import UIKit

let source: Array<Int> = [22, 33, 44, 20, 1000, 4, 2, 445, 0, 99999, 11, 12300]

func sortArray() {
    var array = source
    var sortedArray: [Int] = []

    while !array.isEmpty {
        let smallest = smallest(arrayWithSmallest: array)
        sortedArray.append(smallest)
        array.remove(at: array.firstIndex(of: smallest)!)
    }
    print(sortedArray)
}

func smallest(arrayWithSmallest: Array<Int>) -> Int {
    var smallest: Int = arrayWithSmallest[0]
    for i in 1 ..< arrayWithSmallest.count {
        if smallest > arrayWithSmallest[i] {
            smallest = arrayWithSmallest[i]
        }
    }

    return smallest
}

sortArray()
