def ispalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

assert ispalindrome("A man, a plan, a canal: Panama") == True
assert ispalindrome("") == True
assert ispalindrome("A") == True
assert ispalindrome("Aa") == True
assert ispalindrome("aAA") == True
assert ispalindrome("aBa") == True
assert ispalindrome("A    Bb __,./\[§`~}{ a") == True
assert ispalindrome("Ab") == False
assert ispalindrome("Abb") == False