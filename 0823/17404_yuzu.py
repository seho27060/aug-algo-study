n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def rgb(x):
    ans = 1e10
    dp = [[1e10]*3 for _ in range(n)]
    dp[0][x] = arr[0][x]
    for i in range(1, n):
        dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])

    for y in range(3):
        if x != y and ans > dp[-1][y]:
            ans = dp[-1][y]

    return ans

print(min(rgb(0), rgb(1), rgb(2)))