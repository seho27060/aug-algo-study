# 백준 11060 점프 점프


N = int(input())    # 미로 칸 수
Ai = list(map(int, input().split()))    # 얼마나 점프 할 수 있니?? 니가 그렇게 점프를 잘해?? 눈은 왜 그렇게 뜨니??
dp = [N + 1] * N     # 점프 횟수 기록을 위한 배열
dp[0] = 0

# 반복문으로 점프 확인
for i in range(N):
    for j in range(1, Ai[i]+1):  # 점프로 갈 수 있는 칸 수 확인
        if i + j < N:   # 점프가 가능하다면
            dp[i+j] = min(dp[i+j], dp[i]+1)     # 기록된 값과 새로 점프횟수+1 한 값 중 작은 값을 배열에 저장

# print(dp)

# 배열의 마지막 값 확인해서 출력
if dp[N-1] == N+1:
    print(-1)
else:
    print(dp[N-1])

# 값 저장을 어떻게 해야 할지 계속 고민 해보기...

