import sys
input = sys.stdin.readline

dY = [0, 1, 0, -1]
dX = [1, 0, -1, 0]

N, M, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# 회전 몇개로 나뉨
standard = min(N, M) // 2

# 회전 수만큼 반복
for i in range(R):
    for j in range(standard):
        # 회전 나뉘는 수만큼 0,0 -> 1,1 -> 2,2 순
        sY = j
        sX = j
        dir = 0
        tmp = maps[sY][sX]
        # 4방향이 전부 돌때까지 하면 그룹 1개 끝
        while dir<4:
            nY = sY+dY[dir]
            nX = sX+dX[dir]
            if j<=nX<M-j and j<=nY<N-j:
                maps[sY][sX] = maps[nY][nX]
                sY = nY
                sX = nX
            else:
                dir+=1
        maps[j+1][j] = tmp

for i in range(N):
    print(*maps[i])