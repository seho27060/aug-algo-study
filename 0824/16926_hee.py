N, M, R = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

for _ in range(R):
    for i in range(min(N, M) // 2):
        temp = G[i][i]
        for j in range(i+1, M-i):
            G[i][j-1] = G[i][j]

        for j in range(i+1, N-i):
            G[j-1][M-i-1] = G[j][M-i-1]

        for j in range(M-i-1, i-1, -1):
            G[N-i-1][j] = G[N-i-1][j-1]

        for j in range(N-i-1, i, -1):
            G[j][i] = G[j-1][i]

        G[i+1][i] = temp

for i in G:
    print(*i)