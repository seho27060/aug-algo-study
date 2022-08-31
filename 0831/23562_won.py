import sys
# sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations


n, m = map(int, input().split())
a, b = map(int, input().split())
G = [list(input().rstrip()) for _ in range(n)]
# print(G)
ans = float('inf')
cnt = 0
for i in range(n):
    for k in range(m):
        if G[i][k] == '#':
            cnt += 1

for k in range(1, min(n, m) // 3 + 1):
    size = k * 3
    # sr, sc
    for sr in range(n - size + 1):
        for sc in range(m - size + 1):
            total = 0
            bCnt = cnt
            for cr in range(sr, sr + size):
                for cc in range(sc, sc + size):
                    if G[cr][cc] == '.':
                        total += a
                    if G[cr][cc] == '#':
                        bCnt -= 1
            total += bCnt * b
            for cr in range(sr + k, sr + 2 * k):
                for cc in range(sc + k, sc + 3 * k):
                    if G[cr][cc] == '.':
                        total -= a
                    if G[cr][cc] == '#':
                        total += b
            ans = min(ans, total)
print(ans)