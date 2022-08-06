N, M = map(int, input().split())
K = int(input())
construction = []
for _ in range(K):
    construction.append(list(map(int, input().split())))

def chk(a, b, c, d):
    for ta, tb, tc, td in construction:
        if (a == ta and tb == b and tc == c and td == d) or (a == tc and b == td and c == ta and d == tb):
            return True

DP = [[0] * (N + 1) for _ in range(M + 1)]

for x in range(1, N+1):
    if not chk(x, 0, x-1, 0):
        DP[0][x] = 1
    else:
        break

for y in range(1, M+1):
    if not chk(0, y, 0, y-1):
        DP[y][0] = 1
    else:
        break

for x in range(1, N+1):
    for y in range(1, M+1):
        if not chk(x, y, x, y-1):
            DP[y][x] += DP[y-1][x]

        if not chk(x, y, x - 1, y):
            DP[y][x] += DP[y][x-1]

print(DP[-1][-1])