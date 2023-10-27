cases = int(input())

for i in range (cases):
    line = int(input())
    if line == 5:
        s = "#####"
        for i in range(line):
            print(" ".join(s))
    elif line == 3:
        s = "###"
        for i in range(line):
            print(" ".join(s))