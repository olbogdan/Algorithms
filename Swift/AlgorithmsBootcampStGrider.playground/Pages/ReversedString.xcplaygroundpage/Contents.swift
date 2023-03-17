import Foundation

/// reverse string without using str.reversed() function
func reverse(_ str: String) -> String {
    var reversedArray = Array<Character>()
    reversedArray.reserveCapacity(str.count)
    for i in str {
        reversedArray.insert(i, at: 0)
    }
    return String(reversedArray)
}

print(reverse("hello"))

/// reverse string with reduce()
func reverseReduce(_ str: String) -> String {
    return str.reduce("") { partialResult, char in
        String(char) + partialResult
    }
}

print(reverseReduce("hello"))
