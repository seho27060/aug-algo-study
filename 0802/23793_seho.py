# 220802 23793 두 단계 최단 경로 1
# n < 100,000/ m < 200,000
# 간선에 가중치있음, 방향이 있는 그래프
# x -> y -> z 최단거리와 x -> z(y를 거치지않는) 최단거리찾기

import sys
from heapq import *
input = sys.stdin.readline

def djk(s,e,visited,prohibit):
    global n, graphs
    visited[s] = 0

    queue = []
    heappush(queue,[0,s])

    while queue:
        cost, now = heappop(queue)
        if now == e:
            break
        if visited[now] < cost:
            continue
        for nxt, nxtCost in graphs[now]:
            if nxt != prohibit:
                if visited[nxt] >= cost + nxtCost:
                    visited[nxt] = cost + nxtCost
                    heappush(queue,[cost + nxtCost,nxt])
n, m = map(int,input().split())
graphs = [[] for _ in range(n+1)]
xyVisited = [float("inf")]*(n+1)
yzVisited = [float("inf")]*(n+1)
xzVisited = [float('inf')]*(n+1)

for _ in range(m):
    u, v, w = map(int,input().split())
    graphs[u].append([v,w])
x, y, z = map(int,input().split())
djk(x,y,xyVisited,-1)
djk(y,z,yzVisited,-1)
djk(x,z,xzVisited,y)

xyz = xyVisited[y] + yzVisited[z]
xz = xzVisited[z]
if xyz >= float('inf'):
    xyz = -1
if xz >= float('inf'):
    xz = -1
print(xyz,xz)