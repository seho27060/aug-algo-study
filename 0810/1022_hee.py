r1, c1, r2, c2 = map(int, input().split())
R, C = r2 - r1 + 1, c2 - c1 + 1

G = [[0] * C for _ in range(R)]

D = [(1, 0), (0, -1), (-1, 0), (0, 1)]

x, y = 0, 0
d = 0
N = R * C
val, L = 1, 1

while True:
    if N == 0:
        break

    for _ in range(2):
        for _ in range(L):
            if c1 <= x <= c2 and r1 <= y <= r2:
                N -= 1
                G[y - r1][x - c1] = val
                max_val = val
            x += D[d][0]
            y += D[d][1]
            val += 1
        d = (d+1) % 4
    L += 1

for r in range(R):
    for c in range(C):
        print(str(G[r][c]).rjust(len(str(max_val))), end=' ')
    print()




