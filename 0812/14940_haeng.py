from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

MAP = []

for i in range(n):
    A = list(map(int,input().split()))
    if 2 in A:
        start = (A.index(2),i)
    MAP.append(A)


ST = deque()
ST.append((start[0],start[1],0))
visit = [[0]*m for _ in range(n)]
visit[start[1]][start[0]] = 1
while ST:
    x,y,cnt = ST.popleft()

    MAP[y][x] = cnt

    for dy,dx in (1,0),(0,1),(-1,0),(0,-1):
        X = x + dx
        Y = y + dy
        if 0<=X<m and 0<=Y<n and MAP[Y][X] and visit[Y][X] == 0:
            ST.append((X,Y,cnt+1))
            visit[Y][X] = 1

for y in range(n):
    for x in range(m):
        if visit[y][x] == 0 and MAP[y][x]:
            MAP[y][x] = -1

for y in MAP:
    print(*y)