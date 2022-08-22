# DP를 활용한 문제
# K개를 활용해 N을 만드는 경우는 0 ~ N 각각의 수를 기준으로 나머지 수를 만드는 방법

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(0, N+1):
    for j in range(1, K+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[N][K] % 1000000000)