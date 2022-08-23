N,K = map(int,input().split())

dp= [[0]*(N+1) for _ in range(K)]

for i in range(N+1):
    dp[0][i] =1
for j in range(K):
    dp[j][0] = 1

for y in range(1,K):
    for x in range(1,N+1):
        dp[y][x] = dp[y-1][x] + dp[y][x-1]


print(dp[K-1][N]%1000000000)