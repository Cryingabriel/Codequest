cases = int(input())

for i in range (cases):
    line = int(input())

    if line < 70:
        print("FAIL")
    elif line >= 70 and line <= 100:
        print("PASS")