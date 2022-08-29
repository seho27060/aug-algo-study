dx = [1,-1,0,0]
dy = [0,0,-1,1]

N,M,T = map(int,input().split())
road = []
for _ in range(N):
    road.append(list(map(int,input().split())))

ST = [(0,0,0,0)]
visit = [[0]*M for _ in range(N)]
visit2 = [[0]*M for _ in range(N)]
visit[0][0] = 1

result = 0
while ST:
    nx,ny,cnt,gram = ST.pop(0)

    if ny == N-1 and nx == M-1 and cnt <= T:
        result = cnt
        break

    if road[ny][nx] == 2:
        gram = 1

    for i in range(4):
        X = nx + dx[i]
        Y = ny + dy[i]
        if 0<=X<M and 0<=Y<N:
            if gram and visit2[Y][X] == 0:
                visit2[Y][X] = 1
                ST.append((X,Y,cnt+1,gram))
            elif road[Y][X] != 1 and visit[Y][X] == 0:
                visit[Y][X] = 1
                ST.append((X, Y, cnt + 1, gram))

if result:
    print(result)
else:
    print('Fail')
