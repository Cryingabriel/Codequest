import sys
cases = (int(sys.stdin.readline().rstrip()))

for i in range(cases):
    line = sys.stdin.readline().rstrip()
    line = line.split(" ")

    l = line.index("Nimo") + 1 or line.index("nimo") + 1
    print(l)