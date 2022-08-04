# 220805 1577 도로의 개수
# 0,0 -> n,m 이동
# 근데 못가는 도로 존재

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
k = int(input())
visited = [[0]*(m+1) for _ in range(n+1)]
visited[0][0] = 1
noways = [[[] for i in range(m+1)] for j in range(n+1)]
for _ in range(k):
    a,b,c,d = map(int,input().split())
    lst = [[a,b],[c,d]]
    lst.sort()
    noways[lst[0][0]][lst[0][1]].append(lst[1])
moves = [[0,1],[1,0]]
for row in range(n+1):
    for col in range(m+1):
        for move in moves:
            nxtR, nxtC = row+move[0],col+move[1]
            if 0 <= nxtR <= n and 0<= nxtC <=m:
                if [nxtR,nxtC] not in noways[row][col]:
                    visited[nxtR][nxtC] += visited[row][col]
# for kk in visited:
#     print(kk)
print(visited[-1][-1])
