import sys
# sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N, M = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if G[i][k] == 1 and G[k][j] == 1:
                G[i][j] = 1

ans = 0
for i in range(1, N + 1):
    rank = 0
    for k in range(1, N + 1):
        rank += G[k][i] + G[i][k]
    if rank == N - 1:
        ans += 1

print(ans)

