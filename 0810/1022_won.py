import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

r1, c1, r2, c2 = map(int, input().split())

rr = r2 - r1 + 1
cc = c2 - c1 + 1

G = [[0] * cc for _ in range(rr)]
total = rr * cc

r = 0
c = 0
inputNum = 1
d = 0
i = 0
k = 1
maxNum = -1

while total > 0:
    if r1 <= r <= r2 and c1 <= c <= c2:
        total -= 1
        G[r - r1][c - c1] = inputNum
        maxNum = inputNum

    inputNum += 1
    i += 1
    r += dr[d]
    c += dc[d]

    if i == k:
        i = 0
        d = (d + 1) % 4
        if d % 2 == 0:
            k += 1

length = len(str(maxNum))

for i in range(rr):
    for k in range(cc):
        print(str(G[i][k]).rjust(length), end=' ')
    print()

