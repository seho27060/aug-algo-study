# 백준 2225 합분해

N, K = map(int, input().split())

dp = [[0] * 201 for _ in range(201)]  # 값(경우의 수)을 저장할 2차원 배열

for x in range(1, 201):  # N, K가 200 이내
    dp[1][x] = 1  # 1개로 x를 만드는 경우는 자기 자신인 경우밖에 없음
    dp[2][x] = x + 1  # 2개로 x를 만드는 경우 대충 5로 생각해보면 나옴
    dp[x][1] = x  # x개로 1을 만드는 경우 x개

# 점화식 : dp[i][j] = dp[i][j-1] + dp[i-1][j]
# 이런건 대체 어떻게 생각하는걸까.....

for i in range(2, 201):
    for j in range(2, 201):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000

print(dp[K][N])
