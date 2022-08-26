# 220825 24447 알고리즘 수업 - 너비 우선 탐색 4
# 무방향 그래프, 가중치1 ,모든 노드에대한 d*t의 합 구하기
# 오름차순 방문

import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int,input().split())
graphs = [[] for _ in range(n+1)]
visited = [[-1,0] for _ in range(n+1)]
depth = 1

for _ in range(m):
    u, v = map(int,input().split())
    graphs[u].append(v)
    graphs[v].append(u)

queue = deque([r])

visited[r][0] = 0
while queue:
    now = queue.popleft()
    graphs[now].sort(reverse=True)
    for nxt in graphs[now]:
        if visited[nxt][0] == -1:
            depth += 1
            visited[nxt] = [visited[now][0]+1, depth]
            queue.append(nxt)
answer = 0
for ans in visited:
    answer += ans[0]*ans[1]
print(answer)