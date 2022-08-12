# visited를 활용한 bfs문제
# 배열을 생성할 때 조건에 맞춰 배열을 만들면 나머지는 쉽게 풀이 가능


from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs():
    q = deque()
    q.append((ty, tx))
    visited[ty][tx] = 0
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
    for i in range(n):
        print(*visited[i])


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            ty, tx = i, j
        if arr[i][j] == 0:
            visited[i][j] = 0

bfs()