import pandas as pd
import numpy as np

list1 = []
list2 = []
with open("input.txt") as f:
    for line in f:
        data = line.strip().split()
        list1.append(int(data[0]))
        list2.append(int(data[1]))

assert len(list1) == len(list2)
list1.sort()
list2.sort()

distance = 0
for i, j in zip(list1, list2):
    distance += abs(i - j)


print("The distance is: ", distance)


# similarity score
sim_score = 0
for i in list1:
    cnt = 0
    for j in list2:
        if i == j:
            cnt += 1

    sim_score += i * cnt

print("The similarity score is: ", sim_score)
