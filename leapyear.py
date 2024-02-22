cases = int(input())

for i in range(cases):
    f = int(input())
    for i in range(f):
        r = int(input())

        if r < 1582:
            print("No")
        elif r % 4 >= 1:
            print("No")
        elif r % 100 >= 1:
            print("Yes")
        elif r % 400 >=1:
            print("No")
        else:
            print("Yes")