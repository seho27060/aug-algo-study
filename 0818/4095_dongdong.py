# 백준 4095 최대 정사각형 - dp 점화식 도출 생각하자...

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break  # input이 0이명 끝

    arr = [list(map(int, input().split())) for _ in range(N)]  # 사각형 배열

    # 정사각형은 뭐다... -> 네 변의 길이가 모두 같음 => 내가 위치한 칸을 기준으로 위, 왼, 대각선 방향이 1이면 정사각형
    # 공통된 길이를 구해야 하기 때문에 세 방향 중 최소길이를 구하고 내 길이까지 +1을 해준다

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    result = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if arr[i - 1][j - 1] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                if dp[i][j] > result:
                    result = dp[i][j]

    # print(dp)
    print(result)
