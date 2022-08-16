# 220816 9465 스티커
# 한칸 뜯으면 해당 칸의 상하좌우는 사용불가가 됨
# n <= 100,000

import sys
input = sys.stdin.readline

moves = [[[0,2],[1,1],[1,2]],[[-1,1],[0,2],[-1,2]]] # 행 0일때 1일때 이동이다름

tcNum = int(input())

for tc in range(tcNum):
    n = int(input())
    answer = -1
    board = [list(map(int,input().split())) for _ in range(2)]
    visited = [[0]*n for _ in range(2)]
    visited[0][0] = board[0][0]
    visited[1][0] = board[1][0]

    for col in range(n):
        for row in range(2):
            answer = max(answer,visited[row][col])
            for move in moves[row]:
                nxtR, nxtC = row + move[0], col + move[1]
                if 0 <= nxtR < 2 and 0 <= nxtC < n:
                    if visited[nxtR][nxtC] < visited[row][col] + board[nxtR][nxtC]:
                        visited[nxtR][nxtC] = visited[row][col] + board[nxtR][nxtC]

    print(answer)