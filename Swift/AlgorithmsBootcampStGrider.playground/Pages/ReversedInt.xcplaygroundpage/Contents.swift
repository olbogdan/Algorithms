import Foundation

/// -90 === -9
///  15 === 51
///  500 === 5
func reverse(_ i: Int) -> Int {
    let prefix = i < 0 ? "-":""
    let s: String = prefix + String(abs(i)).reversed()
    let int = Int(s)!
    return int
}

print(reverse(-2300))
