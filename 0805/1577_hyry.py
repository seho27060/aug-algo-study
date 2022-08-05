import sys
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

dist = [[0] * (C + 1) for _ in range(R + 1)]

for row in range(R + 1):
    dist[row][0] = 1

for col in range(C + 1):
    dist[0][col] = 1

stuck = set()
for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())

    if r1 == r2 == 0:
        dist[0][max(c1, c2)] = 0
    elif c1 == c2 == 0:
        dist[max(r1, r2)][0] = 0
    else:
        if r1 == r2:
            if c1 < c2:
                stuck.add(((r1, c1), (r2, c2)))
            else:
                stuck.add(((r2, c2), (r1, c1)))
        elif r1 < r2:
            stuck.add(((r1, c1), (r2, c2)))
        else:
            stuck.add(((r2, c2), (r1, c1)))

for row in range(1, R + 1):
    dist[row][0] = min(dist[row][0], dist[row - 1][0])

for col in range(1, C + 1):
    dist[0][col] = min(dist[0][col], dist[0][col -1])


for row in range(1, R + 1):
    for col in range(1, C + 1):
        up = dist[row - 1][col] if ((row - 1, col), (row, col)) not in stuck else 0
        left = dist[row][col - 1] if ((row, col - 1), (row, col)) not in stuck else 0

        dist[row][col] = up + left


print(dist[R][C])