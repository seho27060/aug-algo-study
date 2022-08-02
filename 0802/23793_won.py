import sys
input = sys.stdin.readline
# from collections import deque
from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations
INF = 10 ** 10
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append([w, v])
x, y, z = map(int, input().split())

def f1(s, e):
    # 꼭 지나야할때
    qu = []
    dist = [INF] * (N + 1)
    dist[s] = 0
    qu.append([0, s])
    while qu:
        cur_dist, cur_node = heappop(qu)

        if dist[cur_node] < cur_dist:
            continue

        for new_dist, new_node in G[cur_node]:
            if dist[new_node] > cur_dist + new_dist:
                dist[new_node] = cur_dist + new_dist
                heappush(qu, [cur_dist + new_dist, new_node])

    return dist[e]

def f2(s, e):
    qu = []
    dist = [INF] * (N + 1)
    dist[s] = 0
    qu.append([0, s])
    while qu:
        cur_dist, cur_node = heappop(qu)

        if dist[cur_node] < cur_dist:
            continue

        for new_dist, new_node in G[cur_node]:
            if new_node == y:
                continue
            if dist[new_node] > cur_dist + new_dist:
                dist[new_node] = cur_dist + new_dist
                heappush(qu, [cur_dist + new_dist, new_node])

    return dist[e]


res1 = f1(x, y)
res2 = f1(y, z)
res3 = f2(x, z)

if res1 == INF or res2 == INF:
    print(-1, end=' ')
else:
    print(res1 + res2, end=' ')
if res3 == INF:
    print(-1)
else:
    print(res3)
