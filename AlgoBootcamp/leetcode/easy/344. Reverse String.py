# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString(s: [str]):
    """
    Do not return anything, modify s in-place instead.
    """
    size = len(s)
    for i in range(0, size // 2):
        s[i], s[-i - 1] = s[-i - 1], s[i]
    return s


assert reverseString(["a", "b"]) == ["b", "a"]
assert reverseString(["a", "b", "c"]) == ["c", "b", "a"]