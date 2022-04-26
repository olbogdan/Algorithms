# --- Directions
# Write a function that returns the number of vowels
# used in a string. Vowels are the characters a, e, i, o and u
import re


def vowels(str):
    vowelsSet = {"a", "e", "i", "o", "u"}
    filteredStr = "".join(filter(lambda c: c.lower() in vowelsSet, str))
    return len(filteredStr)


assert(vowels("aeiou") == 5)
assert(vowels("Hallo") == 2)
assert(vowels("HALLO WALLI AND EVA") == 7)


def vowels_regex(str):
    filtered_str = re.findall('[aeiou]', str.lower())
    return len(filtered_str)


assert(vowels_regex("aeiou") == 5)
assert(vowels_regex("Hallo") == 2)
assert(vowels_regex("HALLO WALLI AND EVA") == 7)