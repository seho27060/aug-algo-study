import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations


N, M, R = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    # 0, 1
    for i in range(min(N, M) // 2):
        cr = i
        cc = i
        cur = G[cr][cc]

        for k in range(i + 1, N - i):
            cr = k
            post = G[cr][cc]
            G[cr][cc] = cur
            cur = post

        for k in range(i + 1, M - i):
            cc = k
            post = G[cr][cc]
            G[cr][cc] = cur
            cur = post

        for k in range(N - i - 2, i - 1, -1):
            cr = k
            post = G[cr][cc]
            G[cr][cc] = cur
            cur = post

        for k in range(M - i - 2, i - 1, -1):
            cc = k
            post = G[cr][cc]
            G[cr][cc] = cur
            cur = post

for i in G:
    print(*i)
