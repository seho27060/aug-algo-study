# 220824 16926 배열 돌리기 1
# n*m 배열을 정해진 규칙대로 돌려보자
# 돌려돌려!~

import sys

input = sys.stdin.readline

n,m,r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
answer =[[0]*(m) for _ in range(n)]

for _ in range(r):
    for s in range(min(n,m) //2):
        sr, sc = s, s
        start = board[sr][sc]

        for nxt in range(s+1,n-s):
            sr = nxt
            prev = board[sr][sc]
            board[sr][sc] = start
            start = prev
        for nxt in range(s+1,m-s):
            sc = nxt
            prev = board[sr][sc]
            board[sr][sc] = start
            start = prev
        for nxt in range(s+1,n-s):
            sr = n - nxt - 1
            prev = board[sr][sc]
            board[sr][sc] = start
            start = prev
        for nxt in range(s+1,m-s):
            sc = m - nxt - 1
            prev = board[sr][sc]
            board[sr][sc] = start
            start = prev

for ans in board:
    print(*ans)