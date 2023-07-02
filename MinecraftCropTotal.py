# Dominik Wrobel

# 02 - 06 - 2023

# Minecraft Calculations 

import math

import random

Fortune_Level = 3
#int(input("Fortune Level?"))

Rows = 75

Columns = 8

Crop = 1 
#input("Crop?")

Answer = 0

total = 0

for i in range(100000):
    y = random.randint(1,10000)
    if y <= 787:
        total += 1
    if y > 787 and y <= 3149+787:
        total += 2
    if y > 3149+787 and y <= 3149+787+4198:
        total += 3
    if y > 3149+787+4198 and y <= 3149+787+4198+1866:
        total += 4


Default_Drops = total/i

Default_Crop_Is_Seed = total/i + 1


Answer = 0


if Fortune_Level == 1:
    Answer = (Columns * Rows) * ((3 + 2/7) + Crop)
if Fortune_Level == 2:
    Answer = (Columns * Rows) * ((3 + 6/7) + Crop)
if Fortune_Level == 3:
    Answer = (Columns * Rows) * ((4 + 3/7) + Crop)



print(Answer)
