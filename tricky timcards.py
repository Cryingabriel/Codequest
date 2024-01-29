nums =[]
hours = 0
minutes = 0


cases = int(input().rstrip())
for i in range(cases):
    nums.clear()
    hours = 0
    minutes = 0
    line = input().rstrip().split(",")
    #print(line)
    for j in range(len(line)-1):
        nums.append((line[j+1]).split(":"))

    for k in range(len(nums)):
        hours += int(nums[k][0])
        minutes += int(nums[k][1])
        hours += int(minutes/60)
        minutes = minutes%60 #strip the numbers off

    if hours >= 1 and hours < 2:
        hourword = "hour"
    else:
        hourword = "hours"
    
    if minutes == 1:
        minuteword = "minute"
    else:
        minuteword = "minutes"
    if minutes == 0:
        print(line[0] + "=" + str(hours), hourword)
    else: print(line[0] + "=" + str(hours), hourword, minutes, minuteword)