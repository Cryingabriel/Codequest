import sys
cases = (int(sys.stdin.readline().rstrip()))

for i in range(cases):
    line = sys.stdin.readline().rstrip()
    line = line.split(" ")
    line = [int(num) for num in line]

    if line[0] < 0:
        print("NEGATIVE")
    elif line[0] > 0:
        print("POSITIVE")
    