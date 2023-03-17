import UIKit

//without using str.reversed() function, without direct comparing strings
func palindrome(_ str: String) -> Bool {
    let count = str.count
    if count < 2 {
        return true
    }
    
    for i in 0 ..< count/2 {
        let left = str.index(str.startIndex, offsetBy: i)
        let right = str.index(str.endIndex, offsetBy: -1 - i)
        print(str[left])
        print(str[right])
        if str[left] != str[right] {
            return false
        }
    }
    return true
}

print(palindrome("tam4mat"))
