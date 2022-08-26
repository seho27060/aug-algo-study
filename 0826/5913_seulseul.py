import sys
input = sys.stdin.readline

farm = [[0] * 6 for _ in range(6)]

K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    farm[y][x] = 2

dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]
ans = 0
farm[1][1] = 1

def btrk(cY, cX, depth):
    global ans
    if cY==5 and cX==5:
        if depth == 25-K:
            ans += 1

    for i in range(4):
        nY = cY + dY[i]
        nX = cX + dX[i]
        if 0<nY<6 and 0<nX<6 and farm[nY][nX]==0:
            farm[nY][nX]=1
            btrk(nY, nX, depth+1)
            farm[nY][nX]=0

btrk(1, 1, 1)
print(ans)