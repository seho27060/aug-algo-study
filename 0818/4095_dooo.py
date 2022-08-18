while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    arr =[list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]

    max_val = 0
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = arr[i][j]
                if dp[i][j] > max_val:
                    max_val = dp[i][j]
            else:
                if arr[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    if dp[i][j] > max_val:
                        max_val = dp[i][j]

    print(max_val)