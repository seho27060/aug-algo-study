import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations


while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    G = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    ans = 0

    for i in range(1, N + 1):
        for k in range(1, M + 1):
            if G[i - 1][k - 1] == 1:
                dp[i][k] = min(dp[i - 1][k], dp[i][k - 1], dp[i - 1][k - 1]) + 1

                if ans < dp[i][k]:
                    ans = dp[i][k]
    print(ans)
