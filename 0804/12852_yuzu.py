dp = [0, 0, 1, 1, 2, 3, 2]
dp2 = [[], [1], [1, 2], [1, 3], [1, 2, 4], [1, 2, 4, 5], [1, 2, 6]]

n = int(input())
dp2 += [[] for _ in range(n-6)]
cnt = 7
while n+1 > cnt:
    if cnt%6 == 0:
        dp.append(min(dp[cnt//3]+1, dp[cnt//2]+1, dp[cnt-1]+1))
        if min(dp[cnt//3]+1, dp[cnt//2]+1, dp[cnt-1]+1) == dp[cnt // 3] + 1:
            dp2[cnt] += dp2[cnt//3]
        elif min(dp[cnt//3]+1, dp[cnt//2]+1, dp[cnt-1]+1) == dp[cnt // 2] + 1:
            dp2[cnt] += dp2[cnt//2]
        else:
            dp2[cnt] += dp2[cnt-1]
        dp2[cnt].append(cnt)
    elif cnt%3 == 0:
        dp.append(min(dp[cnt//3]+1, dp[cnt-1]+1))
        if min(dp[cnt // 3] + 1, dp[cnt-1] + 1) == dp[cnt // 3] + 1:
            dp2[cnt] += dp2[cnt//3]
        else:
            dp2[cnt] += dp2[cnt-1]
        dp2[cnt].append(cnt)
    elif cnt%2 == 0:
        dp.append(min(dp[cnt // 2] + 1, dp[cnt-1] + 1))
        if min(dp[cnt // 2] + 1, dp[cnt-1] + 1) == dp[cnt // 2] + 1:
            dp2[cnt] += dp2[cnt//2]
        else:
            dp2[cnt] += dp2[cnt-1]
        dp2[cnt].append(cnt)
    else:
        dp.append(dp[cnt-1]+1)
        dp2[cnt] += (dp2[cnt-1])
        dp2[cnt].append(cnt)
    cnt += 1
print(dp[n])
print(*sorted(dp2[n], reverse=True))