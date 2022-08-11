import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())

G = [list(map(int, input().split())) for _ in range(n)]


def f(sr, sc):
    qu = deque()
    qu.append([sr, sc])
    visited[sr][sc] = 0
    while qu:
        cr, cc = qu.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < n and 0 <= nc < m and G[nr][nc] != 0 and visited[nr][nc] == -1:
                qu.append([nr, nc])
                visited[nr][nc] = visited[cr][cc] + 1

visited = [[-1] * m for _ in range(n)]

for i in range(n):
    for k in range(m):
        if G[i][k] == 2:
            f(i, k)
            break


for i in range(n):
    for k in range(m):
        if G[i][k] == 0:
            visited[i][k] = 0


for i in visited:
    print(*i)
