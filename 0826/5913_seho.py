# 220826 5913 준규와 사과
# dfs로 경우의 수 카운팅
# 제정신이아니군

import sys

input = sys.stdin.readline

def dfs(jr,jc,hr,hc):
    global n, visited, answer,moves
    visited[jr][jc] = 1
    visited[hr][hc] = 1

    if jr == hr and jc == hc:
        check = True
        for row in range(5):
            for col in range(5):
                if visited[row][col] == 0:
                    check = False
        if check:
            answer += 1
    else:
        for move in moves:
            njr, njc = jr + move[0], jc + move[1]
            if 0 <= njr < 5 and 0 <= njc < 5:
                if visited[njr][njc] == 0:
                    for move in moves:
                        nhr, nhc = hr + move[0], hc + move[1]
                        if 0 <= nhr < 5 and 0 <= nhc < 5:
                            if visited[nhr][nhc] == 0:
                                dfs(njr,njc,nhr,nhc)
    visited[jr][jc] = 0
    visited[hr][hc] = 0
    return

n = int(input())
visited = [[0]*(5) for _ in range(5)]
moves =[[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(n):
    r,c = map(int,input().split())
    visited[r-1][c-1] = -1
answer = 0
dfs(0,0,4,4)
print(answer)