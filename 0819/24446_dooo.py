from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    v[s] = 1
    while q:
        c = q.popleft()
        for e in G[c]:
            if v[e] == 0:
                v[e] = v[c] + 1
                q.append(e)


n, m, s = map(int, input().split())

G = [[] for _ in range(n+1)]

for _ in range(m):
    a, b  = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

v = [0] * (n+1)
bfs(s)
for i in range(1, n+1):
    print(v[i]-1)