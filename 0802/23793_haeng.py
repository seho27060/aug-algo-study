import heapq
import sys
input = sys.stdin.readline

def problem1(S,E):
    visit =[2000000001]*(N+1)
    visit[S] = 0

    ST = [(0,S)]
    while ST:
        cnt,now = heapq.heappop(ST)

        if visit[now] < cnt:
            continue

        for c,next in road[now]:
            if visit[next] > cnt+c:
                visit[next] = cnt+c
                heapq.heappush(ST,(cnt+c,next))

    if visit[E] != 2000000001:
        return visit[E]

def problem2():
    visit =[2000000001]*(N+1)
    visit[Y] = -1
    visit[X] =0
    ST = [(0,X)]
    while ST:
        cnt,now = heapq.heappop(ST)

        if visit[now] < cnt:
            continue

        for c,next in road[now]:
            if visit[next] > cnt+c:
                visit[next] = cnt+c
                heapq.heappush(ST,(cnt+c,next))

    if visit[Z] != 2000000001:
        result.append(visit[Z])
    else:
        result.append(-1)



N,M = map(int,input().split())
road = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    road[a].append((c,b))

X,Y,Z = map(int,input().split())
result =[]
A = problem1(X,Y)
B = problem1(Y,Z)
if A and B:
    result.append(A+B)
else:
    result.append(-1)
problem2()

print(*result)