# DP를 활용한 문제
# 처음에 색칠할 색을 제외한 나머지는 큰 값을 입력
# 마지막에는 처음에 선택한 색을 제외한 나머지 중 최소값을 선택

N = int(input())
color = [list(map(int,input().split())) for _ in range(N)]
# print(color)

ans = 1000000000

for i in range(3):
    dp = [[0] * 3 for _ in range(N)]
    
    for j in range(3):
        if i != j:
            dp[0][j] = 1000000000
        else:
            dp[0][j] = color[0][j]

    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + color[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + color[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + color[j][2]

    for j in range(3):
        if i != j:
            ans = min(ans, dp[N-1][j])
print(ans)