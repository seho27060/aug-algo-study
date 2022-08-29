import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [[1e10] * N for _ in range(N)]

for i in range(N):
    MAP[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    MAP[a - 1][b - 1] = 1
    MAP[b - 1][a - 1] = -1

for mid in range(N):
    for i in range(N):
        for j in range(N):
            if MAP[i][mid] == MAP[mid][j] != 1e10:
                MAP[i][j] = MAP[i][mid]  # or MAP[mid][j]

cnt = 0
for sub in MAP:
    for s in sub:
        if s == 1e10: break
    else:
        cnt += 1

print(cnt)