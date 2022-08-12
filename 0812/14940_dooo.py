dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    q = []
    q.append((sx, sy))
    v[sx][sy] = 1
    while q:
        cx, cy = q.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0 and arr[nx][ny] == 1:
                q.append((nx, ny))
                v[nx][ny] = v[cx][cy] + 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]

def start():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                bfs(i,j)
                return
start()
for i in range(n):
    for j in range(m):
        if v[i][j] == 0 and arr[i][j] == 0:
            print(v[i][j], end = " ")
        else:
            print(v[i][j] - 1, end = " ")
    print()