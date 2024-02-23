import sys
import math
import string

radius = 40075/(2*math.pi)

cases = int(input().rstrip())
for i in range(cases):
    line = int(input()) # the whole line of text
   
    def better_round(val:float, n_digits:int = 0):
        val *= 10**n_digits
        result = int(val + (0.5 if val >= 0 else -0.5))
        return result / 10**n_digits

   
    if int(line) >= 160:
        print(better_round(2*math.pi*(radius + line), 1))

