import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    Q = deque([S])
    visit = [-1] * (V + 1)
    visit[S] = order = sumV = 0

    while Q:
        curV = Q.popleft()
        order += 1
        sumV += order * visit[curV]

        for neiV in adj[curV]:
            if visit[neiV] == -1:
                Q.append(neiV)
                visit[neiV] = visit[curV] + 1

    return sumV


V, E, S = map(int, input().split())
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

for subAdj in adj:
    subAdj.sort()

print(bfs())