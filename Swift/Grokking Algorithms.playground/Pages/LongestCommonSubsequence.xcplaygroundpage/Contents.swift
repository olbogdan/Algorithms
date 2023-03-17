import Foundation

func backtrack(_ matrix: [[Int]], _ word1: String, _ word2: String) -> String {
    var lcs = ""
    
    var i = word1.count
    var j = word2.count
    
    while i>0 && j>0 {
        let currentItem = matrix[i][j]
        if currentItem == matrix[i][j-1] {
            j -= 1
        } else if currentItem == matrix[i-1][j] {
            i -= 1
        } else {
            i -= 1
            j -= 1
            lcs.append(word1[word1.index(word1.startIndex, offsetBy: i)])
        }
        
    }
    return String(lcs.reversed())
}


func minDistance(_ word1: String, _ word2: String) -> Int {

    var matrix = Array(repeating: Array(repeating: 0, count: word2.count+1), count: word1.count+1)
    for (i, w1Char) in word1.enumerated() {
        for (j, w2Char) in word2.enumerated() {
            if (w1Char == w2Char) {
                matrix[i+1][j+1] = matrix[i][j] + 1
            } else {
                matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])
            }
        }
    }
    
    let res = backtrack(matrix, word1, word2)
    print(res)
    return matrix[word1.count][word2.count]
}


let i = minDistance("abcdefggx", "xbxdxxxxxfgx")
print(i)
