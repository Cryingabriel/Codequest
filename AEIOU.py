import sys

cases = (int(sys.stdin.readline().rstrip()))



for i in range(cases):
    line = sys.stdin.readline().rstrip()
    num = 0
    f = len(line)
    for i in range(f): 
       if line[i] == "a" or line[i] == "e" or line[i] == "i" or line[i] == "o" or  line[i] =="u":
            num += 1

    print(num)