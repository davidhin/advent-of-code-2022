from math import prod

import numpy as np

with open("day8_input.txt", "r") as f:
    data = f.read().splitlines()

# Part 1
data = np.array([list(map(int, i)) for i in data])

visible = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

for _ in range(4):
    dp = [[-1 for _ in range(len(data[0]))] for _ in range(len(data))]
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] > dp[row][col - 1]:
                visible[row][col] = 1
            dp[row][col] = max(data[row][col], dp[row][col - 1])
    data = np.rot90(data)
    visible = np.rot90(visible)

visible.sum()


# Part 2
data = [list(map(int, i)) for i in data]


def explore(data, row, col):
    curr_height = data[row][col]
    scenic_score = [0, 0, 0, 0]
    for idx in range(col + 1, len(data[0])):
        if data[row][idx] >= curr_height or idx == len(data[0]) - 1:
            scenic_score[1] = idx - col
            break
    for idx in range(col - 1, -1, -1):
        if data[row][idx] >= curr_height or idx == 0:
            scenic_score[3] = col - idx
            break
    for idx in range(row + 1, len(data)):
        if data[idx][col] >= curr_height or idx == len(data) - 1:
            scenic_score[2] = idx - row
            break
    for idx in range(row - 1, -1, -1):
        if data[idx][col] >= curr_height or idx == 0:
            scenic_score[0] = row - idx
            break

    return prod(scenic_score)


# Part 2
max_scenic_score = 0
for row in range(len(data[0])):
    for col in range(len(data)):
        max_scenic_score = max(max_scenic_score, explore(data, row, col))

max_scenic_score
