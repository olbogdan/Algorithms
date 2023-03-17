import org.junit.jupiter.api.Assertions

// --- Directions
// Write a function that returns the number of vowels
// used in a string. Vowels are the characters a, e, i, o and u

fun vowels(str: String): Int {
    val vowels = setOf("a", "e", "i", "o", "u")
    return str.count {
        vowels.contains(it.lowercase())
    }
}

fun vowelsRegex(str: String): Int {
    return "[aeiou]".toRegex(RegexOption.IGNORE_CASE).findAll(str).count()
}


fun main() {
    vowelsRegex("a abe")
    Assertions.assertTrue(vowels("aeiou") == 5)
    Assertions.assertTrue(vowels("Hallo") == 2)
    Assertions.assertTrue(vowels("HALLO WALLI AND EVA") == 7)

    Assertions.assertTrue(vowelsRegex("aeiou") == 5)
    Assertions.assertTrue(vowelsRegex("Hallo") == 2)
    Assertions.assertTrue(vowelsRegex("HALLO WALLI AND EVA") == 7)
}