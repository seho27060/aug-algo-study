import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N, M = map(int, input().split())
K = int(input())
G = [[[0] * 2 for _ in range(N + 1)] for _ in range(M + 1)]
for _ in range(K):
    a, b, c, d = map(int, input().split())
    if abs(c - a) == 1:
        G[min(b, d)][min(c, a)][0] = 1
    if abs(d - b) == 1:
        G[min(b, d)][min(c, a)][1] = 1
dp = [[0] * (N + 1) for _ in range(M + 1)]
tmp = 1
for i in range(1, N + 1):
    if G[0][i - 1][0] == 1:
        tmp = 0
    dp[0][i] = tmp
tmp = 1
for i in range(1, M + 1):
    if G[i - 1][0][1] == 1:
        tmp = 0
    dp[i][0] = tmp
for i in range(1, M + 1):
    for k in range(1, N + 1):
        if G[i][k - 1][0] == 1 and G[i - 1][k][1] == 1:
            continue
        if G[i][k - 1][0] == 1:
            dp[i][k] = dp[i - 1][k]
        elif G[i - 1][k][1] == 1:
            dp[i][k] = dp[i][k - 1]
        else:
            dp[i][k] = dp[i - 1][k] + dp[i][k - 1]

print(dp[M][N])
