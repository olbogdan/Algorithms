

import Foundation

let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

func searchPosition(of x: Int) -> Int? {

    var min = 0
    var max = array.count - 1

    while min <= max {

        let midIndex = min + (max - min)/2
        if x < array[midIndex] {
            max = midIndex-1
        } else if x > array[midIndex] {
            min = midIndex+1
        } else if array[midIndex] == x {
            return midIndex
        }
    }
    return nil
}

let res = searchPosition(of:22)
print(res)


