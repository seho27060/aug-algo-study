# DP를 활용한 최소값 계산문제
# 배열을 차례로 지나며 점프 가능한 거리와 최소 횟수를 갱신하며 진행

N = int(input())
lst = list(map(int, input().split()))

DP = [-1] * (N)
DP[0] = 0
for i in range(N-1):
    if DP[i] != -1:
        val = lst[i]
        for j in range(val, 0, -1):
            if i + j < N:
                if DP[i+j] == -1 or DP[i+j] > DP[i] + 1:
                    DP[i+j] = DP[i] + 1
print(DP[-1])