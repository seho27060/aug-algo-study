import sys
INF = sys.maxsize
input = sys.stdin.readline

N = int(input())
D = [[INF, []] for _ in range(N+1)]
D[1][0], D[1][1] = 0, [1]
for i in range(2, N+1):
    if i % 3 == 0:
        D[i][0] = D[i//3][0] + 1
        D[i][1] = list(D[i//3][1])
        D[i][1].append(i)

    if i % 2 == 0 and D[i//2][0] + 1 < D[i][0]:
        D[i][0] = D[i//2][0] + 1
        D[i][1] = list(D[i//2][1])
        D[i][1].append(i)

    if D[i-1][0] + 1 < D[i][0]:
        D[i][0] = D[i-1][0] + 1
        D[i][1] = list(D[i-1][1])
        D[i][1].append(i)

print(D[N][0])
D[N][1].reverse()
print(*D[N][1])