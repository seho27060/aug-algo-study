import heapq

def find(now,cnt):
    global result
    if visit==[1]*N:
        if cnt < result:
            result = cnt
        return

    if cnt > result:
        return
    for i,c in enumerate(road[now]):
        if i == now or visit[i]: continue
        visit[i] = 1
        find(i,cnt+c)
        visit[i] = 0

def short(x):
    C = [100001]*N
    C[x] = 0
    ST = [(0,x)]

    while ST:
        cnt, now = heapq.heappop(ST)

        if C[now] > cnt: continue
        for next,c in enumerate(road[now]):
            if C[next] > cnt+c:
                C[next] = cnt+c
                heapq.heappush(ST,(cnt+c,next))
    road[i] = C

N,K = map(int,input().split())
road = {}
for i in range(N):
    road[i] = list(map(int,input().split()))

for i in range(N):
    short(i)

visit = [0]*N
visit[K] =1
result =100001
find(K,0)
print(result)