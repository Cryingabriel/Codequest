import math
import sys
cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    line = int(input().rstrip())

    print(line, end = " ")

    if line % 2 == 0:
        print("Yang", end = " ")
    else:
        print("Yin", end = " ")

    attributes = ["Wood", "Fire", "Earth", "Metal", "Water"]
    element = line - 4
    element = element%10
    element = math.floor(element/2)
    print(attributes[element], end = " ")

    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    year = line - 4
    year = year%12
    print(animals[year])
