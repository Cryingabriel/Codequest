cases = int(input())

for i in range (cases):
    line = input()
    line = line.split(" ")

    line = [int(num) for num in line] #how to make the list into a int instead of a string
    print(max(line))
    
