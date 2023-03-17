import Foundation

//anagrams ingored case, ignored non alpahanumeric chars
func anagrams(_ stringA: String, _ stringB: String) -> Bool {
    let strA = stringA.filter { c in
        c.isLetter
    }
    let strB = stringB.filter { c in
        c.isLetter
    }
//    let strA = stringA.replacingOccurrences(of: "[^\\w]", with: "", options: [.regularExpression]).lowercased()
//    let strB = stringB.replacingOccurrences(of: "[^\\w]", with: "", options: [.regularExpression]).lowercased()

    if strA.count != strB.count {
        return false
    }
    var mapA: [Character: Int] = [:]
    strA.forEach { char in
        let count = mapA[char]
        mapA[char] = count == nil ? 1 : count! + 1
    }
    var mapB: [Character: Int] = [:]
    strB.forEach { char in
        let count = mapB[char]
        mapB[char] = count == nil ? 1 : count! + 1
    }

    return mapA == mapB
}

print(anagrams("näa   ba.. !", "ba -aä ,  n"))
assert(anagrams("aba   ", "baa!") == true)
assert(anagrams("ab", "baa") == false)
assert(anagrams("baa", "ab") == false)

func anagrams2(_ stringA: String, _ stringB: String) -> Bool {

    let filteredA = stringA.lowercased().filter { c in
        c.isLetter
    }
    let filteredB = stringB.lowercased().filter { c in
        c.isLetter
    }
    let sortedA = filteredA.sorted()
    let sortedB = filteredB.sorted()
    return sortedA == sortedB
}

print(anagrams2("näa   ba.. !", "ba -aä ,  n"))
assert(anagrams2("aba   ", "baa!") == true)
assert(anagrams2("ab", "baa") == false)
assert(anagrams2("baa", "ab") == false)

//kotlin
//val re = Regex("[^A-Za-z0-9 ]")
//answer = re.replace(str, "")
//check if char:
//Char.isLetterOrDigit()
//get char from string:
//var b = "a"
//var c = b[0]

//swift
//str.replacingOccurrences(of: "[^A-Za-z0-9 ]", with: "", options: [.regularExpression])
//or
//str.components(separatedBy: CharacterSet.symbols).joined(separator: "")
//check if num:
//character.isWholeNumber

//java
//str.replaceAll("[^a-zA-Z0-9]", " ");
//check if char:
//Character.isLetterOrDigit(string.charAt(index))
//get char from string
//s.charAt(0)

//pattern includes all chars of all languages
//^[{\p{L}}{0-9}]$
