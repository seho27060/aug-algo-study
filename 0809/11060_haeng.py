from collections import deque
N = int(input())
road = list(map(int,input().split()))


dp=[100001]*N

ST = deque()
ST.append((0,0))
dp[0]=0
while ST:
    now,cnt = ST.popleft()

    for j in range(now+1,now+1+road[now]):
        if j<N and dp[j] > cnt+1:
            dp[j]=cnt+1
            ST.append((j,cnt+1))


if dp[N-1] == 100001:
    print(-1)
else:
    print(dp[N-1])