dx=[1,-1,0,0]
dy=[0,0,1,-1]

def check(x,y):
    cnt = 0
    if x == 0:
        cnt += 1
    if x == C-1:
        cnt +=1
    if y ==0 :
        cnt += 1
    if y == R-1:
        cnt +=1
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if 0<=X<C and 0<=Y<R and Map[Y][X]=='.' and visit[Y][X]==0:
            cnt += 1
    if cnt >= 3:
        return 1




R,C = map(int,input().split())

Map = []
for _ in range(R):
    Map.append(list(input()))

visit=[[0]*C for _ in range(R)]

for y in range(R):
    for x in range(C):
        if Map[y][x] == 'X' and check(x,y):
            Map[y][x] = '.'
            visit[y][x] =1


while Map and'X' not in Map[0]:
    Map.pop(0)
while Map and 'X' not in Map[-1]:
    Map.pop()

while 1:
    L = len(Map)
    c = 0
    for i in range(L):
        if Map[i][0] == '.':
            c += 1
    if c == L:
        for i in range(L):
            Map[i].pop(0)
    else:
        break

while 1:
    L = len(Map)
    c = 0
    for i in range(L):
        if Map[i][-1] == '.':
            c += 1
    if c == L:
        for i in range(L):
            Map[i].pop()
    else:
        break

for y in range(len(Map)):
    result = ''
    for x in range(len(Map[y])):
        result += Map[y][x]
    print(result)
