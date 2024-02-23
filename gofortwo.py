cases = int(input().rstrip())

for i in range(cases):
    f = 0
    line = input().rstrip()
    line = line.split()
    if int(line[0])+15 == int(line[1]) or int(line[0])+13 == int(line[1]) or int(line[0])+11 == int(line[1]) or int(line[0])+10 == int(line[1]) or int(line[0])+8 == int(line[1]) or int(line[0])+5 == int(line[1]) or int(line[0])+4 == int(line[1]) or int(line[0])+2 == int(line[1]):
        f +=2
    elif int(line[0])+14 == int(line[1]) or int(line[0])+12 == int(line[1]) or int(line[0])+9 == int(line[1]) or int(line[0])+7 == int(line[1]) or int(line[0])+6 == int(line[1]) or int(line[0])+3 == int(line[1]) or int(line[0])+ 1 == int(line[1]) or int(line[0]) == int(line[1]):
        f +=1
    elif int(line[0])-1 == int(line[1]) or int(line[0])-5 == int(line[1]) or int(line[0])-12 == int(line[1]):
        f += 2
    elif int(line[0])-2 == int(line[1]) or int(line[0])-3 == int(line[1]) or int(line[0])-4 == int(line[1]) or int(line[0])-6 == int(line[1]) or int(line[0])-7 == int(line[1]) or int(line[0])-8 == int(line[1]) or int(line[0])-9 == int(line[1]) or int(line[0])-10 == int(line[1]) or int(line[0])-11 == int(line[1]) or int(line[0])-12 == int(line[1]):
        f += 1
    else:
        f+=1
    print(f)