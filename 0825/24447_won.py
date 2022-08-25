import sys
input = sys.stdin.readline
# sys.stdin = open("sample_input.txt", "r")
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N, M, R = map(int, input().split())
G = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)
tmp = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in G:
    i.sort()

# print(G)
def f(s):
    qu = deque()
    qu.append(s)
    visited[s] = 0
    cnt = 1
    tmp[s] = cnt
    while qu:
        t = qu.popleft()

        for i in G[t]:
            if visited[i] == -1:
                visited[i] = visited[t] + 1
                qu.append(i)
                cnt += 1
                tmp[i] = cnt

f(R)
# print(tmp)
# print(visited)

ans = 0
for i in range(1, N + 1):
    ans += tmp[i] * visited[i]

print(ans)
