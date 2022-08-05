n, m = map(int, input().split())
k = int(input())
graph = [[[0]*(n+1) for _ in range(m+1)] for _ in range(2)]
for _ in range(k):
    a, b, c, d = map(int, input().split())
    if abs(c-a) == 1:
        graph[0][min(b, d)][min(c, a)] = 1
    else:
        graph[1][min(b, d)][min(c, a)] = 1

dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(1, n+1):
    if graph[0][0][i-1] == 0:
        dp[0][i] = 1
    else:
        break
for j in range(1, m+1):
    if graph[1][j-1][0] == 0:
        dp[j][0] = 1
    else:
        break

for i in range(1, m+1):
    for j in range(1, n+1):
        if graph[0][i][j-1] == 1 and graph[1][i-1][j] == 1:
            continue
        elif graph[0][i][j-1] == 1:
            dp[i][j] = dp[i-1][j]
        elif graph[1][i-1][j] == 1:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[m][n])