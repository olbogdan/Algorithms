# Write a function that accepts a positive namber N.
# The function should console log a step shape with N levels
# using the # character. The step has spaces on the right hand side!
# example
# steps(3)
# "#   "
# "## "
# "###"

def steps(n):
    step = " " * 10
    for i in range(n):
        step = step[:i] + "#" + step[i+1:]
        print(step)


steps(3)
