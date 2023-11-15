import sys
cases = int(sys.stdin.readline().rstrip())

def reverse(x):
    return x[::-1]#reverse the string


for i in range(cases):
    line = input()
    line2 = reverse(line)
    print(line2)