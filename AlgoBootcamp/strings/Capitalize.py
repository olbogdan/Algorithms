def capitalize(str):
    split = str.split(" ")
    for i in range(len(split)):
        print(split[i].capitalize())
        split[i] = split[i].capitalize()
    return " ".join(split)


assert(capitalize("aa   a") == "Aa   A")
assert(capitalize("aaaa") == "Aaaa")
assert(capitalize("  a a a a") == "  A A A A")