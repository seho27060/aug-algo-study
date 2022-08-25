from collections import deque

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs():
    cnt = 0
    ans = 0
    q = deque()
    q.append(R)
    visited[R] = 0
    while q:
        x = q.popleft()
        cnt += 1
        ans += cnt*visited[x]
        graph[x].sort(reverse=True)
        for i in graph[x]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[x]+1
    return ans

print(bfs())