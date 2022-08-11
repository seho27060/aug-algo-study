import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())


def func(x, y, N):
    if N == 1:
        return (G[y][x])

    if N == 2:
        L = []

        L.append(G[y][x])
        L.append(G[y][x + 1])
        L.append(G[y + 1][x])
        L.append(G[y + 1][x + 1])

        L.sort()
        return L[1]

    N //= 2
    L = []
    L.append(func(x, y, N))
    L.append(func(x + N, y, N))
    L.append(func(x, y + N, N))
    L.append(func(x + N, y + N, N))
    L.sort()
    return L[1]


G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

print(func(0, 0, N))
