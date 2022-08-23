import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations


N, K = map(int, input().split())

dp = [[0] * 201 for _ in range(201)]


# dp[K][N]
for i in range(1, 201):
    dp[1][i] = 1
    dp[2][i] = i + 1
    dp[i][1] = i

for i in range(2, 201):
    for k in range(2, 201):
        dp[i][k] = (dp[i][k - 1] + dp[i - 1][k]) % 1000000000

print(dp[K][N])
