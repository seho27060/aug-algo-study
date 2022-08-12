import sys
input = sys.stdin.readline

def bfs():
    Q = [(sR, sC)]
    visit[sR][sC] = 0

    while Q:
        curR, curC = Q.pop(0)

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C and MAP[newR][newC] != 0 \
                    and visit[newR][newC] == -1:
                Q.append((newR, newC))
                visit[newR][newC] = visit[curR][curC] + 1


R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]

sR = sC = -1
noPath = []
for row in range(R):
    for col in range(C):
        if MAP[row][col] == 2:
            sR, sC = row, col
        if MAP[row][col] == 0:
            noPath.append((row, col))

visit = [[-1] * C for _ in range(R)]
bfs()

for r, c in noPath:
    visit[r][c] = 0

for lst in visit:
    print(*lst)