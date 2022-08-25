# bfs문제

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q =  deque([R])
    visited[R] = 0
    cnt = 0
    sumV = 0
    while q:
        r = q.popleft()
        cnt += 1
        sumV += cnt * visited[r]

        for i in G[r]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[r] + 1
    return sumV


N, M, R = map(int, input().split())

G = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

for i in G:
    i.sort()

print(bfs())