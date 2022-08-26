import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M, R = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

V = [False] * (N+1)
V[R] = True
Q = deque([(0, R)])
t, ans = 1, 0

while Q:
    cnt, n = Q.popleft()
    ans += t * cnt
    t += 1

    G[n].sort()
    for i in G[n]:
        if not V[i]:
            V[i] = True
            Q.append((cnt+1, i))
print(ans)