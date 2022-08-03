# 백준 17182 우주탐사선 - 플로이드 와샬, 백트래킹

# 플로이드 와샬 - 모든 정점에서 모든 정점으로의 최단경로를 구할 때 사용
# 백트래킹 - 최적화 결정 문제를 푸는 방법, 해를 찾는 도중 해가 아니어서 막히면 되돌아가서 다시 해를 찾는 기법

# 백트래킹 함수
def backtrack(position, cnt, cost):
    global result

    if cnt == N:
        result = min(result, cost)
        return

    for next in range(N):
        if not visited[next]:
            visited[next] = 1
            backtrack(next, cnt + 1, cost + time[position][next])
            visited[next] = 0


# 백트래킹 전혀 이해가 안되는데;;; 공부를 좀 더 해봐야 겠다...


# N = 행성의 개수  K = ana호 발사되는 행성 위치
N, K = map(int, input().split())
time = [list(map(int, input().split())) for _ in range(N)]
# print(time)

# 플로이드 와샬
visited = [0] * N  # 방문 체크 배열
result = 999999999999999
visited[K] = 1
# 플로이드와샬 점화식 모르면 그냥 외우자 이렇게 푼다.....
for k in range(N):
    for i in range(N):
        for j in range(N):
            time[i][j] = min(time[i][j], time[i][k] + time[k][j])

backtrack(K, 1, 0)
print(result)