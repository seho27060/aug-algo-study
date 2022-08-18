# 220818 4095 최대 정사각형
# 1로만 이루어진 가장 큰 정사각형 찾기
# n,m <= 1,000 -> 1,000,000
# dp래, 한칸에서 좌 좌상 상 값 탐색

import sys

input = sys.stdin.readline

moves = [[-1,-1],[0,-1],[-1,0]]
while 1:
    n, m = map(int,input().split())
    if n == 0 and m == 0:
        break
    answer = 0
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[1]*(m) for _ in range(n)]

    for row in range(n):
        for col in range(m):
            if board[row][col] == 1:
                answer = max(1, answer)
                if row >= 1 and col >= 1:
                    check = True
                    minV = float('inf')
                    for move in moves:
                        nxtR = row + move[0]
                        nxtC = col + move[1]
                        if board[nxtR][nxtC] == 0:
                            check = False
                        else:
                            minV = min(visited[nxtR][nxtC],minV)
                    if check:
                        # print(row,col,minV)
                        visited[row][col] = minV+1
                        answer = max(answer,minV+1)
    print(answer)