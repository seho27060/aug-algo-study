# 220829 17836 공주님을 구해라!
import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*(m) for _ in range(n)]
visited[0][0] = 0
queue = deque([[0,0]])
moves = [[0,1],[0,-1],[-1,0],[1,0]]

while queue:
    now = queue.popleft()
    if board[now[0]][now[1]] == 2:
        # print(visited[now[0]][now[1]] + abs(n-1-now[0])+abs(m-1-now[1]))
        if visited[n-1][m-1] == -1 or visited[n-1][m-1] > visited[now[0]][now[1]] + abs(n-1-now[0])+abs(m-1-now[1]):
            visited[n-1][m-1] = visited[now[0]][now[1]] + abs(n-1-now[0])+abs(m-1-now[1])

    for move in moves:
        nxtR, nxtC = now[0] + move[0], now[1] + move[1]
        if 0 <= nxtR < n and 0 <= nxtC < m:
            if board[nxtR][nxtC] != 1:
                if visited[nxtR][nxtC] == -1 or visited[nxtR][nxtC] > visited[now[0]][now[1]] + 1:
                    visited[nxtR][nxtC] = visited[now[0]][now[1]] + 1
                    queue.append([nxtR,nxtC])
if visited[n-1][m-1] == -1 or visited[n-1][m-1] > t:
    print("Fail")
elif visited[n-1][m-1] <= t:
    print(visited[n-1][m-1])