import sys
input = sys.stdin.readline

def bfs():
    Q = [S]
    visit[S] = 0

    while Q:
        curV = Q.pop(0)

        for neiV in adj[curV]:
            if visit[neiV] == -1:
                Q.append(neiV)
                visit[neiV] = visit[curV] + 1


V, E, S = map(int, input().split())

adj = [[] for _ in range(V + 1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

visit = [-1] * (V + 1)
bfs()

for idx in range(1, V + 1):
    print(visit[idx])
    