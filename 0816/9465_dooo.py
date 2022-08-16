TC = int(input())
for _ in range(TC):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    for j in range(1, n):
        for i in range(2):
            if i == 0:
                dp[i][j] = max(dp[i][j-1], dp[1][j-1] + arr[i][j])
            else:
                dp[i][j] = max(dp[i][j-1], dp[0][j-1] + arr[i][j])
    if dp[0][n-1] < dp[1][n-1]:
        print(dp[1][n-1])
    else:
        print(dp[0][n-1])