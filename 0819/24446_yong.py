# bfs를 활용한 그래프 탐색문제
# 모든 노드값을 -1로 탐색한 뒤 방문표시를 하며 시작노드에서 탐색 진행

import sys
from collections import deque
input = sys.stdin.readline

def bfs(r):
    visited = [0] * (N+1)
    ans = [-1] * (N+1)
    q = deque()
    q.append((r, 0))
    visited[r] = True
    ans[r] = 0

    while q:
        node, dep = q.popleft()
        ans[node] = dep

        for v in G[node]:
            if not visited[v]:
                q.append((v, dep+1))
                visited[v] = True 
    for i in ans[1:]:
        print(i)

N, M, R = map(int, input().split())

G = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(N+1):
    G[i].sort()

bfs(R)