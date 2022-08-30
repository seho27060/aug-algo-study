import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())

D = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    D[A][B] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if D[j][i] and D[i][k]:
                D[j][k] = 1

ans = 0
for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        temp += D[i][j] + D[j][i]
    if temp == N-1:
        ans += 1
print(ans)

