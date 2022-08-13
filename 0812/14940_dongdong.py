# 백준 14940 쉬운 최단거리 - bfs

from collections import deque


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(y, x):
    Q = deque()
    Q.append([y, x])
    result[y][x] = 0   # 목표지점은 어차피 0

    while Q:
        y, x = Q.popleft()

        for i in range(4):
            next_y, next_x = y+dy[i], x+dx[i]   # 반복문 돌면서 다음 지점 체크

            # 범위 체크, 방문 했는지 체크
            if 0 <= next_y < n and 0 <= next_x < m and result[next_y][next_x] == -1:
                # 갈 수 있는지 체크
                if arr[next_y][next_x] == 0:    # 갈 수 없다면
                    result[next_y][next_x] = 0    # 어차피 0
                elif arr[next_y][next_x] == 1:   # 갈 수 있다면
                    result[next_y][next_x] = result[y][x] + 1 # 이전 위치의 거리에서 +1 해준다
                    Q.append([next_y, next_x])



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[-1] * m for _ in range(n)]   # 거리 저장 배열 못가면 -1이니까 초기값 -1
# 목표 지점 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 and result[i][j] == -1:
            bfs(i, j)
            break



for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=" ")
        else:
            print(result[i][j], end=" ")
    print()
