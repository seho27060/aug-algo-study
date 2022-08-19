import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs(s):
    V[s] = 0
    Q = deque([s])
    while Q:
        n = Q.popleft()

        for i in G[n]:
            if V[i] == -1:
                V[i] = V[n] + 1
                Q.append(i)
    

N, M, R = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

V = [-1] * (N+1)
bfs(R)
for i in range(1, N+1):
    print(V[i])