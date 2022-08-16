T = int(input())

for _ in range(T):
    n = int(input())
    G = []
    for _ in range(2):
        G.append([0] + list(map(int, input().split())))

    DP = [[0] * (n+1) for _ in range(2)]
    for i in range(1, n+1):
        DP[0][i], DP[1][i] = max(DP[0][i-2], DP[1][i-2], DP[1][i-1]) + G[0][i], max(DP[0][i-1], DP[0][i-2], DP[1][i-2]) + G[1][i]

    print(max(DP[0][-1], DP[1][-1]))
