# 백준 17404 RGB거리 2
# 경우의 수는 세가지 - 첫번째 집이 빨, 초, 파
# 첫번째 집이 빨강이면 마지막집은 초록 또는 파랑 중 최솟값.....

import sys
INF = sys.maxsize

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)

dp = [[0] * 3 for _ in range(N)]

# 0 - 빨 1 - 초 2 - 파

# 첫번째 집이 빨강인 경우
dp[0][0] = arr[0][0]    # 첫번째 집 빨간색 고정
dp[0][1] = INF
dp[0][2] = INF
for i in range(1, N-1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]  # i번째에 빨간색을 고를 경우 이전값은 초, 파 저장값 중 최솟값을 가짐
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]  # i번째에 초록색을 고를 경우 이전값은 빨 , 파 저장값 중 최솟값을 가짐
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]  # i번째에 파란색을 고를 경우 이전 값은 빨, 초 저장값 중 최솟값을 가짐

# print(dp)
# 첫 집이 빨강인 경우 마지막 집은 초 또는 파를 골라야 한다. 이전에 (빨,초)중 최솟값 + 파 또는 (빨,파)중 최솟값 + 초
red = min(min(dp[N-2][0], dp[N-2][1]) + arr[N-1][2], min(dp[N-2][0], dp[N-2][2]) + arr[N-1][1])
# print(red)

# 첫번째 집이 초록인 경우 위와 동일
dp[0][0] = INF
dp[0][1] = arr[0][1]
dp[0][2] = INF
for i in range(1, N-1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]  # i번째에 빨간색을 고를 경우 이전값은 초, 파 저장값 중 최솟값을 가짐
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]  # i번째에 초록색을 고를 경우 이전값은 빨 , 파 저장값 중 최솟값을 가짐
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]  # i번째에 파란색을 고를 경우 이전 값은 빨, 초 저장값 중 최솟값을 가짐
# print(dp)

green = min(min(dp[N-2][1], dp[N-2][2]) + arr[N-1][0], min(dp[N-2][0], dp[N-2][1]) + arr[N-1][2])
# print(green)

# 첫번째 집이 파랑 인 경우 위와 동일
dp[0][0] = INF
dp[0][1] = INF
dp[0][2] = arr[0][2]    # 첫번째 집 파란 색 고정
for i in range(1, N-1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]  # i번째에 빨간색을 고를 경우 이전값은 초, 파 저장값 중 최솟값을 가짐
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]  # i번째에 초록색을 고를 경우 이전값은 빨 , 파 저장값 중 최솟값을 가짐
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]  # i번째에 파란색을 고를 경우 이전 값은 빨, 초 저장값 중 최솟값을 가짐
# print(dp)

blue = min(min(dp[N-2][1], dp[N-2][2]) + arr[N-1][0], min(dp[N-2][0], dp[N-2][2]) + arr[N-1][1])
# print(blue)

print(min(red, green, blue)) # 첫 집이 빨, 초, 파 중 최솟값을 출력
