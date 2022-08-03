# 220803 17182 우주 탐사선
# 모든 노드 탐사, 재방문가능, 모든 탐사하는데 걸리는 최소시간
# n < 10
import sys
from heapq import *
from itertools import permutations
input = sys.stdin.readline

def djk(start):
    global board, dst, n
    queue =[]
    heappush(queue,[0,start])
    dst[start][start] = 0
    while queue:
        cost, now = heappop(queue)
        for nxt in range(n):
            nxtCost = board[now][nxt]
            if dst[start][nxt] > cost + nxtCost:
                dst[start][nxt] = cost + nxtCost
                heappush(queue,[cost+nxtCost,nxt])

def backtrack(start,cnt,cost):
    global visited, n, answer, board,dst

    if cnt == n:
        answer = min(answer,cost)
        return
    for nxt in range(n):
        if visited[nxt] == 0:
            visited[nxt] = 1
            backtrack(nxt,cnt+1, cost+dst[start][nxt])
            visited[nxt] = 0
n, k = map(int, input().split())  # n, k 발사시점
board = [list(map(int,input().split())) for _ in range(n)]
# i에서 j 까지의 최단거리를 djk로 구하자
dst = [[float('inf')]*n for _ in range(n)]
for s in range(n):
    djk(s)
visited = [0]*n
visited[k] = 1

now = k
answer = float('inf')
backtrack(k,1,0)
print(answer)
