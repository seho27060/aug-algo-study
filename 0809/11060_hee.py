import sys
INF = sys.maxsize
N = int(input())
A = list(map(int, input().split()))

DP = [INF] * 2000
DP[0] = 0
for i in range(N):
    for j in range(1, A[i]+1):
        DP[i+j] = min(DP[i]+1, DP[i+j])

if DP[N-1] == INF:
    print(-1)

else:
    print(DP[N-1])