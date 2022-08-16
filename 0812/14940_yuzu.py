from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = [[-1 for _ in range(m)] for _ in range(n)]

sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            sx, sy = i, j
            ans[i][j] = 0
        elif arr[i][j] == 0:
            ans[i][j] = 0

visited = [[0 for _ in range(m)] for _ in range(n)]

q = deque()
q.append((sx, sy, 0))
visited[sx][sy] = 1

while q:
    x, y, z = q.popleft()
    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and arr[nx][ny] == 1:
            ans[nx][ny] = z+1
            visited[nx][ny] = 1
            q.append((nx, ny, z+1))

for i in range(n):
    print(*ans[i])