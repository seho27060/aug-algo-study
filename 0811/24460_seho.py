# 220812 24460 특별상이라도 받고 싶어
# n*n//백트래킹..분할정복../ n =1024
# 값주어질때 특별상 받을수있는 자리번호구하기

import sys

input = sys.stdin.readline

def backtrack(r,c,rank):
    global board
    # print(r,c,rank)
    if rank == 1:
        return board[r][c]
    else:
        nxtRank = rank//2
        result = sorted([backtrack(r-nxtRank,c,nxtRank),backtrack(r-nxtRank,c-nxtRank,nxtRank),backtrack(r,c-nxtRank,nxtRank),backtrack(r,c,nxtRank)])[1]
        return result
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
print(backtrack(n-1,n-1,n))

