import Foundation

func maxRepeatedChar(_ str: String) -> Character? {
    var dictionary: [Character: Int] = [:]
    for s in str {
        let repeats = dictionary[s] ?? 0
        dictionary[s] = repeats+1
    }
    let maxElement = dictionary.max { element1, element2 in
        element1.value < element2.value
    }
    return maxElement?.key
}

var greeting = "Hello, playground..."
print(maxRepeatedChar(greeting))
