# 백준 24446 알고리즘 수업 - 너비 우선 탐색 3

from collections import deque

def bfs(x):
    Q = deque()
    Q.append(x)
    visited[x] = 0

    while Q:
        node = Q.popleft()
        for i in arr[node]:
            if visited[i] == -1:
                Q.append(i)
                visited[i] = visited[node] + 1  # 1씩 가중


N, M, R = map(int, input().split())

arr = [[] for _ in range(N+1)]
# print(arr)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [-1] * (N+1)  # 정답 배열 및 방문 체크 배열, 방문하면 값 변경, 방문 못하면 -1 출력

bfs(R)

# print(visited)
for i in range(1, N+1):
    print(visited[i])
    