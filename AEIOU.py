import sys
num = 0
cases = (int(sys.stdin.readline().rstrip()))



for i in range(cases):
    line = sys.stdin.readline().rstrip()

    line = line.split(" ")
    if len(line) == "a" or "e" or "i" or "o" or  "u":
        num += 1

print(num)