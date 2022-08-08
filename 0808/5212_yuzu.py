R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
result = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'X':
            cnt = 0
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx = i+dx
                ny = j+dy
                if 0<=nx<R and 0<=ny<C and graph[nx][ny] == '.':
                    cnt += 1
                elif 0>nx or R<=nx or 0>ny or C<=ny:
                    cnt += 1
            if cnt >= 3:
                result[i][j] = '.'
            else:
                result[i][j] = 'X'
        else:
            result[i][j] = '.'

r = []
c = []
for i in range(R):
    for j in range(C):
        if result[i][j] == 'X':
            r.append(i)
            c.append(j)

for i in range(min(r), max(r)+1):
    for j in range(min(c), max(c)+1):
        print(result[i][j], end='')
    print()