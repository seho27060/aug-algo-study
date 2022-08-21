while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*(M+1) for _ in range(N+1)]
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            ans = max(ans, dp[i][j])
    print(ans)