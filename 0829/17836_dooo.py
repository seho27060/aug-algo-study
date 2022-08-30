dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


from collections import deque

def bfs(sx, sy, k):
    q = deque()
    q.append((sx, sy, k))
    v[sx][sy][k] = 1
    while q:
        cx, cy, ck = q.popleft()
        if cx == n-1 and cy == m-1:
            return v[cx][cy][ck] - 1
        if v[cx][cy][ck] == t+1:
            return "Fail"

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if ck == 0:
                if 0 <= nx < n and 0 <= ny < m and v[nx][ny][ck] == 0 and arr[nx][ny] == 0:
                    q.append((nx, ny, 0))
                    v[nx][ny][ck] = v[cx][cy][ck] + 1
                elif  0 <= nx < n and 0 <= ny < m and v[nx][ny][ck] == 0 and arr[nx][ny] == 2:
                    q.append((nx, ny, 0))
                    q.append((nx, ny, 1))
                    v[nx][ny][0] = v[cx][cy][ck] + 1
                    v[nx][ny][1] = v[cx][cy][ck] + 1
            else:
                if 0 <= nx < n and 0 <= ny < m and v[nx][ny][ck] == 0:
                    q.append((nx, ny, 1))
                    v[nx][ny][ck] = v[cx][cy][ck] + 1
    return "Fail"
n, m, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

v = [[[0]*2 for _ in range(m)] for _ in range(n)]

print(bfs(0, 0, 0))