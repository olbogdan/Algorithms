# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def isPalindrome(s: str) -> bool:
    slower = s.lower()
    l = 0
    r = len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if slower[l] == slower[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


# assert isPalindrome("A man, a plan, a canal: Panama") == True
print(isPalindrome("0P"))