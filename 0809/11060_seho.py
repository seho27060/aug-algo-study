# 220809 11060 점프 점프
# 일자배열,각 숫자 범위내로 이동 가능
# 백트래킹? dp?
#  0 -> 1 이동, 최소 몇번 점프를 해야하는가/ 못가면 -1
# n < 1000

import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

dp = [float('inf')]*(n)
dp[0] = 0
for start in range(0,n):
    for end in range(lst[start]+1):
        if start+end < n:
            # print(start,start+end)
            if dp[start+end] > dp[start]+1:
                dp[start+end] = dp[start]+1
if dp[n-1] >= float("inf"):
    print(-1)
else:
    print(dp[n-1])