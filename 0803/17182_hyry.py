def permutation(depth, curV):
    global minV
    if depth == N:
        minV = min(minV, curV)
        return

    if curV > minV:
        return

    for neiP in range(N):
        if not visit[neiP]:
            visit[neiP] = True
            perm[depth] = neiP
            permutation(depth + 1, curV + adj[perm[depth - 1]][neiP])
            visit[neiP] = False


N, K = map(int, input().split())
adj = [list(map(int, input().split())) for _ in range(N)]

for mid in range(N):
    for i in range(N):
        for j in range(N):
            adj[i][j] = min(adj[i][j], adj[i][mid] + adj[mid][j])

visit = [False] * N
perm = [-1] * N

visit[K] = True
perm[0] = K

minV = 1e10
permutation(1, 0)

print(minV)