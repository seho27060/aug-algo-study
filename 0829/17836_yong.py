# bfs문제
# 벽을 뚫을 수 있는지 아닌지를 구분하기 위해 방문배열을 2차원배열로 생성
# 검을 발견할 경우 방문 배열을 변경하여 bfs진행

import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs():
    ans = 10001
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        y, x, g = q.popleft()
        if y == N-1 and x == M-1:
            ans = min(ans, visited[g][y][x]-1)
            continue    
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if not g:
                if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] != 1 and not visited[0][ny][nx]:
                    if arr[ny][nx] == 2:
                        if not visited[1][ny][nx]:
                            visited[1][ny][nx] = visited[0][y][x] + 1
                            q.append((ny, nx, 1))
                    else:
                        visited[0][ny][nx] = visited[0][y][x] + 1
                        q.append((ny, nx, 0))
            else:
                if 0 <= ny < N and 0 <= nx < M and not visited[1][ny][nx]:
                    visited[1][ny][nx] = visited[1][y][x] + 1
                    q.append((ny, nx, 1))
    if ans == 10001 or ans > T:
        print("Fail")
    else:
        print(ans)

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            gramr = (i, j)
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
bfs()