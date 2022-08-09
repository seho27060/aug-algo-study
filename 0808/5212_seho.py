# 220808 5212 지구 온난화
#

import sys

input = sys.stdin.readline

r, c = map(int,input().split())
board = [list(input()) for _ in range(r)]
answer = []
moves = [[0,1],[0,-1],[-1,0],[1,0]]
for row in range(r):
    result = []
    for col in range(c):
        cnt = 0
        for move in moves:
            nxtR = row + move[0]
            nxtC = col + move[1]
            if 0 <= nxtR < r and 0 <= nxtC < c:
                if board[nxtR][nxtC] == "X":
                    cnt += 1
        if cnt >= 2 and board[row][col] == "X":
            result.append("X")
        else:
            result.append(".")
    answer.append(result)
minR,maxR = float('inf'), -1
minC, maxC = float('inf'), -1
for row in range(r):
    for col in range(c):
        if answer[row][col] == "X":
            minR = min(minR,row)
            maxR = max(maxR,row)
            minC = min(minC,col)
            maxC = max(maxC,col)
for row in range(minR,maxR+1):
    for col in range(minC,maxC+1):
        print(answer[row][col],end="")
    print()
