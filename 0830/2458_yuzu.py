import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [[0]*N for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    visited[u-1][v-1] = 1

for p in range(N):
    for q in range(N):
        for r in range(N):
            if visited[q][p] + visited[p][r] == 2:
                visited[q][r] = 1

cnt = [0]*N
ans = 0
for i in range(N):
    for j in range(N):
        cnt[i] += visited[i][j] + visited[j][i]
    if cnt[i] == N-1:
        ans += 1

print(ans)