N,M =map(int,input().split())
K = int(input())

noRoad=[]
for _ in range(K):
    a,b,c,d = map(int,input().split())
    noRoad.append([max(a,c),max(b,d),min(a,c),min(b,d)])

dp = [[0]*(N+1) for _ in range(M+1)]

for i in range(1,N+1):
    if [i,0,i-1,0] in noRoad: break
    dp[0][i] = 1
for i in range(1,M+1):
    if [0,i,0,i-1] in noRoad: break
    dp[i][0] = 1


for y in range(1,M+1):
    for x in range(1,N+1):
        if [x,y,x-1,y] in noRoad:
            left = 0
        else:
            left = dp[y][x-1]

        if [x,y,x,y-1] in noRoad:
            up = 0
        else:
            up = dp[y-1][x]


        dp[y][x] = up + left

print(dp[M][N])