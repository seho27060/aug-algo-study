# 구현문제
# 행과 열중  작은값을 2로 나누고 그만큼 안으로 들어가 배열을 회전한다.

import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2):
        x = y = i
        tmp = G[y][x]

        for j in range(i+1, N-i):
            y = j
            val = G[y][x]
            G[y][x] = tmp
            tmp = val

        for j in range(i+1, M-i):
            x = j
            val = G[y][x]
            G[y][x] = tmp
            tmp = val

        for j in range(i+1, N-i):
            y = N-j-1
            val = G[y][x]
            G[y][x] = tmp
            tmp = val

        for j in range(i+1, M-i):
            x = M-j-1
            val = G[y][x]
            G[y][x] = tmp
            tmp = val

for i in range(N):
    for j in range(M):
        print(G[i][j], end=' ')
    print()