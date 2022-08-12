# 220812 14940 쉬운 최단거리
# n <= 1000, 출발점찾고 bfs로 전체탐색
import sys
from collections import deque

input = sys.stdin.readline

def bfs(r,c):
    global board,n,m
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    result = [[float('inf')]*(m) for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if board[row][col] == "0":
                result[row][col] = 0
    queue = deque([[r,c]])
    result[r][c] = 0

    while queue:
        now = queue.popleft()
        cost = result[now[0]][now[1]]
        for move in moves:
            nxtR, nxtC = now[0]+move[0], now[1] + move[1]
            if 0<= nxtR < n and 0<=nxtC<m:
                if board[nxtR][nxtC] == "1" and result[nxtR][nxtC] > cost+1:
                    result[nxtR][nxtC] = cost+1
                    queue.append([nxtR,nxtC])
    for res in result:
        for loc in res:
            if loc >= float('inf'):
                print(-1,end=" ")
            else:
                print(loc, end=" ")
        print()
    exit()
n, m = map(int,input().split())

board = [list(input().split()) for _ in range(n)]

for row in range(n):
    for col in range(m):
        if board[row][col] == "2":
            bfs(row,col)