import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())

road = { i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int,input().split())
    road[a].append(b)
    road[b].append(a)


ST = [(R,0)]
visit = [0]*(N+1)
visit[R] = 1
result =[0]*(N+1)
while ST:
    now,cnt = ST.pop(0)

    result[now] = cnt

    for next in road[now]:
        if visit[next] == 0:
            ST.append((next,cnt+1))
            visit[next] =1

for r in range(1,N+1):
    if r == R:
        print(0)
    elif result[r] == 0:
        print(-1)
    else:
        print(result[r])