from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    v[s] = 0
    cnt = 1
    lst[s] = cnt
    while q:
        c= q.popleft()
        for e in G[c]:
            if v[e] == -1:
                v[e] = v[c] + 1
                q.append(e)
                cnt += 1
                lst[e] = cnt

n, m, s = map(int, input().split())
G = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in G:
    i.sort()
v = [-1] * (n+1)
lst = [0] * (n+1)

bfs(s)
ans = 0
for i in range(1, n+1):
    ans += lst[i] * v[i]
print(ans)