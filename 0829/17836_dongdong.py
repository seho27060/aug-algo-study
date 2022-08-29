# 백준 17836 공주님을 구해라! - 너비우선탐색
# 그람을 구해서 갈 때와 그렇지 않을 때를 따로 생각해보기..

from collections import deque


def bfs():
    result = 10001
    Q.append((0, 0))
    visited[0][0] = 1
    while Q:
        x, y = Q.popleft()
        # 공주님 만난 경우, 공주는 끝 칸에 있다
        if (x, y) == (N - 1, M - 1):
            return min(visited[x][y] - 1, result)

        # 그람 만난 경우
        if arr[x][y] == 2:
            # 그람을 만나면 그 자리에서 공주까지의 거리를 그냥 더해주면 된다
            # 왜?? 그람으로 뽀갤 수 있는 벽 갯수 제한없음 그냥 때려부수면서 공주한테 가자
            result = visited[x][y] - 1 + N - 1 - x + M - 1 - y

        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            # 범위 체크, 방문여부 체크
            if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
                if arr[next_x][next_y] == 0 or arr[next_x][next_y] == 2:
                    visited[next_x][next_y] = visited[x][y] + 1  # 누적하며 visited배열 채워주기
                    Q.append((next_x, next_y))

    return result


N, M, T = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
arr = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
visited = [[0] * M for _ in range(N)]

ans = bfs()
if ans > T:
    print('Fail')
else:
    print(ans)
