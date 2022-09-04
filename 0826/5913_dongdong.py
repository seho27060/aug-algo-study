# 백준 5913 준규와 사과

def dfs(x, y, cnt):
    global result
    if x == 5 and y == 5 and cnt == 0:
        result += 1
        return

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 1 <= next_x < 6 and 1 <= next_y < 6 and visited[next_x][next_y] == 0:
            visited[next_x][next_y] = 1
            dfs(next_x, next_y, cnt - 1)
            visited[next_x][next_y] = 0


K = int(input())
visited = [[0] * 6 for _ in range(6)]  # 방문 배열
for _ in range(K):
    i, j = map(int, input().split())
    visited[i][j] = 1  # 돌이 있는 위치를 방문한거로 만들어버리기
visited[1][1] = 1 # 시작 위치 체크
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
result = 0
cnt = 24 - K
dfs(1, 1, cnt)
print(result)
