import sys
from heapq import *
input = sys.stdin.readline
INF = sys.maxsize

N, M, T = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

V = [[0] * M for _ in range(N)]
VS = [[0] * M for _ in range(N)]
V[0][0] = True
Q = [(0, False, 0, 0)]
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while Q:
    cnt, gram, x, y = heappop(Q)

    if T < cnt:
        print('Fail')
        break

    if x == M-1 and y == N-1:
        print(cnt)
        break

    for dx, dy in D:
        nx = x + dx
        ny = y + dy

        if -1 < ny < N and -1 < nx < M:
            if gram and not VS[ny][nx]:
                VS[ny][nx] = True
                heappush(Q, (cnt + 1, gram, nx, ny))

            else:
                if not V[ny][nx]:
                    V[ny][nx] = True
                    if G[ny][nx] == 0:
                        heappush(Q, (cnt + 1, gram, nx, ny))

                    elif G[ny][nx] == 2:
                         heappush(Q, (cnt + 1, True, nx, ny))

else:
    print('Fail')
