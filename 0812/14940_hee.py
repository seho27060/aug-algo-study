from collections import deque
N, M = map(int, input().split())

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs():
    V[S[1]][S[0]] = 0
    Q = deque([S])
    while Q:
        x, y = Q.popleft()
        for dx, dy in D:
            nx = x + dx
            ny = y + dy
            if -1 < nx < M and -1 < ny < N and V[ny][nx] == -1 and G[ny][nx] == 1:
                V[ny][nx] = V[y][x] + 1
                Q.append((nx, ny))
                    
G = []
for i in range(N):
    temp = list(map(int, input().split()))
    G.append(temp)
    for j in range(M):
        if temp[j] == 2:
            S = (j, i)
            
V = [[-1] * M for _ in range(N)]
bfs()

for i in range(N):
    for j in range(M):
        if G[i][j] == 0:
            V[i][j] = 0
    print(*V[i])