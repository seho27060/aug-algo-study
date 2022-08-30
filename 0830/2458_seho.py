# 220830 2458 키 순서
import sys
from collections import deque
def bfs(start):
    global graphs, orders
    queue = deque([start])
    graphs[start][start] = 0

    while queue:
        now = queue.popleft()
        for nxt in orders[now]:
            if graphs[start][nxt] == -1 or graphs[start][nxt] > graphs[start][now]+1:
                graphs[start][nxt] = graphs[start][now] + 1
                queue.append(nxt)

input = sys.stdin.readline

n, m = map(int,input().split())

graphs = [[-1]*(n) for _ in range(n)]
orders = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int,input().split())
    orders[a-1].append(b-1)

for start in range(n):
    bfs(start)
answer = 0
for start in range(n):
    result = 0
    for end in range(n):
        if graphs[start][end] != -1:
            result += 1
        if graphs[end][start] != -1:
            result += 1
    if result - 1 == n:
        answer += 1
print(answer)
