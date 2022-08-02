

import heapq
import collections
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

x, y, z = map(int, input().split())

def dijkstra(t, f):
    dist = [INF] * (n + 1)
    q = [(0, t)]
    dist[t] = 0
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue
        for v, w in graph[node]:
            if v == y and f == 1:
                continue
            if d+w < dist[v]:
                dist[v] = d+w
                heapq.heappush(q, (d+w, v))
    return dist

dij1 = dijkstra(x, 0)
a = dij1[y]
dij2 = dijkstra(y, 0)
b = dij2[z]
dij3 = dijkstra(x, 1)
c = dij3[z]

ans1 = -1
ans2 = -1
if a != INF and b != INF:
    ans1 = a+b
if c != INF:
    ans2 = c
print(ans1, ans2)