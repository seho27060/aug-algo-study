# 220823 17404 RGB거리 2
# n <= 1000,
# 빠초파중 하나로, 각 칠하는데  비용듬
# 규칙 지키면서 모든 집을 칠하는 최솟값을 구해보자

import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
# 1 - n?
# 0시작, 1시작, 2시작
answer = float('inf')
for start in range(3):
    dp = [[float("inf"), float("inf"), float("inf")] for _ in range(1001)]
    dp[0][start] = board[0][start]
    for idx in range(1,n-1):
        dp[idx][0] = min(dp[idx-1][1],dp[idx-1][2]) + board[idx][0]
        dp[idx][1] = min(dp[idx-1][0],dp[idx-1][2]) + board[idx][1]
        dp[idx][2] = min(dp[idx - 1][0], dp[idx - 1][1]) + board[idx][2]
    last =board[n-1].copy()
    last[start] = float('inf')
    dp[n-1][0] = min(dp[n-1 - 1][1], dp[n-1 - 1][2]) + last[0]
    dp[n-1][1] = min(dp[n-1 - 1][0], dp[n-1 - 1][2]) + last[1]
    dp[n-1][2] = min(dp[n-1 - 1][0], dp[n-1 - 1][1]) + last[2]
    answer = min(answer, min(dp[n-1]))
# print(min([red,green,blue]))
print(answer)