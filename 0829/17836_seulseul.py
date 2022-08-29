from collections import deque
import sys
input = sys.stdin.readline

dY = [-1, 1, 0, 0]
dX = [0, 0, -1, 1]

N, M, T = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
# 그람검 도달 여부
flag = False

# 그람검 X
def non(sY, sX):
    global gY, gX
    global dist
    global flag
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    q = deque([[sY, sX]])
    while q:
        cY, cX = q.popleft()
        for i in range(4):
            nY = cY+dY[i]
            nX = cX+dX[i]
            if 0<=nY<N and 0<=nX<M and not visited[nY][nX] and maps[nY][nX] != 1:
                if maps[nY][nX] == 2:
                    flag = True
                    gY, gX = nY, nX
                    dist = visited[cY][cX]
                q.append([nY, nX])
                visited[nY][nX] = visited[cY][cX]+1
    if not visited[N-1][M-1]:
        return 10001
    else:
        return visited[N-1][M-1]-1

def gram(sY, sX):
    visited2 = [[0]*M for _ in range(N)]
    visited2[sY][sX] = dist
    q = deque([[sY, sX]])
    while q:
        cY, cX = q.popleft()
        for i in range(4):
            nY = cY+dY[i]
            nX = cX+dX[i]
            if 0<=nY<N and 0<=nX<M and not visited2[nY][nX]:
                visited2[nY][nX] = visited2[cY][cX]+1
                q.append([nY, nX])
    if not visited2[N-1][M-1]:
        return 10001
    else:
        return visited2[N-1][M-1]

ans1 = non(0, 0)
ans2 = 10001
if flag:
    ans2 = gram(gY, gX)
print(ans2)


if ans1>10000 and ans2>10001:
    print("Fail")
else:
    ans = min(ans1, ans2)
    if ans > T:
        print("Fail")
    else:
        print(ans)
