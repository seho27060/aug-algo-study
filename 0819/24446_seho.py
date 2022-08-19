# 220819 24446 알고리즘 수업 - 너비 우선 탐색 3
# n개 노드 m개 간선 무방향 그래프
# n <= 100,000/ m <= 200,000

import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int,input().split())
nodes = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int,input().split())
    nodes[s].append(e)
    nodes[e].append(s)

queue = deque([r])
visited = [-1]*(n+1)
visited[r] = 0

while queue:
    now = queue.popleft()

    for nxt in nodes[now]:
        if visited[nxt] > visited[now] + 1 or visited[nxt] == -1:
            visited[nxt] = visited[now]+1
            queue.append(nxt)

for result in visited[1:]:
    print(result)