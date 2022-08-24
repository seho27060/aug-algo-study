n, k = map(int, input().split())

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][1] = 1
for j in range(k+1):
    dp[0][j] = 1

for i in range(1, n+1):
    for j in range(2, k+1):
        for s in range(i+1):
            dp[i][j] += dp[s][j-1]
print(dp[n][k]%1000000000)