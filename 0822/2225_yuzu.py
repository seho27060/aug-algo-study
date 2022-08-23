N, K = map(int, input().split())

dp = [[0]*N for i in range(K)]

for i in range(N):
    dp[0][i] = 1

for i in range(1, K):
    dp[i][0] = i+1

for i in range(1, K):
    for j in range(1, N):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[-1][-1])