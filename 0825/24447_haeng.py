N,M,R = map(int,input().split())
road = { i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int,input().split())
    road[a].append(b)
    road[b].append(a)

for i in range(1,N+1):
    road[i].sort()

result = [(0,0)]*(N+1)
result[R] = (1,0)
ST=[(R,0)]

s = 1
while ST:
    now,cnt = ST.pop(0)
    for i in road[now]:
        if result[i] == (0,0):
            s += 1
            result[i] = (cnt+1,s)
            ST.append((i,cnt+1))

ans = 0
for a,b in result:
    ans += a*b

print(ans)