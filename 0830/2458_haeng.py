#자신의 위와 아래의 갯수를 자신빼고 다 알수 있는경우 찾기
def route(x):
    cnt = 0

    ST = [x]
    visit = [0]*(N+1)
    visit[x] = 1
    while ST:
        now = ST.pop(0)

        for j in UP[now]:
            if visit[j] == 0:
                ST.append(j)
                visit[j] = 1
                cnt += 1


    ST = [x]
    visit = [0] * (N+1)
    visit[x] = 1
    while ST:
        now = ST.pop(0)

        for j in DOWN[now]:
            if visit[j] == 0:
                ST.append(j)
                visit[j] = 1
                cnt += 1

    return cnt


N,M = map(int,input().split())

UP = {i:[] for i in range(1,N+1)}
DOWN = {i:[] for i in range(1,N+1)}


for _ in range(M):
    a,b = map(int,input().split())
    UP[a].append(b)
    DOWN[b].append(a)


result = 0
for i in range(1,N+1):
    if route(i) == N-1:
        result += 1

print(result)