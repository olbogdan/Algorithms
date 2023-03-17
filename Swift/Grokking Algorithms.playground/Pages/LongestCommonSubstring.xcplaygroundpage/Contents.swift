import Foundation

func minDistance(_ word1: String, _ word2: String) -> (Int, String) {
    
    var table = Array(
        repeating: Array(repeating: 0, count: word2.count+1),
        count: word1.count+1)
    
    let word1Array = Array(word1)
    let word2Array = Array(word2)
    var maxDistance = 0
    var substringEndIndex = 0
    for i in 0...word1Array.count {
        for j in 0...word2Array.count {
            if i == 0 || j == 0 {
                continue
            } else if word1Array[i-1] == word2Array[j-1]{
                table[i][j] = table[i-1][j-1] + 1
                if maxDistance < table[i][j] {
                    substringEndIndex = i
                }
                maxDistance = max(maxDistance, table[i][j])
            } else {
                table[i][j] = 0
            }
        }
    }
    
    let p = word1Array[substringEndIndex-maxDistance ..< substringEndIndex]
    return (maxDistance, String(p))
}

let (distance, substring) = minDistance("abcxyz", "abcdefg")
print(distance)
print(substring)

