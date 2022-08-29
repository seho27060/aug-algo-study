N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

sx, sy = 0, 0
ex, ey = N-1, M-1

q = [(sx, sy, 0)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
ans = T+1
while q:
    x, y, z = q.pop(0)
    if arr[x][y] == 2:
        if ans > z+(abs(N-1-x))+abs(M-1-y):
            ans = z+(abs(N-1-x))+abs(M-1-y)
    if x == ex and y == ey:
        if ans > z:
            ans = z
    for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
        nx = x+dx
        ny = y+dy
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0 and arr[nx][ny] != 1:
            q.append((nx, ny, z+1))
            visited[nx][ny] = 1

print('Fail') if ans == T+1 else print(ans)