// Pyramide has spaces on both the left and right hand sides
// Examples
// pyramid(4)
// "   #   "
// "  ###  "
// " ##### "
// "#######"

import Foundation

func pyramid(_ levels: Int) {
    //levels*2 -1
    var arrayLevel = Array.init(repeating: " ", count: levels * 2 - 1)
    for step in 0..<levels {
        let middle = arrayLevel.count / 2
        arrayLevel[middle-step] = "#"
        arrayLevel[middle+step] = "#"
        print(arrayLevel.joined(separator: ""))
    }
}
pyramid(8)
