import sys
cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    r = int(input())
    weight = 0
    health = 0
    for i in range(r):
        line = sys.stdin.readline().rstrip()
        line = line.split(" ")
        if line[0] == "LOW":
            weight += 1
        elif line[0] == "MEDIUM":
            weight += 2
        elif line[0] == "HIGH":
            weight += 3

        if line[0] == "MEDIUM":
            health += int(line[1])*2
        elif int(line[1]) >= 0 and int(line[1]) <= 10:
            health += int(line[1])
        
    
    health = (health//weight)*10
    print((health))