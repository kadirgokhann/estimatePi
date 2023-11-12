from random import random
import math

attempt = 10000000
count = 0

for i in range(attempt):   
    x = random() * 2 - 1
    y = random()
    realY = math.sqrt(1 - x**2)
    if y <= realY:
        count += 1

rectArea = 2 * 1
circArea = count/attempt * rectArea * 2

print(circArea / 1**2)
