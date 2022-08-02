import heapq
import sys

input = sys.stdin.readline
inf = sys.maxsize


def dijk(s, md):
    d = [inf] * (n + 1)
    q = []
    d[s] = 0
    heapq.heappush(q, (0, s))
    if md == 0:
        while q:
            dist, now = heapq.heappop(q)
            if d[now] < dist:
                continue
            for j in G[now]:
                cost = dist + j[1]

                if d[j[0]] > cost:
                    d[j[0]] = cost
                    heapq.heappush(q, (cost, j[0]))
    else:
        while q:
            dist, now = heapq.heappop(q)
            if d[now] < dist:
                continue
            for j in G[now]:

                if j[0] == k:
                    continue
                cost = dist + j[1]
                if d[j[0]] > cost:
                    d[j[0]] = cost
                    heapq.heappush(q, (cost, j[0]))
    return d


n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))

s, k, e = map(int, input().split())
start = dijk(s, 0)
middle = dijk(k, 0)
ans = start[k] + middle[e]
if ans >= inf:
    print(-1, end=" ")
else:
    print(ans, end=" ")

no = dijk(s, 1)
if no[e] == inf:
    print(-1)
else:
    print(no[e])