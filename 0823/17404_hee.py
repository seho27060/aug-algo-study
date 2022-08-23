import sys
INF = sys.maxsize
N = int(input())

G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

DP = [[0] * 3 for _ in range(N)] # RGB
ans = INF
for i in range(3):
    for j in range(3):
        if i == j:
            DP[0][j] = G[0][i]
        else:
            DP[0][j] = INF

    for j in range(1, N):
        DP[j][0] = min(DP[j-1][1], DP[j-1][2]) + G[j][0]
        DP[j][1] = min(DP[j-1][0], DP[j-1][2]) + G[j][1]
        DP[j][2] = min(DP[j-1][0], DP[j-1][1]) + G[j][2]
    for j in range(3):
        if i != j:
            ans = min(ans, DP[-1][j])
print(ans)