import sys
cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    line = (input())
    line = line.split(" ")
    line = [int(num) for num in line]

    if line[0] == line[1]:
        f = (line[0] + line[1])*2
        print(f)
    else:
        f = (line[0] + line[1])
        print(f)

