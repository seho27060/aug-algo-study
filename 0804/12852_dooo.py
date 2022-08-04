import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

def bfs(s):
    q = deque()
    q.append([s])
    while q:
        clst = q.popleft()
        c = clst[0]
        if  c== 1:
            return clst
        if c%3 ==0:
            q.append([c//3] + clst)
        if c%2 == 0:
            q.append([c//2] + clst)

        q.append([c-1] + clst)
ans = bfs(n)
print(len(ans)-1)
print(*ans[::-1])