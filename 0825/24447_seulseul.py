from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]

# 방문 여부
visited = [-1] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

cnt = 0
total = 0
q = deque([R])
visited[R] = 0
while q:
    now = q.popleft()
    cnt+=1
    total += cnt * visited[now]
    for next in arr[now]:
        if visited[next] == -1:
            visited[next] = visited[now]+1
            q.append(next)
print(total)