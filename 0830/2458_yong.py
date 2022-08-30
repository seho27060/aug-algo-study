# 플로이드 워셜 문제
# 자신이 갈 수 있는 노드와 자신에게 올 수 있는 노드의 합이 N-1인 경우 자신의 순서를 알 수 있다

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if arr[j][k] == 1 or (arr[j][i] == 1 and arr[i][k] == 1):
                arr[j][k] = 1

ans = 0
for i in range(1, N+1):
    height = 0
    for j in range(1, N+1):
        height += arr[i][j] + arr[j][i]
    if height == N-1:
        ans += 1
print(ans)