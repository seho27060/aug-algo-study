K = int(input())
graph = [[0]*5 for _ in range(5)]
for _ in range(K):
    i, j = map(int, input().split())
    graph[i-1][j-1] = [1]
graph[0][0] = 1

ans = 0
def dfs(x, y, cnt):
    global ans
    if x == 4 and y == 4 and cnt == 0:
        ans += 1
        return
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx = x+dx
        ny = y+dy
        if 0<=nx<5 and 0<=ny<5 and graph[nx][ny] == 0:
            graph[nx][ny] = 1
            dfs(nx, ny, cnt-1)
            graph[nx][ny] = 0
dfs(0, 0, 24-K)
print(ans)