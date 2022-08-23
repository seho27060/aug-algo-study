n = int(input())

p = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
inf = 1e9

for i in range(3):
    dp = [[0 for _ in range(3)] for _ in range(n)]

    for j in range(3):
        if i == j:
            dp[0][j] = p[0][j]
        else:
            dp[0][j] = inf

    for k in range(1, n):
        dp[k][0] = min(dp[k - 1][1], dp[k - 1][2]) + p[k][0]
        dp[k][1] = min(dp[k - 1][0], dp[k - 1][2]) + p[k][1]
        dp[k][2] = min(dp[k - 1][0], dp[k - 1][1]) + p[k][2]

    for c in range(3):
        if i != c:
            ans = min(ans, dp[n-1][c])

print(ans)