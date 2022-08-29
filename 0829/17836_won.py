import sys
# sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def f(sr, sc):
    qu = deque()
    visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
    qu.append([sr, sc, 0])
    visited[sr][sc][0] = 0
    while qu:
        cr, cc, g = qu.popleft()

        if cr == N - 1 and cc == M - 1:
            return visited[cr][cc][g]

        if visited[cr][cc][g] > T:
            return 'Fail'

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][g] == -1:
                if G[nr][nc] == 0:
                    visited[nr][nc][g] = visited[cr][cc][g] + 1
                    qu.append([nr, nc, g])
                if G[nr][nc] == 1 and g == 1:
                    visited[nr][nc][g] = visited[cr][cc][g] + 1
                    qu.append([nr, nc, g])
                if G[nr][nc] == 2:
                    visited[nr][nc][1] = visited[cr][cc][g] + 1
                    qu.append([nr, nc, 1])
    return 'Fail'

N, M, T = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

ans = f(0, 0)
print(ans)
