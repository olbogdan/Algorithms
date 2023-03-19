package leetcode.easy

class WordPattern {
    fun wordPattern(pattern: String, s: String): Boolean {
        val splitS = s.split(" ")
        if (splitS.size != pattern.length) return false
        val cToW = mutableMapOf<Char, String>()
        val wToC = mutableMapOf<String, Char>()
        for ((char, word) in pattern.toList().zip(splitS)) {
            if (cToW.getOrDefault(char, word) != word ||
                wToC.getOrDefault(word, char) != char)
                return false
            cToW[char] = word
            wToC[word] = char
        }
        return true
    }
}

fun main() {
    val sol = WordPattern()
    require(!sol.wordPattern("abba", "dog cat cat fish"))
    require(sol.wordPattern("abba", "dog cat cat dog"))
}




