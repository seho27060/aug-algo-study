N = int(input())
RGB = []
for _ in range(N):
    RGB.append(list(map(int,input().split())))

result = []
for j in range(3):
    dp = [[999999999] * 3 for _ in range(N)]
    dp[0] = RGB[0][j]

    for k in range(3):
        if k != j:
            dp[1][k] = dp[0] + RGB[1][k]

    for i in range(2,N-1):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + RGB[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + RGB[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + RGB[i][2]

    if j == 0:
        dp[N-1][1] = min(dp[N-2][0],dp[N-2][2]) + RGB[N-1][1]
        dp[N-1][2] = min(dp[N-2][0],dp[N-2][1]) + RGB[N-1][2]
    elif j == 1:
        dp[N-1][0] = min(dp[N-2][1], dp[N-2][2]) + RGB[N-1][0]
        dp[N-1][2] = min(dp[N-2][0],dp[N-2][1]) + RGB[N-1][2]
    else:
        dp[N-1][0] = min(dp[N-2][1], dp[N-2][2]) + RGB[N-1][0]
        dp[N-1][1] = min(dp[N-2][0], dp[N-2][2]) + RGB[N-1][1]
    result.append(min(dp[-1]))

print(min(result))