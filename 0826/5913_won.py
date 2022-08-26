import sys
input = sys.stdin.readline
# sys.stdin = open("sample_input.txt", "r")
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

G = [[0] * 5 for _ in range(5)]
visited = [[0, 0]]

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    # 1 => 돌, 0 => 사과
    G[i][j] = 1

ans = 0

def f(cr, cc):
    global ans
    if cr == 4 and cc == 4:
        if len(visited) == 25 - K:
            ans += 1
        return
    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < 5 and 0 <= nc < 5 and [nr, nc] not in visited and G[nr][nc] == 0:
            visited.append([nr, nc])
            f(nr, nc)
            visited.remove([nr, nc])

f(0, 0)

print(ans)
