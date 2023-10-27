cases = int(input())

for i in range (cases):
    line = input()
    
    line = line.split(" ")
    
    line[0] = int(line[0])
    
    if line[0] % 2 == 0:
        print("EVEN")
    else:
        print("ODD")