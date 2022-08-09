import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

R, C = map(int, input().split())

G = [list(input().rstrip()) for _ in range(R)]

# print(G)
arr = [[] for _ in range(R)]

for r in range(R):
    for c in range(C):
        cnt = 0
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C:
                if G[nr][nc] == '.':
                    cnt += 1
            else:
                cnt += 1
        if cnt >= 3:
            arr[r].append('.')
        else:
            arr[r].append(G[r][c])

# print(arr)

minR, minC = 999, 999
maxR, maxC = -1, -1

for i in range(R):
    for k in range(C):
        if arr[i][k] == 'X':
            minR = min(minR, i)
            minC = min(minC, k)
            maxR = max(maxR, i)
            maxC = max(maxC, k)

for i in range(minR, maxR + 1):
    for k in range(minC, maxC + 1):
        print(arr[i][k], end='')
    print()

