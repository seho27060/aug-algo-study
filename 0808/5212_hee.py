R, C = map(int, input().split())
G = []
for i in range(R):
    G.append(list(input()))

D = [(-1, 0), (1, 0), (0, 1), (0, -1)]
V = [[False] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if G[r][c] == 'X':
            cnt = 0
            for dr, dc in D:
                nr = r + dr
                nc = c + dc
                if not (-1 < nr < R and -1 < nc < C and (G[nr][nc] == 'X' or V[nr][nc])):
                    cnt += 1
            if 3 <= cnt:
                G[r][c] = '.'
                V[r][c] = True

i = 0
while True:
    if G[i] == ['.'] * C:
        G.pop(0)
    else:
        break

i = len(G) - 1
while True:
    if G[i] == ['.'] * C:
        G.pop()
        i -= 1
    else:
        break

L = len(G)
temp = list(zip(*G))

i = 0
while True:
    if list(temp[i]) == ['.'] * L:
        temp.pop(0)
    else:
        break

i = len(temp) - 1
while True:
    if list(temp[i]) == ['.'] * L:
        temp.pop()
        i -= 1
    else:
        break

ans = list(zip(*temp))
for i in ans:
    print(''.join(i))