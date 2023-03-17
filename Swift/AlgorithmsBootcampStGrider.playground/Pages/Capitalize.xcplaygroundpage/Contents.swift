import Foundation

func capitalize(_ str: String) -> String {
    var strArray = str.components(separatedBy: " ")
    // do not use: str.split(separator: " ") it ignores ranges of empty spaces
    for i in 0...strArray.count - 1 {
        strArray[i] = strArray[i].capitalized
    }
    return strArray.joined(separator: " ")
}

assert(capitalize("näa  ba.. !") == "Näa  Ba.. !")
assert(capitalize("abbba") == "Abbba")
