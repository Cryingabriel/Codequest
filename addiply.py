import sys
cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    line = sys.stdin.readline().rstrip()

    line = line.split(" ")
    print(int(line[0])+int(line[1]), int(line[0])*int(line[1]))