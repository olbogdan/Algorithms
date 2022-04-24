# Pyramide has spaces on both the left and right hand sides
# Examples
# pyramid(4)
# "   #   "
# "  ###  "
# " ##### "
# "#######"

def pyramid(levels):
    levelSize = levels*2-1
    for i in range(1, levels+1):
        mid = "#" * (i*2-1)
        side = (levelSize - len(mid)) // 2
        left = " " * side
        right = " " * side
        print(left + mid + right)


pyramid(3)