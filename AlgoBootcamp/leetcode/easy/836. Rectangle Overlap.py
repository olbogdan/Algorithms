# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.
#
# Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.
#
# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.


def isRectangleOverlap(rec1: [int], rec2: [int]) -> bool:
    def isOverlap(a1, a2, b1, b2):
        maxdim = max(a1, b1)
        mindim = min(a2, b2)
        if maxdim >= mindim:
            return False
        return True

    if isOverlap(rec1[0], rec1[2], rec2[0], rec2[2]) and isOverlap(rec1[1], rec1[3], rec2[1], rec2[3]):
        return True
    return False

assert isRectangleOverlap([0,0,2,2], [1,1,3,3]) == True
assert isRectangleOverlap([0,0,2,2], [2,3,3,3]) == False