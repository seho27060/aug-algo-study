from collections import deque
N = int(input())

ST = deque()
visit =[[1000,0] for _ in range(N+1)]
visit[N] = [0,0]
ST.append((0,N))

result=deque()
while ST:
    cnt,now = ST.popleft()

    if now == 1:
        result.appendleft(1)
        while now < N:
            if visit[now][1] == 1:
                now += 1
            else:
                now = now * visit[now][1]
            result.appendleft(now)
        break
    if now%3==0 and visit[now//3][0] > cnt+1:
        visit[now//3]=[cnt+1,3]
        ST.append((cnt+1,now//3))

    if now%2==0 and visit[now//2][0] > cnt+1:
        visit[now//2] = [cnt+1,2]
        ST.append((cnt+1,now//2))

    if visit[now-1][0] > cnt+1:
        visit[now-1] = [cnt+1,1]
        ST.append((cnt+1, now-1))

print(cnt)
print(*result)