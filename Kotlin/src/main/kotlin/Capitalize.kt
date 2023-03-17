import org.junit.jupiter.api.Assertions

fun capitalize(str: String): String {
    val listSubstring = str.split(" ").toMutableList()
    for (i in 0 until listSubstring.count()) {
        val capitalizedStr = listSubstring[i].replaceFirstChar {
            it.uppercase()
        }
        listSubstring[i] = capitalizedStr
    }
    return listSubstring.joinToString(" ")
}

fun main() {
    print(capitalize("ab   ba"))
    Assertions.assertTrue(capitalize("ab   ba") == "Ab   Ba")
    Assertions.assertFalse(capitalize("abbba") == "abbba")
    Assertions.assertTrue(capitalize(" bBa") == " BBa")
}