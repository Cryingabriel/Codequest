import sys
cases = (int(sys.stdin.readline().rstrip()))


for i in range(cases):
    line = sys.stdin.readline().rstrip()
    line = line.split(" ")
    line = [int(num) for num in line]
    small = line[0]
    big = line[1] * 5
    total = line[2]
    
    if big == total or small == total or small + big == total:
        print("true")
    else:
        print("false")