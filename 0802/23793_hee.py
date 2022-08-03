import sys
from heapq import *
input = sys.stdin.readline
INF = sys.maxsize

def dijk(flag, start, mid, end):
    D = [INF] * (N+1)
    Q = [(0, start)]
    D[start] = 0
    while Q:
        c, n1 = heappop(Q)

        if D[n1] < c:
            continue

        for cost, n2 in G[n1]:
            if flag and n2 == mid:
                continue

            if c + cost < D[n2]:
                D[n2] = c + cost
                heappush(Q, (D[n2], n2))
    return D[end]

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append((w, v))

x, y, z = map(int, input().split())

with_y = dijk(0, x, y, y) + dijk(0, y, y, z)
if INF <= with_y:
    with_y = -1

without_y = dijk(1, x, y, z)
if INF <= without_y:
    without_y = -1
print(with_y, without_y)