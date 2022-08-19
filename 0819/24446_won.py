import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations


N, M, R = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

def f(r):
    qu = deque()
    qu.append(r)
    visited[r] = 0
    while qu:
        t = qu.popleft()

        for i in G[t]:
            if visited[i] == -1:
                qu.append(i)
                visited[i] = visited[t] + 1
visited = [-1] * (N + 1)

f(R)
for i in range(1, N + 1):
    print(visited[i])
