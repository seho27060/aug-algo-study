import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra(start, adj, notY=False):
    Q = [(0, start)]
    dist = [1e10] * (V + 1)
    dist[start] = 0
    visit = set()

    while Q:
        cost, curV = heappop(Q)
        if curV in visit: continue
        visit.add(curV)

        for neiCost, neiV in adj[curV]:
            if (not notY or (notY and neiV != Y)) and dist[neiV] > dist[curV] + neiCost\
                    and neiV not in visit:
                dist[neiV] = dist[curV] + neiCost
                heappush(Q, (cost + neiCost, neiV))

    return dist


V, E = map(int, input().split())
adj1 = [[] for _ in range(V + 1)]
adj2 = [[] for _ in range(V + 1)]

for _ in range(E):
    v1, v2, w = map(int, input().split())
    adj1[v1].append((w, v2))
    adj2[v2].append((w, v1))

X, Y, Z = map(int, input().split())

dist1 = dijkstra(X, adj1)
dist2 = dijkstra(Z, adj2)
dist3 = dijkstra(X, adj1, True)

XYZ = dist1[Y] + dist2[Y]
XZ = dist3[Z]

if XYZ >= 1e10: XYZ = -1
if XZ >= 1e10: XZ = -1

print(XYZ, XZ)