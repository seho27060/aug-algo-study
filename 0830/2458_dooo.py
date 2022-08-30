n, m = map(int, input().split())

G = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if G[a][k] +G[k][b] == 2:
                G[a][b] = 1


cnt = [0] *(n+1)
for i in range(1, n+1):
    for j in range(1, n+1):
        if G[i][j] == 1:
            cnt[i] += 1
            cnt[j] += 1
print(cnt.count(n-1))