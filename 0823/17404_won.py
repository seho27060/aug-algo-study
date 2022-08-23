import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

INF = float('inf')
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = INF

for i in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][i] = arr[0][i]
    for k in range(1, N):
        dp[k][0] = arr[k][0] + min(dp[k - 1][1], dp[k - 1][2])
        dp[k][1] = arr[k][1] + min(dp[k - 1][0], dp[k - 1][2])
        dp[k][2] = arr[k][2] + min(dp[k - 1][0], dp[k - 1][1])

    for k in range(3):
        if i == k:
            continue
        ans = min(ans, dp[N - 1][k])

print(ans)
