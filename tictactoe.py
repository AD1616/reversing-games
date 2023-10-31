import random

board = [[0] * 3 for _ in range(3)]

total_1 = 0
minimizer = 0
maximizer = 0

def set_min_max(sum): 
    if total_1 == 5:
        maximizer = 1
        minimizer = -1
    elif total_1 == 4:
        maximizer = -1
        minimizer = 1
    elif sum == 3:
        maximizer = 1
        minimizer = -1
    elif sum == -3:
        maximizer = -1
        minimizer = 1


for i in range(3):
    for j in range(3):
        if board[i][j] == 1:
            total_1 += 1

for i in range(3):
    print(board[i])

for i in range(3):
    sum = 0
    for j in range(3):
        sum += board[i][j]
    set_min_max(sum)

for i in range(3):
    sum = 0
    for j in range(3):
        sum += board[j][i]
    set_min_max(sum)

