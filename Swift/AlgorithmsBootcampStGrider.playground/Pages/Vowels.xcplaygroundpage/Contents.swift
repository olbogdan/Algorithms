// --- Directions
// Write a function that returns the number of vowels
// used in a string. Vowels are the characters a, e, i, o and u

import Foundation

/// swift
func vowels(_ str: String) -> Int {
    let vowels: Set<String> = ["a", "e", "i", "o", "u"]
    let filteredStr = str.filter { it in
        vowels.contains(it.lowercased())
    }
    return filteredStr.count
}

assert(vowels("aeiou") == 5)
assert(vowels("Hallo") == 2)
assert(vowels("HALLO WALLI AND EVA") == 7)

/// swift
func vowelsRegex(_ str: String) -> Int {
    let range = NSRange(location: 0, length: str.count)
    let regex = try! NSRegularExpression(pattern: "[aeiou]",
                                         options: .caseInsensitive)
    return regex.matches(in: str, range: range).count
}

assert(vowelsRegex("aeiou") == 5)
assert(vowelsRegex("Hallo") == 2)
assert(vowelsRegex("HALLO WALLI AND EVA") == 7)

///// kotlin:
//fun vowelsRegex(str: String): Int {
//    return Regex("[aeiou]").findAll(str.lowercase()).count()
//}
//
///// python:
//def vowels_regex(str):
//    filtered_str = re.findall('[aeiou]', str.lower())
//    return len(filtered_str)
