# 220810 1022 소용돌이 예쁘게 출력하기
# -5000 ~ 5000 범위를 갖는 좌표에서
# 0,0 부터 1로하는 우상좌하 방향으로 돌아가는 소용돌이
# "이쁘게 출력하기"
# 10
#  0 일케 출력
# 1억 칸짜리 보드 구하고 r1+5000 c1+ 5000 해서 가져오기
import sys
input = sys.stdin.readline
sr,sc, er,ec = map(int,input().split())

moves = [[0,1],[1,0],[0,-1],[-1,0]]
board = [[0]*(ec-sc+1) for _ in range(er-sr+1)]
n = (ec-sc+1)*(er-sr+1)

r,c = 0,0
num = 1
cnt = 0
dst = 1
moveIdx = 0
maxNum = 0
while n > 0:
    # print(r,c,n)
    if sr <= r <= er and sc <= c <= ec:
        n -= 1
        board[r-sr][c-sc] = num
        maxNum = max(maxNum,num)
    num += 1
    cnt += 1
    r += moves[moveIdx][0]
    c += moves[moveIdx][1]

    if cnt == dst:
        cnt = 0
        moveIdx = (moveIdx+3)%4
        if moveIdx == 0 or moveIdx == 2:
            dst += 1
maxNumLen = len(str(maxNum))
# print(maxNumLen)
for row in range(er-sr+1):
    for col in range(ec-sc+1):
        print(str(board[row][col]).rjust(maxNumLen),end=" ")
    print()
