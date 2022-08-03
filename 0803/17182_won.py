import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

def f(cur, tmp, cnt):
    global ans
    if cnt == N:
        ans = min(ans, tmp)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            f(i, tmp + time[cur][i], cnt + 1)
            visited[i] = 0

N, K = map(int, input().split())
time = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
visited[K] = 1
ans = 999999999
for i in range(N):
    for k in range(N):
        for p in range(N):
            time[k][p] = min(time[k][p], time[k][i] + time[i][p])

f(K, 0, 1)

print(ans)
