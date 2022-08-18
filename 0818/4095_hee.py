import sys
input = sys.stdin.readline
while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    G = []
    for _ in range(N):
        G.append(list(map(int, input().split())))

    ans = 0
    DP = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if x == 0 or y == 0:
                DP[y][x] = G[y][x]
                ans = max(ans, DP[y][x])
                continue

            if G[y][x]:
                DP[y][x] = min(DP[y-1][x], DP[y][x-1], DP[y-1][x-1]) + 1
                ans = max(ans, DP[y][x])

    print(ans)
